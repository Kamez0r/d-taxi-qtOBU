from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, PyQt")
        self.setMinimumSize(400, 300)

        label = QLabel("Hello, World!", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
