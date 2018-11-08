import Simulation as Sim

filename = 'data/TUCAN.csv'
reg = [r'sat[0-9]*']
red = ['#version', 'serial', 'flight', 'call', 'lqi', 'state', 'state_name', 'rssi', 'drogue_voltage', 'main_voltage',
       'battery_voltage', 'year', 'month', 'day', 'hour', 'minute', 'second', 'connected', 'locked']

sensors = Sim.Simulation('TeleMega', filename, red, reg, 'COM3', 115200)

sensors.filter_data()
sensors.show_data()
sensors.simulate()