#!/usr/bin/python3
from pydm import Display
from epics import PV

class Positioner(Display):
    def __init__(self):
        super(Positioner, self).__init__(ui_filename='movemotors.ui')
        self.motor_pv1 = PV('IOC:m1')
        self.motor_pv2 = PV('IOC:m2')
        self.motor_pv3 = PV('IOC:m3')

        self.lineEdit_posX.textChanged.connect(self.validate_positions)
        self.lineEdit_posY.textChanged.connect(self.validate_positions)
        self.lineEdit_posZ.textChanged.connect(self.validate_positions)
        self.pushButton_move.clicked.connect(self.move_motors)

    def validate_positions(self):
        x = self.lineEdit_posX.text()
        y = self.lineEdit_posY.text()
        z = self.lineEdit_posZ.text()
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            self.pushButton_move.setEnabled(True)
            self.window().statusBar().showMessage("")
        except ValueError:
            self.pushButton_move.setEnabled(False)
            self.window().statusBar().showMessage("Desired position is invalid.")

    def move_motors(self):
        self.window().statusBar().showMessage("")
        x = self.lineEdit_posX.text()
        y = self.lineEdit_posY.text()
        z = self.lineEdit_posZ.text()
        self.motor_pv1.put(x)
        self.motor_pv2.put(y)
        self.motor_pv3.put(z)

