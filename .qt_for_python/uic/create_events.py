from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_create_event(object):

    def setupUi(self, create_event):
        create_event.setObjectName("create_event")
        create_event.resize(563, 553)
        create_event.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(create_event)
        self.gridLayout.setObjectName("gridLayout")
        self.create_posts_frame = QtWidgets.QFrame(create_event)
        self.create_posts_frame.setMinimumSize(QtCore.QSize(541, 531))
        self.create_posts_frame.setMaximumSize(QtCore.QSize(541, 531))
        self.create_posts_frame.setStyleSheet("#create_posts_frame{/* Auto layout */\n"
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
        self.create_posts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_posts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_posts_frame.setObjectName("create_posts_frame")
        self.static_post_heading_posts = QtWidgets.QLabel(
            self.create_posts_frame)
        self.static_post_heading_posts.setGeometry(
            QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.static_post_heading_posts.setFont(font)
        self.static_post_heading_posts.setStyleSheet("position: absolute;\n"
                                                     "width: 233px;\n"
                                                     "height: 60px;\n"
                                                     "left: 92px;\n"
                                                     "top: 48px;\n"
                                                     "\n"
                                                     "font-family: Poppins;\n"
                                                     "font-style: normal;\n"
                                                     "font-weight: normal;\n"
                                                     "font-size: 30px;\n"
                                                     "line-height: 60px;\n"
                                                     "/* identical to box height */\n"
                                                     "\n"
                                                     "letter-spacing: 0.05em;\n"
                                                     "text-decoration-line: underline;\n"
                                                     "text-transform: capitalize;\n"
                                                     "\n"
                                                     "color: #000000;\n"
                                                     "")
        self.static_post_heading_posts.setObjectName(
            "static_post_heading_posts")
        self.static_description_label_create_post_label = QtWidgets.QLabel(
            self.create_posts_frame)
        self.static_description_label_create_post_label.setGeometry(
            QtCore.QRect(30, 170, 111, 41))
        self.static_description_label_create_post_label.setStyleSheet("font-family: Poppins;\n"
                                                                      "font-style: normal;\n"
                                                                      "font-weight: normal;\n"
                                                                      "font-size: 15px;\n"
                                                                      "line-height: 30px;\n"
                                                                      "/* identical to box height */\n"
                                                                      "\n"
                                                                      "letter-spacing: 0.05em;\n"
                                                                      "text-transform: capitalize;\n"
                                                                      "")
        self.static_description_label_create_post_label.setObjectName(
            "static_description_label_create_post_label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.create_posts_frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 210, 511, 131))
        self.plainTextEdit.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(
            self.create_posts_frame)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 110, 511, 41))
        self.plainTextEdit_2.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.static_create_post_heading_label = QtWidgets.QLabel(
            self.create_posts_frame)
        self.static_create_post_heading_label.setGeometry(
            QtCore.QRect(30, 70, 81, 41))
        self.static_create_post_heading_label.setStyleSheet("font-family: Poppins;\n"
                                                            "font-style: normal;\n"
                                                            "font-weight: normal;\n"
                                                            "font-size: 15px;\n"
                                                            "line-height: 30px;\n"
                                                            "/* identical to box height */\n"
                                                            "\n"
                                                            "letter-spacing: 0.05em;\n"
                                                            "text-transform: capitalize;\n"
                                                            "")
        self.static_create_post_heading_label.setObjectName(
            "static_create_post_heading_label")
        self.dynamic_file_name = QtWidgets.QLabel(self.create_posts_frame)
        self.dynamic_file_name.setGeometry(QtCore.QRect(20, 360, 511, 41))
        self.dynamic_file_name.setStyleSheet("font-family: Poppins;\n"
                                             "font-style: normal;\n"
                                             "font-weight: normal;\n"
                                             "font-size: 15px;\n"
                                             "line-height: 30px;\n"
                                             "/* identical to box height */\n"
                                             "\n"
                                             "letter-spacing: 0.05em;\n"
                                             "text-transform: capitalize;\n"
                                             "")
        self.dynamic_file_name.setObjectName("dynamic_file_name")
        self.add_files_button_posts = QtWidgets.QPushButton(
            self.create_posts_frame)
        self.add_files_button_posts.setGeometry(
            QtCore.QRect(160, 420, 221, 40))
        self.add_files_button_posts.setStyleSheet("\n"
                                                  "*{\n"
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
                                                  ":pressed {\n"
                                                  "    border-style: inset;\n"
                                                  "    border: 1px solid  #4F4F4F;\n"
                                                  "color: #4F4F4F;\n"
                                                  "background: #FFFFFF;\n"
                                                  "}\n"
                                                  "/* Inside auto layout */\n"
                                                  "\n"
                                                  "")
        self.add_files_button_posts.setObjectName("add_files_button_posts")
        self.create_post_button = QtWidgets.QPushButton(
            self.create_posts_frame)
        self.create_post_button.setGeometry(QtCore.QRect(160, 470, 221, 40))
        self.create_post_button.setStyleSheet("\n"
                                              "*{\n"
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
                                              ":pressed {\n"
                                              "    border-style: inset;\n"
                                              "    color: white;\n"
                                              "background: #4F4F4F;\n"
                                              "border-radius: 8px;\n"
                                              "}\n"
                                              "/* Inside auto layout */\n"
                                              "\n"
                                              "")
        self.create_post_button.setObjectName("create_post_button")
        self.gridLayout.addWidget(self.create_posts_frame, 0, 0, 1, 1)

        self.retranslateUi(create_event)
        QtCore.QMetaObject.connectSlotsByName(create_event)

    def retranslateUi(self, create_event):
        _translate = QtCore.QCoreApplication.translate
        create_event.setWindowTitle(_translate("create_event", "Create Event"))
        self.static_post_heading_posts.setText(
            _translate("create_event", "Create Event"))
        self.static_description_label_create_post_label.setText(
            _translate("create_event", "Description"))
        self.static_create_post_heading_label.setText(
            _translate("create_event", "Heading"))
        self.dynamic_file_name.setText(
            _translate("create_event", "File Name: "))
        self.add_files_button_posts.setText(
            _translate("create_event", "Add Files"))
        self.create_post_button.setText(
            _translate("create_event", "Create Post"))
        self.add_files_button_posts.hide()
        self.dynamic_file_name.hide()
