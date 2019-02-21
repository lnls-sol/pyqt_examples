#!/usr/bin/python3
from pydm import Display

class Positioner(Display):
    def __init__(self):
        super(Positioner, self).__init__(ui_filename='movemotors.ui')
 
