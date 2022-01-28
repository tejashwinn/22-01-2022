### root copy to create posts 
from create_posts import Ui_create_posts_form
from PyQt5 import QtCore, QtGui, QtWidgets

def show_create_post(self):
    self.create_post_mainwindow = QtWidgets.QMainWindow()
    self.ui_create_post = Ui_create_posts_form()
    self.ui_create_post.setupUi(self.create_post_mainwindow)
    self.create_post_mainwindow.show()

self.actionCreatePost.triggered.connect(lambda: self.show_create_post())


def show_post(self):
    self.post_mainwindow = QtWidgets.QMainWindow()
    self.ui_post = Ui_create_posts_form()
    self.ui_post.setupUi(self.post_mainwindow)
    self.post_mainwindow.show()


