#!/usr/bin/python3
import os, sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from pydm import PyDMApplication

class Positioner(QMainWindow):
    def __init__(self, parent=None):
        super(Positioner, self).__init__(parent)
        ui = 'movemotors.ui'
        abs_path = os.path.dirname(os.path.realpath(__file__))
        ui_path = os.path.join(abs_path, ui)
        uic.loadUi(ui_path, baseinstance=self)
        self.show()

    def my_method(self):
        pass

if __name__ == '__main__':
    app = PyDMApplication()
    positioner = Positioner()
    sys.exit(app.exec_())