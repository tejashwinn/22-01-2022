# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\temp_file_storage\components.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(1070, 878)
        mainwindow.setStyleSheet("")
        self.post_button = QtWidgets.QPushButton(mainwindow)
        self.post_button.setGeometry(QtCore.QRect(10, 10, 525, 80))
        self.post_button.setMaximumSize(QtCore.QSize(525, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button.setFont(font)
        self.post_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button.setObjectName("post_button")
        self.events_view = QtWidgets.QFrame(mainwindow)
        self.events_view.setGeometry(QtCore.QRect(600, 170, 229, 70))
        self.events_view.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view.setStyleSheet("#events_view{\n"
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
        self.events_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view.setObjectName("events_view")
        self.label_6 = QtWidgets.QLabel(self.events_view)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("position: absolute;\n"
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
"color: #000000;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.events_view)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 211, 41))
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("position: absolute;\n"
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
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.events_view_2 = QtWidgets.QFrame(mainwindow)
        self.events_view_2.setGeometry(QtCore.QRect(410, 430, 461, 70))
        self.events_view_2.setMinimumSize(QtCore.QSize(0, 70))
        self.events_view_2.setMaximumSize(QtCore.QSize(461, 70))
        self.events_view_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view_2.setStyleSheet("#events_view_2{\n"
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
        self.label_8.setGeometry(QtCore.QRect(10, 0, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
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
"font-size: 15\n"
"px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.events_view_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 441, 21))
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
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(mainwindow)
        self.pushButton.setGeometry(QtCore.QRect(240, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assests/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(mainwindow)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 380, 40, 40))
        self.pushButton_2.setStyleSheet("*{border-radius:0px;}\n"
":pressed{\n"
"    border: 3px solid  #FF0000;\n"
"boder:10px;\n"
"border-radius: 8px;\n"
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\.qt_for_python\\uic\\temp_file_storage\\assests/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.sign_up_button = QtWidgets.QPushButton(mainwindow)
        self.sign_up_button.setGeometry(QtCore.QRect(390, 280, 425, 40))
        self.sign_up_button.setStyleSheet("\n"
"#sign_up_button{\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"/* identical to box height */\n"
"\n"
"align-items: center;\n"
"\n"
"/* Grey / Light */\n"
"\n"
"color: white;\n"
"background: #4F4F4F;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#sign_up_button:pressed {\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_in_button = QtWidgets.QPushButton(mainwindow)
        self.sign_in_button.setGeometry(QtCore.QRect(390, 330, 425, 40))
        self.sign_in_button.setStyleSheet("\n"
"#sign_in_button{\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"/* identical to box height */\n"
"\n"
"align-items: center;\n"
"\n"
"/* Grey / Light */\n"
"\n"
"\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#sign_in_button:pressed {\n"
"    border-style: inset;\n"
"    color: white;\n"
"background: #4F4F4F;\n"
"border-radius: 8px;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.sign_in_button.setObjectName("sign_in_button")
        self.class_view_frame = QtWidgets.QFrame(mainwindow)
        self.class_view_frame.setGeometry(QtCore.QRect(449, 630, 500, 140))
        self.class_view_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.class_view_frame.setMaximumSize(QtCore.QSize(500, 140))
        self.class_view_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.class_view_frame.setStyleSheet("*{\n"
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
        self.class_view_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.class_view_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.class_view_frame.setObjectName("class_view_frame")
        self.class_view_cass_name_label = QtWidgets.QLabel(self.class_view_frame)
        self.class_view_cass_name_label.setGeometry(QtCore.QRect(10, 0, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.class_view_cass_name_label.setFont(font)
        self.class_view_cass_name_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.class_view_cass_name_label.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;\n"
"border:0px")
        self.class_view_cass_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.class_view_cass_name_label.setWordWrap(True)
        self.class_view_cass_name_label.setObjectName("class_view_cass_name_label")
        self.class_view_class_des_label = QtWidgets.QLabel(self.class_view_frame)
        self.class_view_class_des_label.setGeometry(QtCore.QRect(10, 50, 481, 81))
        self.class_view_class_des_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.class_view_class_des_label.setStyleSheet("position: absolute;\n"
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
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;\n"
"border:0px;")
        self.class_view_class_des_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.class_view_class_des_label.setWordWrap(True)
        self.class_view_class_des_label.setObjectName("class_view_class_des_label")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Form"))
        self.post_button.setText(_translate("mainwindow", "Text Label"))
        self.label_6.setText(_translate("mainwindow", "Name"))
        self.label_7.setText(_translate("mainwindow", "Time"))
        self.label_8.setText(_translate("mainwindow", "Comment"))
        self.label_9.setText(_translate("mainwindow", "User"))
        self.pushButton.setText(_translate("mainwindow", "Menu"))
        self.sign_up_button.setText(_translate("mainwindow", "Sign Up"))
        self.sign_in_button.setText(_translate("mainwindow", "Already a user? Sign In"))
        self.class_view_cass_name_label.setText(_translate("mainwindow", "Class Name"))
        self.class_view_class_des_label.setText(_translate("mainwindow", "Des"))
import temp_rc
