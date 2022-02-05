from PyQt5 import QtCore, QtGui, QtWidgets
from sql.insert_post import Create_Post


class Ui_create_posts_form(object):

    path = ["", ""]
    # def sync_t(self):
        #     from compon.post_buttons import Individual_Post_Button
        #     from PyQt5 import QtWidgets
        #     import json

        #     def json_data():
        #         with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
        #             return json.load(settings_json_file)

        #     def clearLayout(layout):
        #         if layout is not None:
        #             while layout.count():
        #                 child = layout.takeAt(0)
        #                 if child.widget() is not None:
        #                     child.widget().deleteLater()
        #                 elif child.layout() is not None:
        #                     clearLayout(child.layout())

        #     clearLayout(self.mw.verticalLayout)
        #     data = json_data()

        #     for i in data["posts_in_class"]:
        #         temp = Individual_Post_Button(mainwindow=self.mw, di=i)
        #         self.mw.verticalLayout.addWidget(temp.child)
        #     spacerItem = QtWidgets.QSpacerItem(
        #         20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #     self.mw.verticalLayout.addItem(spacerItem)

    def open_file(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(
            self.create_posts_frame, 'Select a File', '', 'All Files (*.*)')
        self.dynamic_file_name.setText(
            "File Name: "+self.path[0].split('/')[-1])

    def create(self):
        # print(self.path)
        if self.path[0] == "":
            temp = Create_Post(name=self.create_post_name_entry.toPlainText(
            ), description=self.create_post_des_entry.toPlainText())
            if temp.valid:
                temp.insert()
                self.create_post_button.setDisabled(True)

        else:
            temp = Create_Post(name=self.create_post_name_entry.toPlainText(
            ), description=self.create_post_des_entry.toPlainText(), file_path=self.path[0])
            if temp.valid:
                temp.insert_with_file()
                self.create_post_button.setDisabled(True)


        self.dynamic_create_post_warning_label.show()
        self.dynamic_create_post_warning_label.setText(temp.errors)
        if temp.errors == "":
            self.dynamic_create_post_warning_label.setText("Post Posted")

    def setupUi(self, create_posts_form):
        self.mw = None
        self.path = ["", ""]
        # self.t=create_posts_form
        create_posts_form.setObjectName("create_posts_form")
        create_posts_form.resize(563, 553)
        create_posts_form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(create_posts_form)
        self.gridLayout.setObjectName("gridLayout")
        self.create_posts_frame = QtWidgets.QFrame(create_posts_form)
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
            QtCore.QRect(20, 20, 181, 31))
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
        self.create_post_des_entry = QtWidgets.QPlainTextEdit(
            self.create_posts_frame)
        self.create_post_des_entry.setGeometry(QtCore.QRect(20, 210, 511, 131))
        self.create_post_des_entry.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.create_post_des_entry.setPlainText("")
        self.create_post_des_entry.setObjectName("plainTextEdit")
        self.create_post_name_entry = QtWidgets.QPlainTextEdit(
            self.create_posts_frame)
        self.create_post_name_entry.setGeometry(QtCore.QRect(20, 110, 511, 41))
        self.create_post_name_entry.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.create_post_name_entry.setPlainText("")
        self.create_post_name_entry.setObjectName("plainTextEdit_2")
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
        self.add_files_button_posts.clicked.connect(self.open_file)
        self.create_post_button.clicked.connect(self.create)
        self.dynamic_create_post_warning_label = QtWidgets.QLabel(
            self.create_posts_frame)
        self.dynamic_create_post_warning_label.setGeometry(
            QtCore.QRect(30, 50, 481, 31))
        self.dynamic_create_post_warning_label.setStyleSheet("font-family: Poppins;\n"
                                                             "font-style: normal;\n"
                                                             "font-weight: normal;\n"
                                                             "font-size: 15px;\n"
                                                             "line-height: 30px;\n"
                                                             "/* identical to box height */\n"
                                                             "\n"
                                                             "letter-spacing: 0.05em;\n"
                                                             "text-transform: capitalize;\n"
                                                             "color:red;")
        self.dynamic_create_post_warning_label.setObjectName(
            "dynamic_create_post_warning_label")

        self.retranslateUi(create_posts_form)
        QtCore.QMetaObject.connectSlotsByName(create_posts_form)

    def retranslateUi(self, create_posts_form):
        _translate = QtCore.QCoreApplication.translate
        create_posts_form.setWindowTitle(
            _translate("create_posts_form", "Form"))
        self.static_post_heading_posts.setText(
            _translate("create_posts_form", "Create Post"))
        self.static_description_label_create_post_label.setText(
            _translate("create_posts_form", "Description"))
        self.static_create_post_heading_label.setText(
            _translate("create_posts_form", "Heading"))
        self.dynamic_file_name.setText(
            _translate("create_posts_form", "File Name: "))
        self.add_files_button_posts.setText(
            _translate("create_posts_form", "Add Files"))
        self.create_post_button.setText(
            _translate("create_posts_form", "Create Post"))
        self.dynamic_create_post_warning_label.setText(
            _translate("create_posts_form", "Enter the details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_posts_form = QtWidgets.QWidget()
    ui = Ui_create_posts_form()
    ui.setupUi(create_posts_form)
    create_posts_form.show()
    sys.exit(app.exec_())
