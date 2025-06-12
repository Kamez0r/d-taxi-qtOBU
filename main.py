import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
from src.gui.MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)

    app.setFont(QFont("Consolas", pointSize=16))

    # window = MainWindow()
    window.showFullScreen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
