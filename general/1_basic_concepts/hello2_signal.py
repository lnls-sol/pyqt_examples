#!/usr/bin/python3
import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

@pyqtSlot(str)
def echo(words):
	print(words)
 
class Person(QObject):
	speak = pyqtSignal(str)		# Create a signal with string argument
 
someone = Person()
someone.speak.connect(echo)		# Connect signal to slot
someone.speak.emit("Hello!")	# Emit signal