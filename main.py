import sys
from wsgiref.simple_server import software_version

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
from src.gui.MainWindow import MainWindow

import json
import os

# Get the directory where main.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct full paths
software_version_path = os.path.join(base_dir, 'software_version.txt')
running_config_path = os.path.join(base_dir, 'running_config.json')
nav_data_path = os.path.join(base_dir, 'nav_data.json')
example_running_config_path = os.path.join(base_dir, 'example.running_config.json')
example_nav_data_path = os.path.join(base_dir, 'example.nav_data.json')

def load_data():
    # Load software_version
    with open(software_version_path, 'r') as f:
        software_version = f.readline()

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

    return software_version, running_config, nav_data

def save_new_running_config(new_running_config:dict):
    with open(running_config_path, 'w') as f:
        json.dump(new_running_config, f, indent=4)

def main():
    software_version, running_config, nav_data = load_data()

    app = QApplication(sys.argv)

    app.setFont(QFont("Consolas", pointSize=16))

    window = MainWindow(
        software_version = software_version,
        running_config = running_config,
        nav_data = nav_data
    )
    window.showFullScreen()
    # window.show()

    window.request_update_running_config.connect(save_new_running_config)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
