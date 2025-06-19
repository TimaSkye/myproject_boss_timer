import ctypes
import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from MainWindow import Ui_MainWindow

myappid = 'home.boss_timer.version01'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# 19 минут 55 секунд
TIMER_DURATION = 19 * 60 + 55

class ButtonTimer:
    def __init__(self, button, name, font):
        self.button = button
        self.name = name
        self.remaining = 0
        self.active = False
        self.font = font
        self.set_text_color("black")  # По умолчанию чёрный

    def start(self):
        self.remaining = TIMER_DURATION
        self.active = True
        self.set_text_color("red")

    def tick(self):
        if self.active and self.remaining > 0:
            self.remaining -= 1
            if self.remaining == 0:
                self.active = False
                self.set_text_color("green")

    def is_active(self):
        return self.active

    def get_time(self):
        m, s = divmod(self.remaining, 60)
        return f"{m:02d}:{s:02d}"

    def set_text_color(self, color):
        # Устанавливаем цвет и шрифт
        self.button.setFont(self.font)
        self.button.setStyleSheet(f"color: {color};")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        # Создаём нужный шрифт
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(True)

        # Список кнопок из вашего дизайна
        self.button_names = [
            "btn_naga", "btn_pixi", "btn_lancer", "btn_gvard", "btn_scare", "btn_kurolisk", "btn_vasilisk",
            "btn_sirena", "btn_kuru", "btn_triton", "btn_orc", "btn_troll", "btn_ogr", "btn_kobold",
            "btn_kaballo", "btn_flind", "btn_garpy", "btn_gigant", "btn_minotaur", "btn_chabon",
            "btn_bug", "btn_leprikon", "btn_skelet", "btn_spider"
        ]

        self.timers = []
        for name in self.button_names:
            btn = getattr(self.ui, name)
            timer = ButtonTimer(btn, btn.text(), font)
            btn.clicked.connect(lambda _, t=timer: self.handle_button(t))
            self.timers.append(timer)

        # Инициализация меток
        self.ui.label_now.setText("")
        self.ui.label_next.setText("")
        self.ui.label_timer.setText("")

        self.global_timer = QtCore.QTimer(self)
        self.global_timer.timeout.connect(self.tick_all)
        self.global_timer.start(1000)

    def handle_button(self, timer):
        # Только если таймер не активен — запускаем и красим в красный
        if not timer.is_active():
            timer.start()
            self.ui.label_now.setText(timer.name)

    def tick_all(self):
        for timer in self.timers:
            timer.tick()
        self.update_labels()

    def update_labels(self):
        active_timers = [t for t in self.timers if t.is_active()]
        if active_timers:
            next_timer = min(active_timers, key=lambda t: t.remaining)
            self.ui.label_next.setText(next_timer.name)
            self.ui.label_timer.setText(next_timer.get_time())
        else:
            self.ui.label_next.setText("")
            self.ui.label_timer.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    icon = QIcon("icon.ico")
    app.setWindowIcon(icon)
    window = MainWindow()
    window.setWindowIcon(icon)
    window.show()
    sys.exit(app.exec())
