from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtCore import QTimer, Signal
from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class LandingPage(AbstractAppWidget):
    btn5_triggered = Signal()  # ✅ This signal is emitted after 5 quick presses

    def __init__(self):
        super().__init__()

        self._btn5_press_count = 0
        self._btn5_timer = QTimer(self)
        self._btn5_timer.setInterval(1000)  # ms — time to reset count
        self._btn5_timer.setSingleShot(True)
        self._btn5_timer.timeout.connect(self._reset_btn5_count)

        btn1 = QPushButton("MAP")
        btn2 = QPushButton("TEXT")
        btn3 = QPushButton("AUTH")
        btn4 = QPushButton("CONFIG")
        btn5 = QPushButton("EXIT")

        btn5.clicked.connect(self._handle_btn5_click)

        self.set_screen_area(QLabel("Hello, World!"))
        self.set_buttons([btn1, btn2, btn3, btn4, btn5])


    def _handle_btn5_click(self):
        self._btn5_press_count += 1
        self._btn5_timer.start()  # Restart countdown each click

        if self._btn5_press_count == 5:
            self._btn5_press_count = 0
            self._btn5_timer.stop()
            self.btn5_triggered.emit()  # ✅ Emit signal

    def _reset_btn5_count(self):
        self._btn5_press_count = 0
