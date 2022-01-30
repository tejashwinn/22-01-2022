
from PyQt5 import QtCore, QtGui, QtWidgets


class Pass():
    
    def __init__(self, line_edit, line_edit_frame):
        self.postion = False
        self.line_edit = line_edit
        self.line_edit_frame = line_edit_frame
        self.load_icons()
        self.set_up
        

    def load_icons(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.eye = icon
        icon.addPixmap(QtGui.QPixmap(
            "c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/eye-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eye_off = icon

    def set_up_toggle(self):
        self.show_password_switch = QtWidgets.QToolButton(self.line_edit_frame)
        self.show_password_switch.setGeometry(QtCore.QRect(400, 40, 27, 22))
        self.show_password_switch.setStyleSheet("border:0px white;")
        self.show_password_switch.setObjectName("show_password")
        self.show_password_switch.setIcon(self.eye_off)
        self.show_password_switch.clicked.connect(self.action)

    def action(self):
        if self.postion:
            self.line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.postion = False
        else:
            self.line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.postion = True

    def set_up(self):
        self.line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.postion = True
