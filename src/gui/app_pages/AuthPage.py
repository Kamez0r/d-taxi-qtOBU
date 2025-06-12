from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QLineEdit, QSizePolicy
from pyqttoast import Toast, ToastPosition

from src.gui.app_pages.AbstractAppWidget import AbstractAppWidget


class AuthPage(AbstractAppWidget):
    request_login = Signal()
    request_logout = Signal()
    request_save = Signal()
    request_back = Signal()

    input_callsign : QLineEdit
    input_airport  : QLineEdit
    input_auth_key : QLineEdit

    def __init__(self, parent=None):
        super().__init__(parent)

        screen_area = self.create_screen_area()

        self.btn_login = self.create_btn_login()
        self.btn_logout = self.create_btn_logout()
        self.btn_save   = self.create_btn_save()
        self.btn_blank_4 = self.create_btn_blank_pos4()

        self.btn_back = self.create_btn_back()

        self.set_screen_area(screen_area)
        self.set_buttons([self.btn_login, self.btn_logout, self.btn_save, self.btn_blank_4, self.btn_back])


    def create_screen_area(self):
        screen_area = QWidget()

        screen_layout = QVBoxLayout()
        lbl_title = QLabel("Auth Page")
        lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_title.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        fnt = lbl_title.font()
        fnt.setBold(True)
        lbl_title.setFont(fnt)
        screen_layout.addWidget(lbl_title)

        screen_layout.addWidget(QLabel("Callsign:"))
        self.input_callsign = QLineEdit(self)
        self.input_callsign.setMaxLength(30)
        screen_layout.addWidget(self.input_callsign)

        screen_layout.addWidget(QLabel("Airport ICAO:"))
        self.input_airport = QLineEdit(self)
        self.input_airport.setMaxLength(4)
        screen_layout.addWidget(self.input_airport)

        screen_layout.addWidget(QLabel("Auth Key:"))
        self.input_auth_key = QLineEdit(self)
        screen_layout.addWidget(self.input_auth_key)

        screen_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        screen_area.setLayout(screen_layout)

        fnt = self.font()
        fnt.setPointSizeF(self.font().pointSizeF() * 2)
        screen_area.setFont(fnt)

        return screen_area

    def create_btn_login(self):
        btn = QPushButton("LOGIN")
        btn.clicked.connect(self.login_requested)
        return btn

    def login_requested(self):
        self.btn_login.setDisabled(True)
        self.input_callsign.setDisabled(True)
        self.input_airport.setDisabled(True)
        self.input_auth_key.setDisabled(True)


        toast = Toast(self)
        toast.setDuration(2000)
        toast.setPosition(ToastPosition.BOTTOM_LEFT)
        toast.setMaximumOnScreen(5)
        toast.setPositionRelativeToWidget(self)
        toast.setTitle("Login request sent")
        toast.show()

        self.request_login.emit()

        return

    def create_btn_logout(self):
        btn = QPushButton("LOGOUT")
        btn.setDisabled(True)
        btn.clicked.connect(self.logout_requested)
        return btn

    def logout_requested(self):
        self.btn_logout.setDisabled(True)
        self.request_logout.emit()

    def create_btn_save(self):
        btn = QPushButton("SAVE")
        btn.clicked.connect(self.save_requested)
        return btn

    def save_credentials(self):
        return

    def save_requested(self):
        # Action to save credentials
        self.save_credentials()
        self.request_back.emit()
        return

    def create_btn_blank_pos4(self):
        btn = QPushButton(" ")
        btn.setDisabled(True)
        return btn

    def create_btn_back(self):
        btn = QPushButton("BACK")
        btn.clicked.connect(self.request_back.emit)
        return btn
