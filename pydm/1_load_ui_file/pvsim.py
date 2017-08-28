#!/usr/bin/python3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from pydm import PyDMApplication

app = PyDMApplication()
window = uic.loadUi('pvsim.ui', baseinstance=QMainWindow())
window.show()
sys.exit(app.exec_())
