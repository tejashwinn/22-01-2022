from PyQt5 import QtCore, QtGui, QtWidgets
from pip import main
from root_copy import Ui_MainWindow

def sign_up_switch(variable):
    variable.up_outer_frame.show()
    variable.in_outer_frame.hide()

def sign_in_switch(variable):
    variable.in_outer_frame.show()
    variable.up_outer_frame.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.actionSignUp.triggered.connect(lambda: sign_up_switch(ui))
    ui.actionSignIn.triggered.connect(lambda: sign_in_switch(ui))
    
    MainWindow.show()
    sys.exit(app.exec_())
