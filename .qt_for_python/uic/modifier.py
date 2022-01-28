from tempfile import tempdir
from PyQt5 import QtCore, QtGui, QtWidgets
from pip import main
from root_copy import Ui_MainWindow
from create_posts import Ui_create_posts_form
from posts import Ui_posts_form


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


def return_post_bu1tton(window, head):
    
    def show_post():
        post_mainwindow = QtWidgets.QMainWindow()
        ui_post = Ui_posts_form()
        ui_post.setupUi(post_mainwindow)
        post_mainwindow.show()
        
    _translate = QtCore.QCoreApplication.translate
    post_button = QtWidgets.QPushButton(window, clicked=show_post)
    post_button.setMaximumSize(QtCore.QSize(505, 80))
    font = QtGui.QFont()
    font.setFamily("Poppins Medium")
    font.setPointSize(14)
    post_button.setFont(font)
    post_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    post_button.setLayoutDirection(QtCore.Qt.LeftToRight)
    post_button.setStyleSheet("position: absolute;\n"
                              "width: 1000px;\n"
                              "height: 148px;\n"
                              "left: calc(50% - 1000px/2 + 2px);\n"
                              "top: calc(50% - 148px/2 + 249px);\n"
                              "\n"
                              "background: #FFFFFF;\n"
                              "border: 2px solid #000000;\n"
                              "box-sizing: border-box;\n"
                              "box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
                              "border-radius: 10px;\n"
                              "")
    post_button.setObjectName(head)
    post_button.setText(_translate("mainwindow", head))

    return post_button


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

    for i in range(100):
        temp = ui.return_post_button(MainWindow, str(i))
        ui.verticalLayout.addWidget(temp)
        ui.posts_scroll_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
    MainWindow.show()
    sys.exit(app.exec_())
