from PySide6.QtCore import Qt
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, PyQt")
        self.setMinimumSize(800, 600)

        main_layout = QHBoxLayout()

        # Create screen_area (75% width)
        screen_area = QLabel("This is the screen")
        screen_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        screen_area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create button_area (25% width)
        button_area = QVBoxLayout()
        for label in ["B1", "B2", "B3", "B4", "B5"]:
            btn = QPushButton(label)
            btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
            button_area.addWidget(btn)

        # Add widgets to main_layout with stretch factors
        main_layout.addWidget(screen_area, stretch=3)   # 75%
        main_layout.addLayout(button_area, stretch=1)   # 25%

        # Wrap in central widget
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)