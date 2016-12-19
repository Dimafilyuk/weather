#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import random
class BME280(object):

	def get_data(self):
	     nois=random.randint(0, 10)
		  print nois
		temperature = 10+nois


		# Avoid exception caused by division by zero

		pressure = 100+nois*5

		humidity = 10/nois
		if (humidity > 100.0):
			humidity = 100.0
		else:
			if(humidity < 0.0):
				humidity = 0.0

		return {'t':temperature, 'p':pressure, 'h':humidity}
