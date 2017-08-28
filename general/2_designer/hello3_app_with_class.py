#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        uic.loadUi('hello.ui', baseinstance=self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())