import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])


planet = 33759952
targets = [ {'galaxy': 1, 'system': 7, 'position': 4},
            {'galaxy': 1, 'system': 7, 'position': 5},
            {'galaxy': 1, 'system': 7, 'position': 8},
            {'galaxy': 1, 'system': 6, 'position': 7},
            {'galaxy': 1, 'system': 5, 'position': 10},
            {'galaxy': 1, 'system': 4, 'position': 12},
            {'galaxy': 1, 'system': 3, 'position': 11},
            {'galaxy': 1, 'system': 3, 'position': 12},
            {'galaxy': 1, 'system': 2, 'position': 4},
            {'galaxy': 1, 'system': 8, 'position': 6},]

speed = Speed['100%']
mission = Missions['Attack']
#
for target in targets:
    ogame.send_fleet(planet, [(Ships['SmallCargo'], 50)], speed, target, mission, {})