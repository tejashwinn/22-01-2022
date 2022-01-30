from PyQt5 import QtCore, QtGui, QtWidgets
from create_posts import Ui_create_posts_form
from posts import Ui_posts_form
from sign_in import Sign_Up


class PasswordEdit(QtWidgets.QLineEdit):
    """
    A LineEdit with icons to show/hide password entries
    """
    CSS = '''QLineEdit {
        border-radius: 0px;
        height: 30px;
        margin: 0px 0px 0px 0px;
    }
    '''

    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

        # Set styles
        self.setStyleSheet(self.CSS)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # self.visibleIcon = load_icon("eye_visible.svg")
        # self.hiddenIcon = load_icon("eye_hidden.svg")
        self.visibleIcon = icon
        self.hiddenIcon = icon
        self.setEchoMode(QtWidgets.QLineEdit.Password)
        self.togglepasswordAction = self.addAction(
            self.visibleIcon, QtWidgets.QLineEdit.TrailingPosition)
        self.togglepasswordAction.triggered.connect(
            self.on_toggle_password_Action)
        self.password_shown = False

    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)
