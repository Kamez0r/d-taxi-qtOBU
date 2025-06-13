from PySide6.QtWidgets import *

from src.gui.app_pages.AuthPage import AuthPage
from src.gui.app_pages.ConfigPage import ConfigPage
from src.gui.app_pages.LandingPage import LandingPage
from src.gui.app_pages.MapPage import MapPage
from src.gui.app_pages.TextPage import TextPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, PyQt")
        self.setMinimumSize(1920, 1080)

        self.central_widget = QStackedWidget(self)

        # Landing page
        self.landing_page = LandingPage(self)
        self.landing_page.request_map.connect(self.request_map_page)
        self.landing_page.request_text.connect(self.request_text_page)
        self.landing_page.request_auth.connect(self.request_auth_page)
        self.landing_page.request_config.connect(self.request_config_page)
        self.landing_page.request_exit.connect(self.close)
        self.central_widget.addWidget(self.landing_page)

        # Map page
        self.map_page = MapPage(self)
        self.map_page.request_taxi.connect(self.action_request_taxi)
        self.map_page.request_ack.connect(self.action_acknowledge)
        # self.map_page.request_manual_release.connect(self.?)
        self.map_page.request_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.map_page)

        # Text page
        self.text_page = TextPage(self)
        self.text_page.request_taxi.connect(self.action_request_taxi)
        self.text_page.request_ack.connect(self.action_acknowledge)
        # self.text_page.request_recall.connect(self.?)
        self.text_page.request_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.text_page)

        # Auth page
        self.auth_page = AuthPage(self)
        # self.auth_page.request_login.connect(self.?)
        # self.auth_page.request_logout.connect(self.?)
        # self.auth_page.request_save.connect(self.?)
        self.auth_page.request_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.auth_page)

        # Config page
        self.config_page = ConfigPage(self)
        # self.config_page.request_save.connect(self.?)
        self.config_page.request_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.config_page)



        self.setCentralWidget(self.central_widget)
        self.request_landing_page()

    def request_landing_page(self):
        self.central_widget.setCurrentWidget(self.landing_page)

    def request_map_page(self):
        self.central_widget.setCurrentWidget(self.map_page)

    def request_text_page(self):
        self.central_widget.setCurrentWidget(self.text_page)

    def request_config_page(self):
        self.central_widget.setCurrentWidget(self.config_page)

    def request_auth_page(self):
        self.central_widget.setCurrentWidget(self.auth_page)

    def action_request_taxi(self):
        pass

    def action_acknowledge(self):
        pass
