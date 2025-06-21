import os
import sys
import time
import threading
import queue

import cv2
import numpy as np
from PIL import ImageGrab

import pyttsx3
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QIcon

from MainWindow import Ui_MainWindow

TIMER_DURATION = 19 * 60 + 55


def resource_path(relative_path):
    """
    Возвращает абсолютный путь к ресурсу, корректно работает как в режиме разработки, так и в собранном .exe.

    Аргументы:
        relative_path (str): Относительный путь к ресурсу.

    Возвращает:
        str: Абсолютный путь к ресурсу.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ButtonTimer:
    """
    Класс, реализующий таймер для кнопки с отображением оставшегося времени и изменением цвета текста.

    Атрибуты:
        button: Qt кнопка, связанная с таймером.
        name (str): Название таймера (обычно текст кнопки).
        remaining (int): Оставшееся время в секундах.
        active (bool): Флаг активности таймера.
        font (QFont): Шрифт для кнопки.
    """
    def __init__(self, button, name, font):
        """
        Инициализация таймера.

        Аргументы:
            button: Qt кнопка.
            name (str): Название таймера.
            font (QFont): Шрифт для текста кнопки.
        """
        self.button = button
        self.name = name
        self.remaining = 0
        self.active = False
        self.font = font
        self.set_text_color("black")

    def start(self):
        """
        Запускает таймер, устанавливая время в TIMER_DURATION и меняя цвет текста на красный.
        """
        self.remaining = TIMER_DURATION
        self.active = True
        self.set_text_color("red")

    def tick(self):
        """
        Уменьшает оставшееся время на 1 секунду, если таймер активен.
        При достижении 0 меняет цвет текста на зелёный и деактивирует таймер.
        """
        if self.active and self.remaining > 0:
            self.remaining -= 1
            if self.remaining == 0:
                self.active = False
                self.set_text_color("green")

    def is_active(self):
        """
        Проверяет, активен ли таймер.

        Возвращает:
            bool: True, если таймер активен, иначе False.
        """
        return self.active

    def get_time(self):
        """
        Возвращает оставшееся время в формате MM:SS.

        Возвращает:
            str: Форматированное время.
        """
        m, s = divmod(self.remaining, 60)
        return f"{m:02d}:{s:02d}"

    def set_text_color(self, color):
        """
        Устанавливает цвет текста кнопки и применяет шрифт.

        Аргументы:
            color (str): Цвет текста (например, "red", "green", "black").
        """
        self.button.setFont(self.font)
        self.button.setStyleSheet(f"color: {color};")


class ScannerThread(QtCore.QThread):
    """
    Поток для фонового сканирования экрана на наличие изображений боссов с помощью шаблонного сопоставления.

    Сигналы:
        boss_detected (str): Сигнал с именем обнаруженного босса.
    """
    boss_detected = pyqtSignal(str)

    def __init__(self, boss_images, template_to_boss_name):
        """
        Инициализация потока сканера.

        Аргументы:
            boss_images (dict): Словарь с шаблонами изображений боссов.
            template_to_boss_name (dict): Сопоставление ключей шаблонов с именами боссов.
        """
        super().__init__()
        self.boss_images = boss_images
        self.template_to_boss_name = template_to_boss_name
        self.active = False
        self.last_detected_boss = None
        self.lock = threading.Lock()

    def run(self):
        """
        Основной цикл потока: периодически захватывает экран, ищет совпадения с шаблонами,
        при обнаружении нового босса отправляет сигнал boss_detected.
        """
        while True:
            with self.lock:
                if not self.active:
                    break
            try:
                screenshot = ImageGrab.grab()
                screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
                for template_key, template in self.boss_images.items():
                    res = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, _ = cv2.minMaxLoc(res)
                    if max_val >= 0.9 and self.last_detected_boss != template_key:
                        boss_name = self.template_to_boss_name.get(template_key, template_key)
                        self.last_detected_boss = template_key
                        self.boss_detected.emit(boss_name)
                        break
                else:
                    self.last_detected_boss = None
            except Exception as e:
                print(f"Ошибка сканера: {e}")
            time.sleep(0.5)

    def start_scan(self):
        """
        Активирует сканирование и запускает поток, если он ещё не запущен.
        """
        with self.lock:
            self.active = True
        if not self.isRunning():
            self.start()

    def stop_scan(self):
        """
        Деактивирует сканирование, что приведёт к завершению цикла run().
        """
        with self.lock:
            self.active = False


class SpeechEngine:
    """
    Класс для озвучки текста с помощью pyttsx3 в отдельном потоке, чтобы не блокировать GUI.
    """
    def __init__(self, rate_delta=-5, volume=1.0):
        """
        Инициализация движка озвучки и запуск рабочего потока.

        Аргументы:
            rate_delta (int): Смещение скорости речи относительно стандартной.
            volume (float): Громкость речи (0.0 - 1.0).
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.engine.getProperty('rate') + rate_delta)
        self.engine.setProperty('volume', volume)
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._worker, daemon=True)
        self.thread.start()

    def _worker(self):
        """
        Цикл рабочего потока, который последовательно озвучивает поступающие тексты из очереди.
        """
        while True:
            text = self.queue.get()
            if text is None:
                break
            self.engine.say(text)
            self.engine.runAndWait()
            self.queue.task_done()

    def speak(self, text):
        """
        Добавляет текст в очередь для озвучки.

        Аргументы:
            text (str): Текст для озвучивания.
        """
        self.queue.put(text)

    def stop(self):
        """
        Останавливает рабочий поток озвучки.
        """
        self.queue.put(None)


