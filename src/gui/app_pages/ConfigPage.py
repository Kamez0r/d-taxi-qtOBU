from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class ConfigPage(AbstractAppWidget):
    request_save = Signal()
    request_back = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        screen_area = self.create_screen_area()

        btn_blank_1 = QPushButton(" ")
        btn_blank_1.setDisabled(True)

        btn_blank_2 = QPushButton(" ")
        btn_blank_2.setDisabled(True)

        self.btn_save = self.create_btn_save()

        btn_blank_4 = QPushButton(" ")
        btn_blank_4.setDisabled(True)

        self.btn_back = self.create_btn_back()

        self.set_screen_area(screen_area)
        self.set_buttons([btn_blank_1, btn_blank_2, self.btn_save, btn_blank_4, self.btn_back])

    def create_screen_area(self):
        screen_area = QWidget()

        screen_layout = QVBoxLayout()

        # Populate layout bellow this
        lbl = QLabel("This page is unused, it could be populated with checkboxes, sliders and other relevant things")
        lbl.setWordWrap(True)
        screen_layout.addWidget(lbl)

        screen_layout.addWidget(QLabel(" "))
        screen_layout.addWidget(QLabel("GPS Source: Sensor/Simulator/Webview"))
        screen_layout.addWidget(QLabel("Heading Source Source: Sensor/Simulator/Webview"))

        # Populate layout above this

        screen_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        screen_area.setLayout(screen_layout)

        fnt = self.font()
        fnt.setPointSizeF(self.font().pointSizeF() * 2)
        screen_area.setFont(fnt)

        return screen_area

    def create_btn_save(self):
        btn = QPushButton("SAVE")
        btn.clicked.connect(self.save_requested)
        return btn

    def save_config(self):
        # Pre proccess data?
        self.request_save.emit()
        return

    def save_requested(self):
        self.save_config()
        self.request_back.emit()
        return

    def create_btn_back(self):
        btn = QPushButton("BACK")
        btn.clicked.connect(self.request_back.emit)
        return btn