import Simulation as Sim

filename = 'dane/TUCAN.csv'
reg = r'sat[0-9]*'
red = ['#version', 'serial', 'flight', 'call']

TeleMega = Sim.Simulation('TeleMega', filename, red, reg, 'COM3')

TeleMega.data_filter()
TeleMega.show_data()
TeleMega.simulate()
