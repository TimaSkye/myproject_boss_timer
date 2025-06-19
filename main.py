import sys
from PyQt6 import QtWidgets, QtCore
from MainWindow import Ui_MainWindow

# Константа времени 19 минут 55 секунд. Время респавна боссов 20 минут. 5 секунд запас.
TIMER_DURATION = 19 * 60 + 55


class ButtonTimer:
    """Класс таймера для кнопки."""

    def __init__(self, button, name):
        self.button = button
        self.name = name
        self.remaining = 0
        self.active = False

    def start_timer(self):
        self.remaining = TIMER_DURATION
        self.active = True

    def tick(self):
        if self.active and self.remaining > 0:
            self.remaining -= 1
            if self.remaining == 0:
                self.active = False

    def is_active(self):
        return self.active

    def get_time(self):
        m, s = divmod(self.remaining, 60)
        return f'{m:02d}:{s:02d}'


class MainWindow(QtWidgets.QMainWindow):
    """Класс отображения рабочего окна программы."""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
