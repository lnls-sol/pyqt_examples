#!/usr/bin/python3.4
'''
Simple
'''

MOTOR_STEP = 0.1
MOTOR_SCAN = 0.1
PREC = 2
STRING_FORMAT = '% .'+str(PREC)+'f'

from pcaspy import Driver, SimpleServer

prefix = 'EX:'
pvdb = {
		'CALC' :
			{
			'value': 0.0,
			'scan' : 1,
			'hilim' : 9,
			'hihi' : 8,
			'high' : 7,
			'low'  : 3,
			'lolo' : 1,
			'lolim' : 0,
			},
		'MOTOR1' : 
			{
			'value': 0.0,
			'prec': PREC,
			'hilim' : 180,
			'hihi' : 140,
			'high' : 100,
			'low'  : -100,
			'lolo' : -140,
			'lolim' : -180,
			'unit' : 'deg'
			},
		'MOTOR1.RBV' : 
			{
			'value': 0.0,
			'prec': 2,
			'step': MOTOR_STEP,
			'scan' : MOTOR_SCAN,
			'unit' : 'deg'
			},
		'MOTOR2' : 
			{
			'value': 0.0,
			'prec': PREC,
			'hilim' : 180,
			'hihi' : 140,
			'high' : 100,
			'low'  : -100,
			'lolo' : -140,
			'lolim' : -180,
			'unit' : 'deg'
			},
		'MOTOR2.RBV' : 
			{
			'value': 0.0,
			'prec': 2,
			'step': MOTOR_STEP,
			'scan' : MOTOR_SCAN,
			'unit' : 'deg'	
			},
		'MOTOR3' : 
			{
			'value': 0.0,
			'prec': PREC,
			'hilim' : 180,
			'hihi' : 140,
			'high' : 100,
			'low'  : -100,
			'lolo' : -140,
			'lolim' : -180,
			'unit' : 'deg'
			},
		'MOTOR3.RBV' : 
			{
			'value': 0.0,
			'prec': 2,
			'step': MOTOR_STEP,
			'scan' : MOTOR_SCAN,
			'unit' : 'deg'	
			}
		}


class myDriver(Driver):
	def __init__(self):
		super(myDriver, self).__init__()

	def read(self, reason):
		value = self.getParam(reason)

		if reason == 'CALC':
			if value == 9:
				value = 0
			else:
				value = value + 1
			self.setParam('CALC', value)

		elif reason == 'MOTOR1.RBV':
			value_formatted = float(STRING_FORMAT % value)
			motor_val = self.getParam('MOTOR1')
			if value_formatted < motor_val:
				result = value_formatted + MOTOR_STEP
				value = result
				self.setParam('MOTOR1.RBV', value)
			elif value_formatted > motor_val:
				result = value_formatted - MOTOR_STEP
				value = result
				self.setParam('MOTOR1.RBV', value)

		elif reason == 'MOTOR2.RBV':
			value_formatted = float(STRING_FORMAT % value)
			motor_val = self.getParam('MOTOR2')
			if value_formatted < motor_val:
				result = value_formatted + MOTOR_STEP
				value = result
				self.setParam('MOTOR2.RBV', value)
			elif value_formatted > motor_val:
				result = value_formatted - MOTOR_STEP
				value = result
				self.setParam('MOTOR2.RBV', value)

		elif reason == 'MOTOR3.RBV':
			value_formatted = float(STRING_FORMAT % value)
			motor_val = self.getParam('MOTOR3')
			if value_formatted < motor_val:
				result = value_formatted + MOTOR_STEP
				value = result
				self.setParam('MOTOR3.RBV', value)
			elif value_formatted > motor_val:
				result = value_formatted - MOTOR_STEP
				value = result
				self.setParam('MOTOR3.RBV', value)

		return value
            

if __name__ == '__main__':
	server = SimpleServer()
	server.createPV(prefix, pvdb)
	driver = myDriver()

	# process CA transactions
	print("Server is running... (ctrl+c to close)")
	while True:
		server.process(0.1)
