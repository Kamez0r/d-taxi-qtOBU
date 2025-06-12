from PySide6.QtWidgets import *

from src.gui.app_pages.LandingPage import LandingPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, PyQt")
        self.setMinimumSize(1280, 720)

        # Wrap in central widget
        main_widget = LandingPage()
        main_widget.request_exit.connect(self.close)


        self.setCentralWidget(main_widget)