from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QLabel

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class AuthPage(AbstractAppWidget):
    btn_back = Signal()

    def __init__(self):
        super().__init__()

        btn1 = QPushButton("LOGIN")
        btn2 = QPushButton("LOGOUT")
        btn3 = QPushButton("SAVE")
        btn4 = QPushButton("")
        btn5 = QPushButton("BACK")

        self.set_screen_area(QLabel("Auth Page"))
        self.set_buttons([btn1, btn2, btn3, btn4, btn5])