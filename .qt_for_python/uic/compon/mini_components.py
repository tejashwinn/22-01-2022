from PyQt5 import QtCore, QtGui, QtWidgets
import json
from compon.post_buttons import Individual_Post_Button
from compon.assignment_buttons import Individual_As_Button
from sql.fetch_posts import Retrieve_Post_Cl
from sql.fetch_assignments import Retrieve_As_Cl


class Individual_Class_Button():

    def create_buttons_post(self):
        def json_data():
            with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
                return json.load(settings_json_file)
        data = json_data()

        def clearLayout(layout):
            if layout is not None:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget() is not None:
                        child.widget().deleteLater()
                    elif child.layout() is not None:
                        clearLayout(child.layout())
        clearLayout(self.ui_te.verticalLayout)

        clearLayout(self.ui_te.verticalLayout_3)
        temp1 = QtWidgets.QLabel()
        temp1.setGeometry(QtCore.QRect(10, 10, 441, 30))
        temp1.setStyleSheet("position: absolute;\n"
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
        temp1.setObjectName("temp1")
        temp1.setText("Posts")
        self.ui_te.verticalLayout.addWidget(temp1)
        
        for i in data["posts_in_class"]:
            temp = Individual_Post_Button(mainwindow=self.mainwindow, di=i)
            self.ui_te.verticalLayout.addWidget(temp.child)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui_te.verticalLayout.addItem(spacerItem)

        for i in data["as_in_class"]:
            # print(i)
            temp = Individual_As_Button(mainwindow=self.mainwindow, di=i)
            self.ui_te.verticalLayout_3.addWidget(temp.child)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui_te.verticalLayout_3.addItem(spacerItem)

    def open_class(self, event):
        self.ui_te.all_classes_frame.hide()
        self.ui_te.class_name_frame.show()
        self.ui_te.posts_scroll_area.show()
        self.ui_te.class_name_label_dynamic.setText(self.name)
        self.ui_te.class_description_label_dynamic.setText(self.description)
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            data["class_selected"] = self.class_code
            data["post_selected"] = ""
        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(data, settings_json_file, indent=4)
        Retrieve_Post_Cl()
        Retrieve_As_Cl()
        self.create_buttons_post()

    def __init__(self, mainwindow, name, description, ui_te, class_code):
        self.mainwindow = mainwindow
        self.name = name
        self.description = description
        self.ui_te = ui_te
        self.class_code = class_code
        self.child = self.return_object()

    def return_object(self):
        self.class_view_frame = QtWidgets.QFrame(self.mainwindow)
        self.class_view_frame.setGeometry(QtCore.QRect(449, 630, 500, 140))
        self.class_view_frame.setMinimumSize(QtCore.QSize(250, 100))
        self.class_view_frame.setMaximumSize(QtCore.QSize(500, 140))
        self.class_view_frame.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.class_view_frame.setObjectName(self.name+"class_view_frame")
        self.class_view_cass_name_label = QtWidgets.QLabel(
            self.class_view_frame)
        self.class_view_cass_name_label.setGeometry(
            QtCore.QRect(10, 0, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.class_view_cass_name_label.setFont(font)
        self.class_view_cass_name_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.class_view_cass_name_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.class_view_cass_name_label.setWordWrap(True)
        self.class_view_cass_name_label.setObjectName(self.name +
                                                      "class_view_cass_name_label")
        self.class_view_class_des_label = QtWidgets.QLabel(
            self.class_view_frame)
        self.class_view_class_des_label.setGeometry(
            QtCore.QRect(10, 50, 481, 81))
        self.class_view_class_des_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.class_view_class_des_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.class_view_class_des_label.setWordWrap(True)
        self.class_view_class_des_label.setObjectName(
            self.name +
            "class_view_class_des_label")

        self.class_view_class_des_label.mousePressEvent = self.open_class
        self.class_view_cass_name_label.mousePressEvent = self.open_class

        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)
        _translate = QtCore.QCoreApplication.translate
        self.class_view_cass_name_label.setText(
            _translate("mainwindow", self.name))
        self.class_view_class_des_label.setText(
            _translate("mainwindow", self.description))

        return self.class_view_frame
