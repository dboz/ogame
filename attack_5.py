import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])


planet = 33759952
targets = [ {'galaxy': 1, 'system': 18, 'position': 5},
            {'galaxy': 1, 'system': 18, 'position': 6},
            {'galaxy': 1, 'system': 18, 'position': 8},
            {'galaxy': 1, 'system': 17, 'position': 11},
            {'galaxy': 1, 'system': 16, 'position': 5},
            {'galaxy': 1, 'system': 16, 'position': 10},
            {'galaxy': 1, 'system': 16, 'position': 12},
            {'galaxy': 1, 'system': 14, 'position': 9},
            {'galaxy': 1, 'system': 14, 'position': 10},
            {'galaxy': 1, 'system': 14, 'position': 13},]

speed = Speed['100%']
mission = Missions['Attack']
#1 hours and 5 minutes
for target in targets:
    ogame.send_fleet(planet, [(Ships['SmallCargo'], 50)], speed, target, mission, {})