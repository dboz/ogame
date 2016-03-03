import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])


planet = 33759952
targets = [ {'galaxy': 1, 'system': 35, 'position': 9},
            {'galaxy': 1, 'system': 36, 'position': 5},
            {'galaxy': 1, 'system': 36, 'position': 6},
            {'galaxy': 1, 'system': 36, 'position': 8},
            #{'galaxy': 1, 'system': 36, 'position': 9},
            {'galaxy': 1, 'system': 38, 'position': 5},
            {'galaxy': 1, 'system': 39, 'position': 5},
            {'galaxy': 1, 'system': 39, 'position': 11},
            {'galaxy': 1, 'system': 40, 'position': 11},
            {'galaxy': 1, 'system': 40, 'position': 12},]

speed = Speed['100%']
mission = Missions['Attack']
#
for target in targets:
    ogame.send_fleet(planet, [(Ships['SmallCargo'], 100)], speed, target, mission, {})