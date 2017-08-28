#!/usr/bin/python3
import os, sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from pydm import PyDMApplication
from epics import PV

class Positioner(QMainWindow):
    def __init__(self, parent=None):
        super(Positioner, self).__init__(parent)
        self.ui = uic.loadUi('movemotors.ui', baseinstance=self)
        self.show()

        self.motor_pv1 = PV('EX:MOTOR1')
        self.motor_pv2 = PV('EX:MOTOR2')
        self.motor_pv3 = PV('EX:MOTOR3')

        self.ui.lineEdit_posX.textChanged.connect(self.validate_positions)
        self.ui.lineEdit_posY.textChanged.connect(self.validate_positions)
        self.ui.lineEdit_posZ.textChanged.connect(self.validate_positions)
        self.ui.pushButton_move.clicked.connect(self.move_motors)

    def validate_positions(self):
        x = self.lineEdit_posX.text()
        y = self.lineEdit_posY.text()
        z = self.lineEdit_posZ.text()
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            self.ui.pushButton_move.setEnabled(True)
            self.window().statusBar().showMessage("")
        except ValueError:
            self.ui.pushButton_move.setEnabled(False)
            self.window().statusBar().showMessage("Desired position is invalid.")

    def move_motors(self):
        self.window().statusBar().showMessage("")
        x = self.ui.lineEdit_posX.text()
        y = self.lineEdit_posY.text()
        z = self.lineEdit_posZ.text()
        self.motor_pv1.put(x)
        self.motor_pv2.put(y)
        self.motor_pv3.put(z)

if __name__ == '__main__':
    this_file = os.path.realpath(__file__)
    app = PyDMApplication()
    positioner = Positioner()
    sys.exit(app.exec_())