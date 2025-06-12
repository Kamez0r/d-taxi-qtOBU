from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QTimer, Signal, Qt
from pyqttoast import Toast, ToastPosition

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class LandingPage(AbstractAppWidget):

    request_auth = Signal()
    request_exit = Signal()
    _exit_press_count = None
    _exit_timer = None


    def __init__(self, parent=None):
        super().__init__(parent)

        screen_area = self.create_screen_area()

        btn_map   = self.create_btn_map()
        btn_text   = self.create_btn_text()
        btn_auth   = self.create_btn_auth()
        btn_config = self.create_btn_config()
        btn_exit   = self.create_btn_exit()


        self.set_screen_area(screen_area)
        self.set_buttons([btn_map, btn_text, btn_auth, btn_config, btn_exit])

    def create_screen_area(self):
        screen_area = QWidget()

        screen_layout = QVBoxLayout()
        screen_layout.addWidget(QLabel("D-TAXI OBU"))
        screen_layout.addWidget(QLabel("Digital-Taxi On Board Unit"))
        screen_layout.addWidget(QLabel("Software Version: xx"))
        screen_layout.addWidget(QLabel("AIRAC: 2606"))
        screen_layout.addWidget(QLabel("Auth Status: Not Connected"))
        screen_layout.addWidget(QLabel("Username: -"))
        screen_layout.addWidget(QLabel("Callsign: -"))

        screen_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        screen_area.setLayout(screen_layout)
        return screen_area

    def create_btn_map(self):
        btn_map = QPushButton("MAP")
        btn_map.setDisabled(True)
        return btn_map

    def create_btn_text(self):
        btn_text = QPushButton("TEXT")
        btn_text.setDisabled(True)
        return btn_text

    def create_btn_auth(self):
        btn_auth = QPushButton("AUTH")
        btn_auth.clicked.connect(self.request_auth.emit)
        return btn_auth

    def create_btn_config(self):
        btn_config = QPushButton("CONFIG")
        btn_config.setDisabled(True)
        return btn_config

    def create_btn_exit(self):
        btn_exit = QPushButton("EXIT")
        btn_exit.clicked.connect(self._handle_exit_click)
        self._exit_press_count = 0
        self._exit_timer = QTimer(self)
        self._exit_timer.setInterval(1000)  # ms — time to reset count
        self._exit_timer.setSingleShot(True)
        self._exit_timer.timeout.connect(self._reset_exit_count)
        return btn_exit

    def _handle_exit_click(self):
        self._exit_press_count += 1
        self._exit_timer.start()  # Restart countdown each click

        toast = Toast(self)
        toast.setDuration(1000)
        toast.setPosition(ToastPosition.BOTTOM_LEFT)
        toast.setMaximumOnScreen(5)
        toast.setPositionRelativeToWidget(self)
        toast.setTitle("Exit requested")
        toast.setText("Press [EXIT] " + str(5-self._exit_press_count) + " more times to exit.")
        toast.show()

        if self._exit_press_count == 5:
            self._exit_press_count = 0
            self._exit_timer.stop()
            self.request_exit.emit()  # ✅ Emit signal

    def _reset_exit_count(self):
        self._exit_press_count = 0
