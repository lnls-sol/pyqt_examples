#!/usr/bin/python3.4
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

FormClass, BaseClass = uic.loadUiType('hello.ui')

class Window(FormClass, BaseClass):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
