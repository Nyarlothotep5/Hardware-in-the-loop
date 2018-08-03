import re
import time

import pandas as pd
import pyfirmata as pf


class Simulation:
	def __init__(self, name: str, filename: str, redundant: list, reg: str, ard_port: str):
		self.name = name
		self.data = pd.read_csv(filename)
		self.redundant = redundant
		self.reg = reg
		self.port = ard_port

	def data_filter(self):
		for col in self.data:
			if re.match(self.reg, col) is not None:
				self.redundant.append(col)

		self.data = self.data.drop(columns=self.redundant)

	def show_data(self):
		print(self.data)

	# def send_data(self, brd: Arduino, dt_ind: int):
	# sending signal

	def simulate(self):
		board = pf.Arduino(self.port)

		for ind in self.data.index:
			timeframe = 0.01
			if self.data['time'][ind] != self.data.last_valid_index():
				timeframe = self.data['time'][ind + 1] - self.data['time'][ind]

			print(self.data.ix[ind])
			print("time: ", self.data['time'][ind])
			self.send_data(board, ind)
			time.sleep(timeframe)
