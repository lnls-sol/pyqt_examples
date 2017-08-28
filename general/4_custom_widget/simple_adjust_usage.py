#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget
#from lnls import Ui_Form
from PyQt5 import uic
import sys

Ui_Form, QtBaseClass = uic.loadUiType("simple_adjust_usage.ui")

class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        super(Ui_Form, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())