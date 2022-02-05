from xml.etree.ElementTree import tostring
from PyQt5 import QtCore, QtGui, QtWidgets
from compon.insert_assignment import Create_Assignment


class Ui_Assignment_form(object):
    path = ["", ""]

    def open_file(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(
            self.create_assignment_frame, 'Select a File', '', 'All Files (*.*)')
        self.label_file_name.setText(
            "File Name: "+self.path[0].split('/')[-1])

    def create(self):
        self.dt = self.date_time_edit.dateTime()

        if self.path[0] == "":
            temp = Create_Assignment(
                head=self.head_entry.toPlainText(),
                description=self.des_entry.toPlainText(),
                sub_date=self.dt.toString("dd-MM-yyyy hh:mm:ss"),
                marks=self.marks_entry.toPlainText()
            )
            if temp.valid:
                temp.insert()
                self.post_assignment_button.setDisabled(True)
        else:
            temp = Create_Assignment(
                head=self.head_entry.toPlainText(),
                description=self.des_entry.toPlainText(),
                sub_date=self.dt.toString("dd-MM-yyyy hh:mm:ss"),
                marks=self.marks_entry.toPlainText(),
                file_path=self.path[0]
            )
            if temp.valid:
                temp.insert_with_file()
                self.post_assignment_button.setDisabled(True)

        self.warning_label.show()
        self.warning_label.setText(temp.errors)
        if temp.errors == "":
            self.warning_label.setText("Post Posted")

    def setupUi(self, Assignment_form):
        Assignment_form.setObjectName("Assignment_form")
        Assignment_form.resize(567, 641)
        Assignment_form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Assignment_form)
        self.gridLayout.setObjectName("gridLayout")
        self.create_assignment_frame = QtWidgets.QFrame(Assignment_form)
        self.create_assignment_frame.setMinimumSize(QtCore.QSize(541, 607))
        self.create_assignment_frame.setMaximumSize(QtCore.QSize(541, 607))
        self.create_assignment_frame.setStyleSheet("#create_assignment_frame{/* Auto layout */\n"
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
        self.create_assignment_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.create_assignment_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_assignment_frame.setObjectName("create_assignment_frame")
        self.post_heading_posts = QtWidgets.QLabel(
            self.create_assignment_frame)
        self.post_heading_posts.setGeometry(QtCore.QRect(20, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.post_heading_posts.setFont(font)
        self.post_heading_posts.setStyleSheet("position: absolute;\n"
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
        self.post_heading_posts.setObjectName("post_heading_posts")
        self.static_des = QtWidgets.QLabel(self.create_assignment_frame)
        self.static_des.setGeometry(QtCore.QRect(30, 170, 111, 41))
        self.static_des.setStyleSheet("font-family: Poppins;\n"
                                      "font-style: normal;\n"
                                      "font-weight: normal;\n"
                                      "font-size: 15px;\n"
                                      "line-height: 30px;\n"
                                      "/* identical to box height */\n"
                                      "\n"
                                      "letter-spacing: 0.05em;\n"
                                      "text-transform: capitalize;\n"
                                      "")
        self.static_des.setObjectName("static_des")
        self.des_entry = QtWidgets.QPlainTextEdit(self.create_assignment_frame)
        self.des_entry.setGeometry(QtCore.QRect(20, 210, 511, 131))
        self.des_entry.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.des_entry.setPlainText("")
        self.des_entry.setObjectName("des_entry")
        self.head_entry = QtWidgets.QPlainTextEdit(
            self.create_assignment_frame)
        self.head_entry.setGeometry(QtCore.QRect(20, 110, 511, 41))
        self.head_entry.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.head_entry.setPlainText("")
        self.head_entry.setObjectName("head_entry")
        self.head_label = QtWidgets.QLabel(self.create_assignment_frame)
        self.head_label.setGeometry(QtCore.QRect(30, 70, 81, 41))
        self.head_label.setStyleSheet("font-family: Poppins;\n"
                                      "font-style: normal;\n"
                                      "font-weight: normal;\n"
                                      "font-size: 15px;\n"
                                      "line-height: 30px;\n"
                                      "/* identical to box height */\n"
                                      "\n"
                                      "letter-spacing: 0.05em;\n"
                                      "text-transform: capitalize;\n"
                                      "")
        self.head_label.setObjectName("head_label")
        self.label_file_name = QtWidgets.QLabel(self.create_assignment_frame)
        self.label_file_name.setGeometry(QtCore.QRect(20, 430, 511, 41))
        self.label_file_name.setStyleSheet("font-family: Poppins;\n"
                                           "font-style: normal;\n"
                                           "font-weight: normal;\n"
                                           "font-size: 15px;\n"
                                           "line-height: 30px;\n"
                                           "/* identical to box height */\n"
                                           "\n"
                                           "letter-spacing: 0.05em;\n"
                                           "text-transform: capitalize;\n"
                                           "")
        self.label_file_name.setObjectName("label_file_name")
        self.add_files_button = QtWidgets.QPushButton(
            self.create_assignment_frame)
        self.add_files_button.setGeometry(QtCore.QRect(160, 490, 221, 40))
        self.add_files_button.setStyleSheet("\n"
                                            "#add_files_button{\n"
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
                                            "#add_files_button:pressed {\n"
                                            "    border-style: inset;\n"
                                            "    border: 1px solid  #4F4F4F;\n"
                                            "color: #4F4F4F;\n"
                                            "background: #FFFFFF;\n"
                                            "}\n"
                                            "/* Inside auto layout */\n"
                                            "\n"
                                            "")
        self.add_files_button.setObjectName("add_files_button")
        self.date_entry = QtWidgets.QLabel(self.create_assignment_frame)
        self.date_entry.setGeometry(QtCore.QRect(20, 370, 51, 41))
        self.date_entry.setStyleSheet("font-family: Poppins;\n"
                                      "font-style: normal;\n"
                                      "font-weight: normal;\n"
                                      "font-size: 15px;\n"
                                      "line-height: 30px;\n"
                                      "/* identical to box height */\n"
                                      "\n"
                                      "letter-spacing: 0.05em;\n"
                                      "text-transform: capitalize;\n"
                                      "")
        self.date_entry.setWordWrap(True)
        self.date_entry.setObjectName("date_entry")
        self.date_time_edit = QtWidgets.QDateTimeEdit(
            self.create_assignment_frame)
        self.date_time_edit.setGeometry(QtCore.QRect(70, 370, 211, 41))
        self.date_time_edit.setStyleSheet("font-family: Poppins;\n"
                                          "font-style: normal;\n"
                                          "font-weight: normal;\n"
                                          "font-size: 15px;\n"
                                          "line-height: 30px;\n"
                                          "/* identical to box height */\n"
                                          "\n"
                                          "letter-spacing: 0.05em;\n"
                                          "text-transform: capitalize;\n"
                                          "")
        self.date_time_edit.setCalendarPopup(True)
        self.date_time_edit.setObjectName("date_time_edit")
        self.marks_entry = QtWidgets.QPlainTextEdit(
            self.create_assignment_frame)
        self.marks_entry.setGeometry(QtCore.QRect(390, 370, 81, 41))
        self.marks_entry.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.marks_entry.setPlainText("")
        self.marks_entry.setObjectName("marks_entry")
        self.marks_label = QtWidgets.QLabel(self.create_assignment_frame)
        self.marks_label.setGeometry(QtCore.QRect(330, 370, 51, 41))
        self.marks_label.setStyleSheet("font-family: Poppins;\n"
                                       "font-style: normal;\n"
                                       "font-weight: normal;\n"
                                       "font-size: 15px;\n"
                                       "line-height: 30px;\n"
                                       "/* identical to box height */\n"
                                       "\n"
                                       "letter-spacing: 0.05em;\n"
                                       "text-transform: capitalize;\n"
                                       "")
        self.marks_label.setObjectName("marks_label")
        self.post_assignment_button = QtWidgets.QPushButton(
            self.create_assignment_frame)
        self.post_assignment_button.setGeometry(
            QtCore.QRect(160, 550, 221, 40))
        self.post_assignment_button.setStyleSheet("*{\n"
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
        self.post_assignment_button.setObjectName(
            "add_files_button_assignment")
        self.warning_label = QtWidgets.QLabel(self.create_assignment_frame)
        self.warning_label.setGeometry(QtCore.QRect(30, 55, 491, 21))
        self.warning_label.setStyleSheet("position: absolute;\n"
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
        self.warning_label.setObjectName("warning_label")
        self.gridLayout.addWidget(self.create_assignment_frame, 0, 0, 1, 1)

        ###
        self.add_files_button.clicked.connect(self.open_file)
        self.post_assignment_button.clicked.connect(self.create)
        ###
        self.retranslateUi(Assignment_form)
        QtCore.QMetaObject.connectSlotsByName(Assignment_form)

    def retranslateUi(self, Assignment_form):
        _translate = QtCore.QCoreApplication.translate
        Assignment_form.setWindowTitle(_translate("Assignment_form", "Form"))
        self.post_heading_posts.setText(_translate(
            "Assignment_form", "Create Assignment"))
        self.static_des.setText(_translate("Assignment_form", "Description"))
        self.head_label.setText(_translate("Assignment_form", "Heading"))
        self.label_file_name.setText(
            _translate("Assignment_form", "File Name: "))
        self.add_files_button.setText(
            _translate("Assignment_form", "Add Files"))
        self.date_entry.setText(_translate("Assignment_form", "Date"))
        self.marks_label.setText(_translate("Assignment_form", "Marks:"))
        self.post_assignment_button.setText(
            _translate("Assignment_form", "Post Assignment"))
        self.warning_label.setText(_translate("Assignment_form", ""))

        self.date_time_edit.setDateTime(QtCore.QDateTime.currentDateTime())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_posts_form = QtWidgets.QWidget()
    ui = Ui_Assignment_form()
    ui.setupUi(create_posts_form)
    create_posts_form.show()
    sys.exit(app.exec_())
