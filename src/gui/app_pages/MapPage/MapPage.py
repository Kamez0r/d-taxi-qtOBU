from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class MapPage(AbstractAppWidget):
    request_taxi = Signal()
    request_ack = Signal()
    request_manual_release = Signal()
    request_back = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        screen_area = self.create_screen_area()

        self.btn_req = self.create_btn_req()
        self.btn_ack = self.create_btn_ack()
        self.btn_manual_release = self.create_btn_manual_release()
        self.btn_toggle_view = self.create_btn_toggle_view()
        self.btn_back = self.create_btn_back()

        self.set_screen_area(screen_area)
        self.set_buttons([self.btn_req, self.btn_ack, self.btn_manual_release, self.btn_toggle_view, self.btn_back])


    def create_btn_req(self):
        btn = QPushButton("REQUEST TAXI")
        btn.clicked.connect(self.taxi_requested)
        return btn

    def taxi_requested(self):
        self.request_taxi.emit()

    def create_btn_ack(self):
        btn = QPushButton("ACKNOWLEDGE")
        btn.setDisabled(True)
        btn.clicked.connect(self.ack_requested)
        return btn

    def ack_requested(self):
        self.request_ack.emit()

    def create_btn_manual_release(self):
        btn = QPushButton("MANUAL RELEASE")
        btn.clicked.connect(self.manual_release_requested)
        return btn

    def manual_release_requested(self):
        # Pre proccess data?
        self.request_manual_release.emit()
        return

    def create_btn_toggle_view(self):
        btn = QPushButton("TOGGLE VIEW")
        btn.setDisabled(True)
        return btn

    def create_btn_back(self):
        btn = QPushButton("BACK")
        btn.clicked.connect(self.request_back.emit)
        return btn


    def create_screen_area(self):
        screen_area = QWidget()

        screen_layout = QVBoxLayout()

        # Populate layout bellow this
        lbl = QLabel("This page will be the visual map to navigate with, this will display the taxi route, new instructions etc.")
        lbl.setWordWrap(True)
        screen_layout.addWidget(lbl)

        screen_layout.addWidget(QLabel(" "))
        screen_layout.addWidget(QLabel(" "))
        screen_layout.addWidget(QLabel(" "))

        # Populate layout above this

        screen_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        screen_area.setLayout(screen_layout)

        fnt = self.font()
        fnt.setPointSizeF(self.font().pointSizeF() * 1)
        screen_area.setFont(fnt)

        return screen_area