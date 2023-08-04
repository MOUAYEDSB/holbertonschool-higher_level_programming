#!/usr/bin/python3
'''

this module provide function that add 2 intergers

'''
def add_integer(a, b=98):
	'''
	function that adds 2 integers, a and b must be integers or floats
	'''
	if type(a) not in (int, float):
		raise TypeError("a must be an integer")
	if type(b) not in (int, float):
		raise TypeError("b must be an integer")
	return int(a) + int(b)
