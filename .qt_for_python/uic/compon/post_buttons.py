from PyQt5 import QtCore, QtGui, QtWidgets
import json
from compon.posts import Ui_posts_form
import sqlite3
from sqlite3 import Error


class Individual_Post_Button():
    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

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
        sql = """SELECT post_file from posts_cvs where post_code = ?"""
        self.create_connection()
        self.cursor.execute(sql, (self.post_code,))
        rows = self.cursor.fetchall()
        file1 = rows[0][0]
        temp_storage = 'C:/Users/tejas/Desktop/22-01-22/.qt_for_python/uic/temp_file_storage/' + \
            self.post_file_name
        with open(temp_storage, 'wb') as file:
            file.write(file1)
        file = str(QtWidgets.QFileDialog.getExistingDirectory(
            self.ui_post.frame_2, "Select Directory"))
        import shutil
        file += "/"+self.post_file_name
        src_path = temp_storage
        dst_path = file
        shutil.move(src_path, dst_path)
        # print(src_path, "\n", dst_path)
        self.ui_post.label_2.setText("Downloaded: "+self.post_file_name)

    def open_post(self, event):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            data["post_selected"] = self.post_code
        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(data, settings_json_file, indent=4)

        from sql.fetch_posts import Retrieve_Post_Cl
        Retrieve_Post_Cl()

        from sql.fetch_assignments import Retrieve_As_Cl
        Retrieve_As_Cl()

        # open post
        self.post_mainwindow = QtWidgets.QMainWindow()
        self.ui_post = Ui_posts_form()

        self.ui_post.setupUi(self.post_mainwindow)
        self.ui_post.dynamic_time_label.setText(self.post_date)
        self.ui_post.dynamic_posts_heading_label.setText(self.post_heading)
        self.ui_post.dynamic_posts_description_label.setText(
            self.post_description)

        if self.post_file_name != '' and self.post_file_exten != "":
            self.ui_post.label_2.setText("File Name: "+self.post_file_name)
            self.ui_post.button_file_download.clicked.connect(
                self.download_file)
        else:
            self.ui_post.label_2.setText("No attachments")
            self.ui_post.button_file_download.setDisabled(True)
        self.post_mainwindow.show()

        # def json_data():
        #     with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
        #         return json.load(settings_json_file)

        # data = json_data()
        # from compon.add_insert_comment import Comments
        # self.te1 = Comments(user=str(data["log"]["username"]),
        #                     post=data["post_selected"], comment=self.ui_post.lineEdit.text())
        # print(self.ui_post.lineEdit.text())
        # self.load_comment()

    def __init__(self, mainwindow, di):

        self.mainwindow = mainwindow
        self.post_code = di["post_code"]
        self.post_heading = di["post_heading"]
        self.post_date = di["post_date"]
        self.post_file_exten = di["post_file_exten"]
        self.post_file_name = di["post_file_name"]
        self.post_description = di["post_description"]
        self.child = self.return_object()

    def return_object(self):
        self.post_single_button = QtWidgets.QFrame(self.mainwindow)
        self.post_single_button.setGeometry(QtCore.QRect(240, 530, 461, 70))
        self.post_single_button.setMinimumSize(QtCore.QSize(0, 70))
        self.post_single_button.setMaximumSize(QtCore.QSize(520, 70))
        self.post_single_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_single_button.setStyleSheet("*{position: absolute;\n"
                                              "width: 370px;\n"
                                              "height: 110px;\n"
                                              "left: 7px;\n"
                                              "top: 28px;\n"
                                              "\n"
                                              "background: rgba(0, 0, 0, 0.05);\n"
                                              "border: 1px solid rgba(0, 0, 0, 0.3);\n"
                                              "box-sizing: border-box;\n"
                                              "border-radius: 10px}")
        self.post_single_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.post_single_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.post_single_button.setObjectName("post_single_button")
        self.post_single_heading = QtWidgets.QLabel(self.post_single_button)
        self.post_single_heading.setGeometry(QtCore.QRect(10, 0, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.post_single_heading.setFont(font)
        self.post_single_heading.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_single_heading.setStyleSheet("position: absolute;\n"
                                               "left: 20px;\n"
                                               "right: 30px;\n"
                                               "top: 10px;\n"
                                               "bottom: 10px;\n"
                                               "\n"
                                               "font-family: Poppins;\n"
                                               "font-style: normal;\n"
                                               "font-weight: normal;\n"
                                               "font-size: 18\n"
                                               "px;\n"
                                               "line-height: 37px;\n"
                                               "letter-spacing: 0.05em;\n"
                                               "background: rgba(0, 0, 0, 0.01);\n"
                                               "color: #000000;\n"
                                               "border:0px;")
        self.post_single_heading.setObjectName("post_single_heading")
        self.post_single_timings = QtWidgets.QLabel(self.post_single_button)
        self.post_single_timings.setGeometry(QtCore.QRect(10, 40, 441, 21))
        self.post_single_timings.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_single_timings.setStyleSheet("position: absolute;\n"
                                               "left: 20px;\n"
                                               "right: 30px;\n"
                                               "top: 10px;\n"
                                               "bottom: 10px;\n"
                                               "\n"
                                               "font-family: Poppins;\n"
                                               "font-style: normal;\n"
                                               "font-weight: normal;\n"
                                               "font-size: 12px;\n"
                                               "line-height: 37px;\n"
                                               "letter-spacing: 0.05em;\n"
                                               "background: rgba(0, 0, 0, 0.01);\n"
                                               "color: #000000;\n"
                                               "border:0px;")
        self.post_single_timings.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.post_single_timings.setObjectName("post_single_timings")
        # QtCore.QMetaObject.connectSlotsByName(mainwindow)
        _translate = QtCore.QCoreApplication.translate

        self.post_single_heading.setText(
            _translate("mainwindow", self.post_heading))
        self.post_single_timings.setText(
            _translate("mainwindow", self.post_date.rsplit(":", 1)[0]))

        self.post_single_heading.mousePressEvent = self.open_post
        self.post_single_timings.mousePressEvent = self.open_post

        return self.post_single_button
