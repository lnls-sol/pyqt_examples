#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QMainWindow
from hello import Ui_Form
import sys

app = QApplication(sys.argv)
window = QMainWindow()
form = Ui_Form()
form.setupUi(window)
window.show()
sys.exit(app.exec_())