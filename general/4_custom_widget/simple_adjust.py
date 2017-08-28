#!/usr/bin/python3
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QFrame, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5 import uic, QtCore

class QSimpleAdjust(QWidget):
	"""docstring for PyDMAdjust"""
	# Emitted when value changes.
	valueChanged = pyqtSignal(str)

	def __init__(self, parent=None):
		super(QSimpleAdjust, self).__init__(parent)
		# Frame
		self.frame = QFrame()
		self.frame.setFrameShape(QFrame.StyledPanel) # Border
		# Button plus
		self.pushButtonPlus = QPushButton(self)
		self.pushButtonPlus.setText('+')
		# Line Edit
		self.lineEdit = QLineEdit(self)
		self.lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
		self.lineEdit.setReadOnly(True)
		# Button minus
		self.pushButtonMinus = QPushButton(self)
		self.pushButtonMinus.setText('-')

		# Frame layout
		self.frame_layout = QVBoxLayout()
		self.frame.setLayout(self.frame_layout)

		self.frame_layout.addWidget(self.pushButtonPlus)
		self.frame_layout.addWidget(self.lineEdit)
		self.frame_layout.addWidget(self.pushButtonMinus)

		# Widget layout
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.layout.addWidget(self.frame)

		'''
		# Previous lines are equivalent to:
		uic.loadUi('simple_adjust.ui', baseinstance=self)
		'''
		
		# Properties
		self._precision = 1
		self._value = 0.1	# Initial value

		self._format_string = "{:.1f}"			# For validating float precision
		self.lineEdit.setText(str(self._value))	# Initial value in lineEdit

		# Connect buttons
		self.pushButtonPlus.clicked.connect(self.sendValueplus)
		self.pushButtonMinus.clicked.connect(self.sendValueminus)

	@pyqtSlot()
	def sendValueplus(self):
		value = self._value
		self.valueChanged.emit(str(value))

	@pyqtSlot()
	def sendValueminus(self):
		value = (-1) * self._value
		self.valueChanged.emit(str(value))

	# Properties getters and setters
	def getPrecision(self):
		return self._precision

	def setPrecision(self, new_prec):
		if self._precision != int(new_prec) and new_prec >= 0:
			self._precision = int(new_prec)
			self._format_string = "{:." +str(self._precision)+ "f}"
      
	precision = pyqtProperty(int, getPrecision, setPrecision)

	def getValue(self):
		return self._value

	def setValue(self, new_value):
		value = float(self._format_string.format(new_value))
		self._value = value
		self.lineEdit.setText(str(value))
      
	value = pyqtProperty(float, getValue, setValue)