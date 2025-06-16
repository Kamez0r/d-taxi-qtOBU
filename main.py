import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
from src.gui.MainWindow import MainWindow

import json
import os

def load_data():
    # Define file paths
    running_config_path = 'running_config.json'
    nav_data_path = 'nav_data.json'
    example_running_config_path = 'example.running_config.json'
    example_nav_data_path = 'example.nav_data.json'

    # Load or create running_config
    if not os.path.exists(running_config_path):
        with open(example_running_config_path, 'r') as f:
            running_config = json.load(f)
        with open(running_config_path, 'w') as f:
            json.dump(running_config, f, indent=4)
    else:
        with open(running_config_path, 'r') as f:
            running_config = json.load(f)

    # Load or create nav_data
    if not os.path.exists(nav_data_path):
        with open(example_nav_data_path, 'r') as f:
            nav_data = json.load(f)
        with open(nav_data_path, 'w') as f:
            json.dump(nav_data, f, indent=4)
    else:
        with open(nav_data_path, 'r') as f:
            nav_data = json.load(f)

    return running_config, nav_data


def main():
    running_config, nav_data = load_data()

    app = QApplication(sys.argv)

    app.setFont(QFont("Consolas", pointSize=16))

    window = MainWindow()
    window.showFullScreen()
    # window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