class MainWindow(QtWidgets.QMainWindow):
    """
    Главное окно приложения с кнопками таймеров, сканером и озвучкой.
    """
    BUTTON_NAMES = [
        "btn_naga", "btn_pixi", "btn_lancer", "btn_gvard", "btn_scare", "btn_kurolisk", "btn_vasilisk",
        "btn_sirena", "btn_kuru", "btn_triton", "btn_orc", "btn_troll", "btn_ogr", "btn_kobold",
        "btn_kaballo", "btn_flind", "btn_garpy", "btn_gigant", "btn_minotaur", "btn_chabon",
        "btn_bug", "btn_leprikon", "btn_skelet", "btn_spider"
    ]

    def __init__(self):
        """
        Инициализация GUI, таймеров, сканера и озвучки.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.speech = SpeechEngine()

        font = QFont("Comic Sans MS", 7, QFont.Weight.Bold)
        self.timers = []
        for name in self.BUTTON_NAMES:
            btn = getattr(self.ui, name)
            timer = ButtonTimer(btn, btn.text(), font)
            btn.clicked.connect(lambda _, t=timer: self.handle_button(t))
            self.timers.append(timer)

        self.ui.label_now.setText("")
        self.ui.label_next.setText("")
        self.ui.label_timer.setText("")

        self.boss_images = self._load_boss_images()
        self.template_to_boss_name = {name[4:]: getattr(self.ui, name).text() for name in self.BUTTON_NAMES}

        self.scanner_active = False
        self.scanner_thread = ScannerThread(self.boss_images, self.template_to_boss_name)
        self.scanner_thread.boss_detected.connect(self.on_boss_detected)

        self.ui.btn_scaner.clicked.connect(self.toggle_scanner)
        self.ui.btn_scaner.setText("Сканер боссов")
        self.ui.btn_scaner.setStyleSheet("color: black;")
        self.scaner_font = self.ui.btn_scaner.font()
        self.ui.btn_scaner.setFixedSize(self.ui.btn_scaner.size())

        self.global_timer = QtCore.QTimer(self)
        self.global_timer.timeout.connect(self.tick_all)
        self.global_timer.start(1000)

    def _load_boss_images(self):
        """
        Загружает шаблоны изображений боссов из папки 'src'.

        Возвращает:
            dict: Словарь {ключ: изображение в градациях серого}.
        """
        boss_images = {}
        src_folder = resource_path("src")
        for filename in os.listdir(src_folder):
            if filename.lower().endswith(".bmp"):
                key = os.path.splitext(filename)[0]
                img_path = os.path.join(src_folder, filename)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    boss_images[key] = img
        return boss_images

    def handle_button(self, timer):
        """
        Обработчик нажатия кнопки: запускает соответствующий таймер и обновляет метку текущего босса.

        Аргументы:
            timer (ButtonTimer): Таймер, связанный с кнопкой.
        """
        timer.start()
        self.ui.label_now.setText(timer.name)

    def tick_all(self):
        """
        Обновляет все активные таймеры каждую секунду,
        озвучивает имя босса за 3 секунды до окончания таймера,
        обновляет метки интерфейса.
        """
        for timer in self.timers:
            if timer.is_active() and timer.remaining == 3:
                self.speech.speak(timer.name)
            timer.tick()
        self.update_labels()

    def update_labels(self):
        """
        Обновляет метки следующего босса и оставшегося времени.
        Если активных таймеров нет — очищает метки.
        """
        active_timers = [t for t in self.timers if t.is_active()]
        if active_timers:
            next_timer = min(active_timers, key=lambda t: t.remaining)
            self.ui.label_next.setText(next_timer.name)
            self.ui.label_timer.setText(next_timer.get_time())
        else:
            self.ui.label_next.setText("")
            self.ui.label_timer.setText("")

    def toggle_scanner(self):
        """
        Включает или выключает сканер экрана.
        При переключении обновляет текст и цвет кнопки, а также озвучивает статус.
        """
        if self.scanner_active:
            self.scanner_thread.stop_scan()
            self.ui.btn_scaner.setText("Сканер деактивирован")
            self.ui.btn_scaner.setStyleSheet("color: red;")
            self.speech.speak("Сканер деактивирован")
        else:
            self.scanner_thread.start_scan()
            self.ui.btn_scaner.setText("Сканер активирован")
            self.ui.btn_scaner.setStyleSheet("color: green;")
            self.speech.speak("Сканер активирован")
        self.scanner_active = not self.scanner_active
        self.ui.btn_scaner.setFont(self.scaner_font)
        self.ui.btn_scaner.setFixedSize(self.ui.btn_scaner.size())

    def on_boss_detected(self, boss_name):
        """
        Обработчик сигнала обнаружения босса сканером.
        Запускает таймер соответствующего босса и обновляет метку текущего босса.

        Аргументы:
            boss_name (str): Имя обнаруженного босса.
        """
        for timer in self.timers:
            if timer.name == boss_name:
                timer.start()
                self.ui.label_now.setText(boss_name)
                break

    def closeEvent(self, event):
        """
        Обработчик закрытия окна.
        Корректно останавливает потоки сканера и озвучки.
        """
        self.scanner_thread.stop_scan()
        self.scanner_thread.quit()
        self.scanner_thread.wait()
        self.speech.stop()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    icon = QIcon(resource_path("icon.ico"))
    app.setWindowIcon(icon)
    window = MainWindow()
    window.setWindowIcon(icon)
    window.show()
    sys.exit(app.exec())
