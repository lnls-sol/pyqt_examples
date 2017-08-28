#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot
 
@pyqtSlot()
def sayHello():
	print('Hello PyQt!')

app = QApplication(sys.argv)		# Create application 
button = QPushButton('Click me!')	# Add button
button.clicked.connect(sayHello)	# Connect its clicked signal to sayHello slot
button.show() 						# Show window with button
sys.exit(app.exec_())				# Run the app! 