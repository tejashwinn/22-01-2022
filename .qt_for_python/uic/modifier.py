from sql.fetch_assignments import Retrieve_As_Cl
import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from root_copy import Ui_MainWindow
from sql.fetch_classes_sql import Fetch_Classes_Cl
from compon.mini_components import Individual_Class_Button
from sql.fetch_posts import Retrieve_Post_Cl
from sql.fetch_classes_sql import Fetch_Classes_Cl
from compon.assignment_buttons import Individual_As_Button
from sql.fetch_events import Retrieve_Events_Cl


def json_data():
    with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
        return json.load(settings_json_file)


def block_log(variable):
    variable.menuViews.setDisabled(True)
    variable.menuClassesMain.setDisabled(True)
    variable.menuClub.setDisabled(True)
    variable.actionRefresh.setDisabled(True)


def sign_up_switch(variable):
    variable.up_outer_frame.show()
    variable.in_outer_frame.hide()
    variable.main_class_frame.hide()

    variable.log_set()
    block_log(variable)


def sign_in_switch(variable):
    variable.in_outer_frame.show()
    variable.up_outer_frame.hide()
    variable.main_class_frame.hide()

    variable.log_set()
    block_log(variable)


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


def log_out(variable):
    import json
    with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\temp.json') as temp_json_file:
        template = json.load(temp_json_file)

    data = template.copy()
    with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
        json.dump(data, settings_json_file, indent=4)

    block_log(variable)

    variable.up_outer_frame.show()
    variable.in_outer_frame.hide()
    variable.main_class_frame.hide()

    variable.log_set()


def show(variable):
    data = json_data()
    if (
        data["log"]["name"] == ''
        or data["log"]["email_id"] == ''
        or not str(data["log"]["username"])
    ):
        sign_up_switch(variable)
        show_all_classes_frame(variable, "classes_owned")

    else:
        show_all_classes_frame(variable, "classes_owned")
        variable.main_class_frame.show()
        variable.all_classes_frame.show()
        variable.class_name_frame.hide()
        variable.posts_scroll_area.hide()


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
    clearLayout(variable.verticalLayout_3)
    clearLayout(variable.verticalLayout_2)

    data = json_data()
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
    from compon.individual_event import Individual_Event_Button

    for i in data["events"]:
        temp = Individual_Event_Button(
            mainwindow=MainWindow, name=i["ev_heading"], description=i["ev_description"], ui_te=ui, date=i["ev_date"])
        variable.verticalLayout_2.addWidget(temp.child)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    variable.verticalLayout_2   .addItem(spacerItem)
    Retrieve_Post_Cl()
    Retrieve_As_Cl()

    variable.all_classes_frame.show()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()


def view_assignment(variable):
    from sql.fetch_assignments import Retrieve_As_Cl
    Retrieve_As_Cl()

    def clearLayout(layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    clearLayout(child.layout())
    clearLayout(variable.verticalLayout_3)
    clearLayout(variable.verticalLayout)
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
    temp1.setText("Assignments")
    variable.verticalLayout.addWidget(temp1)

    data = json_data()
    for i in data["as_in_class"]:
        # print(i)
        temp = Individual_As_Button(mainwindow=variable, di=i)
        variable.verticalLayout.addWidget(temp.child)

        temp.dynamic_in_label.mousePressEvent = temp.open_assignment
        temp.dynamic_sub_label.mousePressEvent = temp.open_assignment
        temp.dynamic_name_label.mousePressEvent = temp.open_assignment
        temp.as_frame.mousePressEvent = temp.open_assignment


def restart(variable):
    Fetch_Classes_Cl()
    # Retrieve_Post_Cl()
    Retrieve_Events_Cl()
    show_all_classes_frame(variable, "classes_joined")
    show_all_classes_frame(variable, "classes_owned")

    data = json_data()
    data["class_selected"] = ""
    data["post_selected"] = ""
    data["as_selected"] = ""

    with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
        json.dump(data, settings_json_file, indent=4)

    variable.main_class_frame.show()
    variable.all_classes_frame.show()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()


if __name__ == "__main__":

    # clears previous posts and class selected
    data = json_data()
    data["class_selected"] = ""
    data["post_selected"] = ""
    data["as_selected"] = ""

    with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
        json.dump(data, settings_json_file, indent=4)

    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Fetch_Classes_Cl()
    Retrieve_Events_Cl


    # switches
    ui.actionSignUp.triggered.connect(lambda: sign_up_switch(ui))
    ui.actionSignIn.triggered.connect(lambda: sign_in_switch(ui))
    ui.actionLogOut.triggered.connect(lambda: log_out(ui))
    ui.actionViewAssignment.triggered.connect(
        lambda: view_assignment(ui))
    ui.actionClasses.triggered.connect(
        lambda: show_all_classes_frame(ui, "classes_joined"))
    ui.actionViewClasses.triggered.connect(
        lambda: show_all_classes_frame(ui, "classes_owned"))
    # ui.actionClubEvents.triggered.connect(lambda: add_events(ui))
    # button actions
    ui.actionRefresh.triggered.connect(lambda: restart(ui))
    ui.in_sign_up_button.clicked.connect(lambda: sign_up_switch(ui))
    ui.up_sign_in_button.clicked.connect(lambda: sign_in_switch(ui))

    # actions
    ui.posts_scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarAlwaysOff)
    ui.up_sign_up_button.clicked.connect(ui.sign_up_insert)

    show(ui)

    MainWindow.show()

    sys.exit(app.exec_())
