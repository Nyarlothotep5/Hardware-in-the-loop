import re
import time

import pandas as pd
import serial


class Simulation:
	def __init__(self, name: str, filename: str, redundant: list, reg: list, port: str, baudrate: int):
		self.name = name
		self.data = pd.read_csv(filename)
		self.redundant = redundant
		self.reg = reg
		self.baudrate = baudrate
		self.ser = serial.Serial(port)

	def filter_data(self):
		for col in self.data:
			for expr in self.reg:
				if re.search(expr, col) is not None:
					self.redundant.append(col)

		self.data = self.data.drop(columns=self.redundant)

	def show_data(self):
		print(self.data)

	def send_data(self):
		# TODO

		print('')

	def simulate(self):

		for ind in self.data.index:
			timeframe = 0.01
			if self.data['time'][ind] != self.data.last_valid_index():
				timeframe = self.data['time'][ind + 1] - self.data['time'][ind]

			print(self.data.ix[ind])
			print("time: ", self.data['time'][ind])
			self.send_data()
			time.sleep(timeframe)
