from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sqlite3
from sqlite3 import Error


class Individual_As_Button():
    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def open_file(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(
            self.ui_post.assign_frame, 'Select a File', '', 'All Files (*.*)')
        self.ui_post.dynamic_add_files.setText(
            "File Name: "+self.path[0].split('/')[-1])

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            self.valid = False
            print(e)

    def download_file(self):

        sql = """SELECT as_file from as_cvs where as_code = ?"""
        self.create_connection()
        self.cursor.execute(sql, (self.as_code,))
        rows = self.cursor.fetchall()

        file1 = rows[0][0]
        temp_storage = 'C:/Users/tejas/Desktop/22-01-22/.qt_for_python/uic/temp_file_storage/' + \
            self.as_file_name
        with open(temp_storage, 'wb') as file:
            file.write(file1)
        file = str(QtWidgets.QFileDialog.getExistingDirectory(
            self.ui_post.assign_frame, "Select Directory"))
        import shutil
        file += "/"+self.as_file_name
        src_path = temp_storage
        dst_path = file
        shutil.move(src_path, dst_path)
        # print(src_path, "\n", dst_path)
        self.ui_post.dynamic_files.setText("Downloaded: "+self.as_file_name)

    def open_post(self, event):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            # data["as_selected"] = self.as_code
        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(data, settings_json_file, indent=4)

        from sql.fetch_assignments import Retrieve_As_Cl
        Retrieve_As_Cl()

        # open post
        self.post_mainwindow = QtWidgets.QMainWindow()
        from assignments import Ui_Assignments
        self.ui_post = Ui_Assignments()

        self.ui_post.setupUi(self.post_mainwindow)
        self.ui_post.add_file_button.clicked.connect(self.open_file)
        self.ui_post.dynamic_as_date.setText("Date: " + self.as_date)
        self.ui_post.dynamic_sub_date.setText(
            "Submisson date: " + self.as_sub_date)
        self.ui_post.dynamic_marks.setText(str(self.as_marks))
        self.ui_post.dynamic_des_label.setText(self.as_description)

        if self.as_file_name != '' and self.as_exten != "":
            self.ui_post.dynamic_files.setText("File Name: "+self.as_file_name)
            self.ui_post.download_button.clicked.connect(self.download_file)
            self.ui_post.download_button.setDisabled(False)

        else:
            self.ui_post.dynamic_files.setText("No attachments")
            self.ui_post.download_button.setDisabled(True)

        self.post_mainwindow.show()

    def __init__(self, mainwindow, di):
        from datetime import datetime

        self.mainwindow = mainwindow
        self.as_code = di["as_code"]
        self.as_heading = di["as_heading"]
        self.as_description = di["as_des"]
        self.as_date = di["as_date"].rsplit(":", 1)[0]
        self.as_sub_date = di["as_sub_date"].rsplit(":", 1)[0]
        self.as_marks = str(di["as_marks"])
        self.as_file_name = di["as_file_name"]
        self.as_exten = di["as_exten"]
        self.as_comments = di["as_comments"]

        self.child = self.return_object()
        self.dynamic_name_label.setText(self.as_heading)
        self.dynamic_in_label.setText("Date: "+self.as_date)
        self.dynamic_sub_label.setText("Sub: "+self.as_sub_date)

    def return_object(self):
        self.as_frame = QtWidgets.QFrame(self.mainwindow)
        self.as_frame.setGeometry(QtCore.QRect(730, 40, 248, 120))
        self.as_frame.setMinimumSize(QtCore.QSize(0, 120))
        self.as_frame.setMaximumSize(QtCore.QSize(99999, 120))
        self.as_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.as_frame.setStyleSheet("*{\n"
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
        self.as_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.as_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.as_frame.setObjectName("as_frame")
        self.dynamic_name_label = QtWidgets.QLabel(self.as_frame)
        self.dynamic_name_label.setGeometry(QtCore.QRect(10, 0, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dynamic_name_label.setFont(font)
        self.dynamic_name_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dynamic_name_label.setStyleSheet("position: absolute;\n"
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
                                              "border:0px;\n"
                                              "")
        self.dynamic_name_label.setWordWrap(True)
        self.dynamic_name_label.setObjectName("dynamic_name_label")
        self.dynamic_in_label = QtWidgets.QLabel(self.as_frame)
        self.dynamic_in_label.setGeometry(QtCore.QRect(10, 60, 231, 21))
        self.dynamic_in_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dynamic_in_label.setStyleSheet("position: absolute;\n"
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
        self.dynamic_in_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dynamic_in_label.setObjectName("dynamic_in_label")
        self.dynamic_sub_label = QtWidgets.QLabel(self.as_frame)
        self.dynamic_sub_label.setGeometry(QtCore.QRect(10, 90, 231, 21))
        self.dynamic_sub_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dynamic_sub_label.setStyleSheet("position: absolute;\n"
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
        self.dynamic_sub_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dynamic_sub_label.setObjectName("dynamic_sub_label")

        self.dynamic_in_label.mousePressEvent = self.open_post
        self.dynamic_sub_label.mousePressEvent = self.open_post
        self.dynamic_name_label.mousePressEvent = self.open_post
        self.as_frame.mousePressEvent = self.open_post

        return self.as_frame
