from PySide6.QtWidgets import *

from src.gui.app_pages.AuthPage import AuthPage
from src.gui.app_pages.LandingPage import LandingPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, PyQt")
        self.setMinimumSize(1920, 1080)

        self.central_widget = QStackedWidget(self)

        # Landing page
        self.landing_page = LandingPage(self)
        self.landing_page.request_auth.connect(self.request_auth_page)
        self.landing_page.request_exit.connect(self.close)
        self.central_widget.addWidget(self.landing_page)

        # Auth page
        self.auth_page = AuthPage(self)
        self.auth_page.btn_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.auth_page)


        self.setCentralWidget(self.central_widget)
        self.request_landing_page()

    def request_landing_page(self):
        self.central_widget.setCurrentWidget(self.landing_page)

    def request_auth_page(self):
        self.central_widget.setCurrentWidget(self.auth_page)