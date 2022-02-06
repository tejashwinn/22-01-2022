from PyQt5 import QtCore, QtGui, QtWidgets
from events import Ui_events_form


class Individual_Event_Button():

    def open_post(self, event):
        self.create_class_main_window = QtWidgets.QMainWindow()
        self.ui_class_create = Ui_events_form()
     
        self.ui_class_create.setupUi(self.create_class_main_window)
        self.ui_class_create.label_2.setText(self.name)
        self.ui_class_create.label.setText(self.description)
        self.ui_class_create.label_3.setText(self.date)
        self.create_class_main_window.show()

    def __init__(self, mainwindow, name, description, ui_te, date):
        self.mainwindow = mainwindow
        self.name = name
        self.description = description
        self.ui_te = ui_te
        
        self.date = date.rsplit(":", 1)[0]
        self.child = self.return_object()

    def return_object(self):
        self.events_view_2 = QtWidgets.QFrame(self.mainwindow)
        self.events_view_2.setGeometry(QtCore.QRect(830, 240, 229, 70))
        self.events_view_2.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_2.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view_2.setStyleSheet("*{\n"
                                         "position: absolute;\n"
                                         "width: 370px;\n"
                                         "height: 110px;\n"
                                         "left: 7px;\n"
                                         "top: 28px;\n"
                                         "\n"
                                         "background: rgba(0, 0, 0, 0.05);\n"
                                         "border: 1px solid rgba(0, 0, 0, 0.3);\n"
                                         "box-sizing: border-box;\n"
                                         "border-radius: 10px}")
        self.events_view_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_2.setObjectName("events_view_2")
        self.label_8 = QtWidgets.QLabel(self.events_view_2)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("position: absolute;\n"
                                   "left: 20px;\n"
                                   "right: 30px;\n"
                                   "top: 10px;\n"
                                   "bottom: 10px;\n"
                                   "\n"
                                   "font-family: Poppins;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 20px;\n"
                                   "line-height: 37px;\n"
                                   "letter-spacing: 0.05em;\n"
                                   "background: rgba(0, 0, 0, 0.01);\n"
                                   "color: #000000;\n"
                                   "border:0px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.events_view_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 211, 41))
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("position: absolute;\n"
                                   "left: 20px;\n"
                                   "right: 30px;\n"
                                   "top: 10px;\n"
                                   "bottom: 10px;\n"
                                   "\n"
                                   "font-family: Poppins;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 15px;\n"
                                   "line-height: 37px;\n"
                                   "letter-spacing: 0.05em;\n"
                                   "border:0px;\n"
                                   "background: rgba(0, 0, 0, 0.01);\n"
                                   "color: #000000;")
        self.label_9.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")

        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("mainwindow", str(self.name)))
        self.label_9.setText(_translate(
            "mainwindow", str(self.date.rsplit(":", 1)[0])))

        self.label_9.mousePressEvent = self.open_post
        self.label_8.mousePressEvent = self.open_post
        self.events_view_2.mousePressEvent = self.open_post

        return self.events_view_2
