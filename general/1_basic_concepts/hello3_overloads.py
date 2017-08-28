#!/usr/bin/python3
import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
 
# define a new slot that receives a int or str
@pyqtSlot(str)
@pyqtSlot(int)
def echo(stuff):
	print(stuff)
 
class Person(QObject):
	# This signal can have a str (default) or int argument
	speak = pyqtSignal([str], [int])
 
someone = Person()

# Connect each signal (the nondefaul must be explicited)
someone.speak.connect(echo)
someone.speak[int].connect(echo)

# Emit signals
someone.speak.emit('Hello!')
someone.speak[int].emit(10)