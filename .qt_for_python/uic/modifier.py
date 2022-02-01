import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from root_copy import Ui_MainWindow
from sql.fetch_classes_sql import Fetch_Classes_Cl
from compon.mini_components import Individual_Class_Button
from sql.fetch_posts import Retrieve_Post_Cl


def json_data():
    with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
        return json.load(settings_json_file)


def sign_up_switch(variable):
    variable.up_outer_frame.show()
    variable.in_outer_frame.hide()
    variable.main_class_frame.hide()
    variable.in_email_entry.setText("")
    variable.in_password_entry.setText("")


def sign_in_switch(variable):

    variable.in_outer_frame.show()
    variable.up_outer_frame.hide()
    variable.main_class_frame.hide()

    variable.up_name_entry.setText("")
    variable.up_username_entry.setText("")
    variable.up_email_entry.setText("")
    variable.up_password_entry.setText("")


def show_main_frame(variable):
    variable.main_class_frame.show()
    variable.all_classes_frame.show()
    variable.up_outer_frame.hide()
    variable.in_outer_frame.hide()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()


def show_posts_scroll_and_class_frame(variable):
    variable.all_classes_frame.hide()
    variable.class_name_frame.show()
    variable.posts_scroll_area.show()


def show_all_classes_frame(variable, te):

    def clearLayout(layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    clearLayout(child.layout())
    clearLayout(variable.verticalLayout_5)

    data = json_data()
    variable.all_classes_frame.show()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()
    temp1 = QtWidgets.QLabel(variable.in_inner_frame)
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
    temp1.setText(te.replace('_', ' ').upper())
    variable.verticalLayout_5.addWidget(temp1)

    for i in data[te]:
        temp = Individual_Class_Button(
            mainwindow=MainWindow, name=i["class_name"], description=i["class_description"], ui_te=ui, class_code=i["class_code"])
        variable.verticalLayout_5.addWidget(temp.child)
    spacerItem = QtWidgets.QSpacerItem(
        20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    variable.verticalLayout_5.addItem(spacerItem)

    Retrieve_Post_Cl()
    variable.all_classes_frame.show()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Fetch_Classes_Cl()

    # switches
    ui.actionSignUp.triggered.connect(lambda: sign_up_switch(ui))
    ui.actionSignIn.triggered.connect(lambda: sign_in_switch(ui))

    ui.actionClasses.triggered.connect(
        lambda: show_all_classes_frame(ui, "classes_joined"))
    ui.actionViewClasses.triggered.connect(
        lambda: show_all_classes_frame(ui, "classes_owned"))

    # button actions
    ui.in_sign_up_button.clicked.connect(lambda: sign_up_switch(ui))
    ui.up_sign_in_button.clicked.connect(lambda: sign_in_switch(ui))

    # actions
    ui.posts_scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarAlwaysOff)
    ui.up_sign_up_button.clicked.connect(ui.sign_up_insert)

    # for i in range(100):
    #     temp = ui.return_post_button(MainWindow, str(i))
    #     ui.verticalLayout.addWidget(temp)
    show_all_classes_frame(ui, "classes_owned")
    MainWindow.show()
    
    sys.exit(app.exec_())
