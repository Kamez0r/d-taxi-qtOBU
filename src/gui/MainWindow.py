from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from src.api.API import API
from src.gui.app_pages.AuthPage import AuthPage
from src.gui.app_pages.ConfigPage import ConfigPage
from src.gui.app_pages.LandingPage import LandingPage
from src.gui.app_pages.MapPage.MapPage import MapPage
from src.gui.app_pages.TextPage import TextPage


class MainWindow(QMainWindow):

    request_update_running_config = Signal(dict)

    software_version: str
    running_config: dict
    nav_data: dict

    def __init__(self,
        software_version : str,
        running_config : dict,
        nav_data : dict
    ):
        super().__init__()
        self.setWindowTitle("Hello, PyQt")
        self.setMinimumSize(1920, 1080)

        self.software_version = software_version
        self.running_config = running_config
        self.nav_data = nav_data

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
        self.auth_page.request_login.connect(self._auth_request_login)
        self.auth_page.request_logout.connect(self._auth_request_logout)
        self.auth_page.request_save.connect(self.save_current_running_config)
        self.auth_page.request_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.auth_page)

        # Config page
        self.config_page = ConfigPage(self)
        self.config_page.request_save.connect(self.save_current_running_config)
        self.config_page.request_back.connect(self.request_landing_page)
        self.central_widget.addWidget(self.config_page)


        self.setCentralWidget(self.central_widget)
        self.request_landing_page()

        self.api = API(self)


    def save_current_running_config(self):
        return self.action_save_running_config(self.running_config)

    def action_save_running_config(self, new_running_config):
        self.running_config = new_running_config
        self.request_update_running_config.emit(new_running_config)

    def _auth_request_login(self):
        self.api.call_login(self.auth_page.login_finished)

    def _auth_request_logout(self):
        self.api.call_logout(self.auth_page.logout_finished)

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
