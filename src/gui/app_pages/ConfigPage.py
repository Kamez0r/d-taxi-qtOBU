from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QSizePolicy, QComboBox

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class ConfigPage(AbstractAppWidget):
    request_save = Signal()
    request_back = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.combo_gps_source = None
        self.combo_heading_source = None
        self.input_api_baseurl = None
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
    
    def on_page_changed(self, page_index: int):
        self.input_api_baseurl.setText(self.running_config["api_baseurl"])
        self.combo_heading_source.setCurrentText(self.running_config["heading_source"])
        self.combo_gps_source.setCurrentText(self.running_config["gps_source"])

    def create_screen_area(self):
        screen_area = QWidget()
        layout = QVBoxLayout()

        lbl_title = QLabel("Configuration Page")
        lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fnt = lbl_title.font()
        fnt.setBold(True)
        lbl_title.setFont(fnt)
        lbl_title.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        layout.addWidget(lbl_title)

        # API Base URL
        layout.addWidget(QLabel("API Base URL:"))
        self.input_api_baseurl = QLineEdit(self)
        layout.addWidget(self.input_api_baseurl)

        # GPS Source
        layout.addWidget(QLabel("GPS Source:"))
        self.combo_gps_source = QComboBox(self)
        self.combo_gps_source.addItems(["SIMULATOR", "SENSOR(WIP)", "FSD(WIP)"]) # TODO the obvious...
        layout.addWidget(self.combo_gps_source)

        # Heading Source
        layout.addWidget(QLabel("Heading Source:"))
        self.combo_heading_source = QComboBox(self)
        self.combo_heading_source.addItems(["SIMULATOR", "SENSOR(WIP)", "FSD(WIP)"])
        layout.addWidget(self.combo_heading_source)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        screen_area.setLayout(layout)

        fnt = self.font()
        fnt.setPointSizeF(fnt.pointSizeF() * 2)
        screen_area.setFont(fnt)

        return screen_area

    def create_btn_save(self):
        btn = QPushButton("SAVE")
        btn.clicked.connect(self.save_config)
        return btn

    def create_btn_back(self):
        btn = QPushButton("BACK")
        btn.clicked.connect(self.request_back.emit)
        return btn

    def save_config(self):
        self.running_config["api_baseurl"] = self.input_api_baseurl.text()
        self.running_config["gps_source"] = self.combo_gps_source.currentText()
        self.running_config["heading_source"] = self.combo_heading_source.currentText()
        self.request_save.emit()
        self.request_back.emit()