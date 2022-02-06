from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Assignments(object):
    path = ["", ""]

    def check_date(self):
        self.as_sub_date = self.dic["as_sub_date"].rsplit(":", 1)[0]
        self.cur_date = QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")
        if self.as_sub_date < self.cur_date:
            self.add_file_button.setDisabled(True)
            self.submit_button_assignment.setDisabled(True)
            self.label.setText("Submissions are not longer accepted")

    def open_file(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(
            self.assign_frame, 'Select a File', '', 'All Files (*.*)')
        self.dynamic_add_files.setText(
            "File Name: "+self.path[0].split('/')[-1])

    def submit(self):
        print(self.path)
        if self.path[0] == "":
            self.label.setText("No file selected")
        else:
            from sql.submit_assignments import Sub_Assignment
            temp = Sub_Assignment(cur_date=self.cur_date,
                                  file_path=self.path[0], di=self.dic)

            if temp.valid:
                temp.submission()
                self.submit_button_assignment.setDisabled(True)
                self.add_file_button.setDisabled(True)
                self.label.setText("Submitted")
            else:
                if temp.errors == 'Already submitted':
                    self.submit_button_assignment.setDisabled(True)
                    self.add_file_button.setDisabled(True)
                self.label.setText(temp.errors)
        self.label.show()

    def setupUi(self, Assignments, di):
        self.dic = di
        Assignments.setObjectName("Assignments")
        Assignments.resize(563, 522)
        Assignments.setStyleSheet("")
        self.assign_frame = QtWidgets.QFrame(Assignments)
        self.assign_frame.setGeometry(QtCore.QRect(11, 11, 541, 500))
        self.assign_frame.setMinimumSize(QtCore.QSize(541, 500))
        self.assign_frame.setMaximumSize(QtCore.QSize(541, 500))
        self.assign_frame.setStyleSheet("#assign_frame\n"
                                        "{/* Auto layout */\n"
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
        self.assign_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.assign_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.assign_frame.setObjectName("assign_frame")
        self.dynamic_heading_as = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_heading_as.setGeometry(QtCore.QRect(20, 20, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dynamic_heading_as.setFont(font)
        self.dynamic_heading_as.setStyleSheet("position: absolute;\n"
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
        self.dynamic_heading_as.setObjectName("dynamic_heading_as")
        self.dynamic_des_label = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_des_label.setGeometry(QtCore.QRect(20, 130, 511, 131))
        self.dynamic_des_label.setMaximumSize(QtCore.QSize(511, 16777215))
        self.dynamic_des_label.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.dynamic_des_label.setScaledContents(False)
        self.dynamic_des_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dynamic_des_label.setWordWrap(True)
        self.dynamic_des_label.setObjectName("dynamic_des_label")
        self.dynamic_files = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_files.setGeometry(QtCore.QRect(20, 300, 381, 31))
        self.dynamic_files.setStyleSheet("font-family: Poppins;\n"
                                         "font-style: normal;\n"
                                         "font-weight: normal;\n"
                                         "font-size: 15px;\n"
                                         "line-height: 30px;\n"
                                         "/* identical to box height */\n"
                                         "\n"
                                         "letter-spacing: 0.05em;\n"
                                         "text-transform: capitalize;\n"
                                         "")
        self.dynamic_files.setObjectName("dynamic_files")
        self.submit_button_assignment = QtWidgets.QPushButton(
            self.assign_frame)
        self.submit_button_assignment.setGeometry(
            QtCore.QRect(170, 420, 191, 41))
        self.submit_button_assignment.setStyleSheet("*{\n"
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
        self.submit_button_assignment.setObjectName("submit_button_assignment")
        self.dynamic_as_date = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_as_date.setGeometry(QtCore.QRect(20, 60, 501, 16))
        self.dynamic_as_date.setStyleSheet("font-family: Poppins;\n"
                                           "font-style: normal;\n"
                                           "font-weight: normal;\n"
                                           "font-size: 13px;\n"
                                           "line-height: 30px;\n"
                                           "/* identical to box height */\n"
                                           "\n"
                                           "letter-spacing: 0.05em;\n"
                                           "text-transform: capitalize;\n"
                                           "")
        self.dynamic_as_date.setObjectName("dynamic_as_date")
        self.dynamic_sub_date = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_sub_date.setGeometry(QtCore.QRect(20, 90, 351, 20))
        self.dynamic_sub_date.setStyleSheet("font-family: Poppins;\n"
                                            "font-style: normal;\n"
                                            "font-weight: normal;\n"
                                            "font-size: 13px;\n"
                                            "line-height: 30px;\n"
                                            "/* identical to box height */\n"
                                            "\n"
                                            "letter-spacing: 0.05em;\n"
                                            "text-transform: capitalize;\n"
                                            "")
        self.dynamic_sub_date.setObjectName("dynamic_sub_date")
        self.download_button = QtWidgets.QPushButton(self.assign_frame)
        self.download_button.setGeometry(QtCore.QRect(410, 300, 121, 31))
        self.download_button.setStyleSheet("*{\n"
                                           "font-family: Inter;\n"
                                           "font-style: normal;\n"
                                           "font-weight: 500;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 17px;\n"
                                           "align-items: center;\n"
                                           "border-style: inset;\n"
                                           "border: 1px solid  #4F4F4F;\n"
                                           "color: #4F4F4F;\n"
                                           "background: #FFFFFF;\n"
                                           "border-radius:10px;\n"
                                           "}\n"
                                           "\n"
                                           ":pressed {\n"
                                           "border-style: inset;\n"
                                           "color: white;\n"
                                           "background: #4F4F4F;\n"
                                           "border-radius: 8px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.download_button.setObjectName("download_button")
        self.dynamic_add_files = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_add_files.setGeometry(QtCore.QRect(20, 350, 371, 31))
        self.dynamic_add_files.setStyleSheet("font-family: Poppins;\n"
                                             "font-style: normal;\n"
                                             "font-weight: normal;\n"
                                             "font-size: 15px;\n"
                                             "line-height: 30px;\n"
                                             "/* identical to box height */\n"
                                             "\n"
                                             "letter-spacing: 0.05em;\n"
                                             "text-transform: capitalize;\n"
                                             "")
        self.dynamic_add_files.setObjectName("dynamic_add_files")
        self.add_file_button = QtWidgets.QPushButton(self.assign_frame)
        self.add_file_button.setGeometry(QtCore.QRect(410, 350, 121, 31))
        self.add_file_button.setStyleSheet("*{\n"
                                           "font-family: Inter;\n"
                                           "font-style: normal;\n"
                                           "font-weight: 500;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 17px;\n"
                                           "align-items: center;\n"
                                           "border-style: inset;\n"
                                           "border: 1px solid  #4F4F4F;\n"
                                           "color: #4F4F4F;\n"
                                           "background: #FFFFFF;\n"
                                           "border-radius:10px;\n"
                                           "}\n"
                                           "\n"
                                           ":pressed {\n"
                                           "border-style: inset;\n"
                                           "color: white;\n"
                                           "background: #4F4F4F;\n"
                                           "border-radius: 8px;\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.add_file_button.setObjectName("add_file_button")
        self.dynamic_marks = QtWidgets.QLabel(self.assign_frame)
        self.dynamic_marks.setGeometry(QtCore.QRect(380, 90, 141, 20))
        self.dynamic_marks.setStyleSheet("font-family: Poppins;\n"
                                         "font-style: normal;\n"
                                         "font-weight: normal;\n"
                                         "font-size: 13px;\n"
                                         "line-height: 30px;\n"
                                         "/* identical to box height */\n"
                                         "\n"
                                         "letter-spacing: 0.05em;\n"
                                         "text-transform: capitalize;\n"
                                         "")
        self.dynamic_marks.setObjectName("dynamic_marks")
        self.label = QtWidgets.QLabel(self.assign_frame)
        self.label.setGeometry(QtCore.QRect(20, 270, 501, 16))
        self.label.setStyleSheet("position: absolute;\n"
                                 "left: 0%;\n"
                                 "right: 12.33%;\n"
                                 "top: 15%;\n"
                                 "bottom: 14.17%;\n"
                                 "\n"
                                 "font-family: poppins;\n"
                                 "font-style: normal;\n"
                                 "font-weight: normal;\n"
                                 "font-size: 14px;\n"
                                 "line-height: 17px;\n"
                                 "\n"
                                 "/* Dark / Medium */\n"
                                 "\n"
                                 "color: #FF0000;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.add_file_button.clicked.connect(self.open_file)
        self.submit_button_assignment.clicked.connect(self.submit)

        self.retranslateUi(Assignments)
        QtCore.QMetaObject.connectSlotsByName(Assignments)

    def retranslateUi(self, Assignments):
        _translate = QtCore.QCoreApplication.translate
        Assignments.setWindowTitle(_translate("Assignments", "Form"))
        self.dynamic_heading_as.setText(
            _translate("Assignments", "Assignment Heading"))
        self.dynamic_des_label.setText(_translate(
            "Assignments", ""))
        self.dynamic_files.setText(_translate("Assignments", "Files: "))
        self.submit_button_assignment.setText(
            _translate("Assignments", "Submit"))
        self.dynamic_as_date.setText(
            _translate("Assignments", "Assignment Date:"))
        self.dynamic_sub_date.setText(
            _translate("Assignments", "Submisson Date:"))
        self.download_button.setText(
            _translate("Assignments", "Download File"))
        self.dynamic_add_files.setText(_translate("Assignments", "Add Files"))
        self.add_file_button.setText(_translate("Assignments", "Add file"))
        self.dynamic_marks.setText(_translate("Assignments", "Max Marks:"))
        self.check_date()
