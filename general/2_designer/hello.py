# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 107)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(8, 22, 159, 25))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(178, 20, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(308, 62, 106, 27))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_clear = QtWidgets.QPushButton(Form)
        self.pushButton_clear.setGeometry(QtCore.QRect(308, 20, 106, 27))
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.retranslateUi(Form)
        self.pushButton_close.clicked.connect(Form.close)
        self.pushButton_clear.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hello PyQt"))
        self.label.setText(_translate("Form", "Awesome text here:"))
        self.pushButton_close.setText(_translate("Form", "Close"))
        self.pushButton_clear.setText(_translate("Form", "Clear"))

