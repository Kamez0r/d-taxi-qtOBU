from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout
from pyqttoast import Toast, ToastPosition

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class AuthPage(AbstractAppWidget):
    request_back = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)


        screen_area = self.create_screen_area()

        btn_login = self.create_btn_login()
        btn_logout = self.create_btn_logout()
        btn_save   = self.create_btn_save()
        btn_blank_4 = self.create_btn_blank_pos4()

        btn_back = self.create_btn_back()

        self.set_screen_area(screen_area)
        self.set_buttons([btn_login, btn_logout, btn_save, btn_blank_4, btn_back])

    def create_btn_login(self):
        btn = QPushButton("LOGIN")
        btn.clicked.connect(self.login_requested)
        return btn

    def login_requested(self):
        toast = Toast(self)
        toast.setDuration(1000)
        toast.setPosition(ToastPosition.BOTTOM_LEFT)
        toast.setMaximumOnScreen(5)
        toast.setPositionRelativeToWidget(self)
        toast.setTitle("login requested")
        toast.show()
        return

    def create_btn_logout(self):
        btn = QPushButton("LOGOUT")
        btn.setDisabled(True)
        return btn

    def create_btn_save(self):
        btn = QPushButton("SAVE")
        btn.clicked.connect(self.save_credentials)
        return btn

    def save_credentials(self):
        # Action to save credentials
        self.request_back.emit()
        return

    def create_btn_blank_pos4(self):
        btn = QPushButton(" ")
        btn.setDisabled(True)
        return btn

    def create_btn_back(self):
        btn = QPushButton("BACK")
        btn.clicked.connect(self.request_back.emit)
        return btn

    def create_screen_area(self):
        screen_area = QWidget()

        screen_layout = QVBoxLayout()
        screen_layout.addWidget(QLabel("Auth Page"))
        screen_layout.addWidget(QLabel("Auth Page"))
        screen_layout.addWidget(QLabel("Auth Page"))
        screen_layout.addWidget(QLabel("Auth Page"))
        screen_layout.addWidget(QLabel("Auth Page"))

        screen_area.setLayout(screen_layout)
        return screen_area