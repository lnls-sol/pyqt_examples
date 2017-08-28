#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import sys

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        uic.loadUi('hello.ui', baseinstance=self)
        self.show()
        # Bind button to method
        self.pushButton_action.clicked.connect(self.myAction)

    def myAction(self):
        awesome_text = self.lineEdit.text() # Text form LineEdit
        # Define a message box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Information")
        msg.setText('The awesome text is: ' + awesome_text)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # Show message
        reply = msg.exec_()
        # Get pushed button
        if reply == msg.Ok: print('"Ok" button was pushed.')
        elif reply == msg.Cancel: print('"Cancel" button was pushed.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())