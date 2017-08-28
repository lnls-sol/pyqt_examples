#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys

app = QApplication(sys.argv)
window = uic.loadUi('hello.ui')
window.show()
sys.exit(app.exec_())