from tempfile import tempdir
from PyQt5 import QtCore, QtGui, QtWidgets
from root_copy import Ui_MainWindow


def sign_up_switch(variable):
    variable.up_outer_frame.show()
    variable.in_outer_frame.hide()
    variable.main_class_frame.hide()


def sign_in_switch(variable):
    variable.in_outer_frame.show()
    variable.up_outer_frame.hide()
    variable.main_class_frame.hide()


def show_main_frame(variable):
    variable.main_class_frame.show()
    variable.up_outer_frame.hide()
    variable.in_outer_frame.hide()
    variable.all_classes_frame.hide()


def posts(variable):
    variable.all_classes_frame.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # switches
    ui.actionSignUp.triggered.connect(lambda: sign_up_switch(ui))
    ui.actionSignIn.triggered.connect(lambda: sign_in_switch(ui))
    ui.actionClasses.triggered.connect(lambda: show_main_frame(ui))

    # button actions
    ui.in_sign_up_button.clicked.connect(lambda: sign_up_switch(ui))
    ui.up_sign_in_button.clicked.connect(lambda: sign_in_switch(ui))

    # default hide actions
    ui.all_classes_frame.hide()

    # actions
    ui.posts_scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarAlwaysOff)
    ui.up_sign_up_button.clicked.connect(ui.sign_up_insert)

    # for i in range(100):
    #     temp = ui.return_post_button(MainWindow, str(i))
    #     ui.verticalLayout.addWidget(temp)

    sign_up_switch(ui)
    MainWindow.show()
    sys.exit(app.exec_())
