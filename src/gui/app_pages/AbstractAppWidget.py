
from src.gui import MainWindow
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QPushButton, QHBoxLayout



class AbstractAppWidget(QWidget):
    software_version: str
    running_config: dict
    nav_data: dict

    def __init__(self, parent: MainWindow):
        super().__init__(parent)

        self.software_version = parent.software_version
        self.running_config = parent.running_config
        self.nav_data = parent.nav_data
        parent.request_update_running_config.connect(self.on_running_config_changed)
        parent.central_widget.currentChanged.connect(self.on_page_changed)

        self.main_layout = QHBoxLayout()
        self.screen_area = QWidget()
        self.button_area = QVBoxLayout()

        self.main_layout.addWidget(self.screen_area, stretch=3)
        self.main_layout.addLayout(self.button_area, stretch=1)

        self.setLayout(self.main_layout)

    def on_page_changed(self, page_index: int):
        pass

    def on_running_config_changed(self, new_running_config: dict):
        pass

    def set_screen_area(self, screen_area: QWidget):
        # Remove the old one
        self.main_layout.removeWidget(self.screen_area)
        self.screen_area.deleteLater()

        self.screen_area = screen_area
        self.main_layout.insertWidget(0, self.screen_area, stretch=3)

    def set_buttons(self, buttons: list[QPushButton]):
        # Remove old buttons
        while self.button_area.count():
            item = self.button_area.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for btn in buttons:
            btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
            font = self.font()
            font.setPointSizeF(self.font().pointSizeF() * 1.5)
            btn.setFont(font)
            self.button_area.addWidget(btn)
