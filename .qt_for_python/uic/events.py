from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_events_form(object):
    def setupUi(self, posts_form):
        posts_form.setObjectName("posts_form")
        posts_form.resize(563, 313)
        posts_form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(posts_form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(posts_form)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 541, 251))
        self.frame_2.setMinimumSize(QtCore.QSize(541, 251))
        self.frame_2.setMaximumSize(QtCore.QSize(541, 251))
        self.frame_2.setStyleSheet("#frame_2{/* Auto layout */\n"
                                   "\n"
                                   "display: flex;\n"
                                   "flex-direction: column;\n"
                                   "align-items: flex-start;\n"
                                   "padding: 40px 25px;\n"
                                   "\n"
                                   "position: absolute;\n"
                                   "width: 593px;\n"
                                   "height: 594px;\n"
                                   "left: calc(50% - 593px/2 - 0.5px);\n"
                                   "top: 243px;\n"
                                   "\n"
                                   "/* White */\n"
                                   "\n"
                                   "background: #FFFFFF;\n"
                                   "/* Grey / Dark */\n"
                                   "\n"
                                   "border: 1px solid #D1D1D1;\n"
                                   "box-sizing: border-box;\n"
                                   "border-radius: 8px;}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("position: absolute;\n"
                                   "width: 233px;\n"
                                   "height: 60px;\n"
                                   "left: 92px;\n"
                                   "top: 48px;\n"
                                   "\n"
                                   "font-family: Poppins;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 25px;\n"
                                   "line-height: 60px;\n"
                                   "/* identical to box height */\n"
                                   "\n"
                                   "letter-spacing: 0.05em;\n"
                                   "text-decoration-line: underline;\n"
                                   "text-transform: capitalize;\n"
                                   "\n"
                                   "color: #000000;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 70, 511, 131))
        self.label.setMaximumSize(QtCore.QSize(511, 16777215))
        self.label.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
                                 "font-family: Poppins;\n"
                                 "font-style: normal;\n"
                                 "font-weight: normal;\n"
                                 "font-size: 15px;\n"
                                 "line-height: 30px;\n"
                                 "/* identical to box height */\n"
                                 "\n"
                                 "letter-spacing: 0.05em;\n"
                                 "text-transform: capitalize;\n"
                                 "\n"
                                 "color: #000000;")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.label_3.setStyleSheet("font-family: Poppins;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 13px;\n"
                                   "line-height: 30px;\n"
                                   "/* identical to box height */\n"
                                   "\n"
                                   "letter-spacing: 0.05em;\n"
                                   "text-transform: capitalize;\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.retranslateUi(posts_form)
        QtCore.QMetaObject.connectSlotsByName(posts_form)

    def retranslateUi(self, posts_form):
        _translate = QtCore.QCoreApplication.translate
        posts_form.setWindowTitle(_translate("posts_form", "Form"))
        self.label_2.setText(_translate("posts_form", "Post Heading"))
        self.label.setText(_translate("posts_form", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec."))
        self.label_3.setText(_translate("posts_form", "Time"))
