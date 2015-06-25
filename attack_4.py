import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])


planet = 33759952
targets = [ {'galaxy': 1, 'system': 25, 'position': 4},
            #{'galaxy': 1, 'system': 25, 'position': 6},
            {'galaxy': 1, 'system': 25, 'position': 10},
            {'galaxy': 1, 'system': 25, 'position': 12},
            {'galaxy': 1, 'system': 24, 'position': 10},
            {'galaxy': 1, 'system': 23, 'position': 4},
            {'galaxy': 1, 'system': 23, 'position': 5},
            {'galaxy': 1, 'system': 23, 'position': 10},
            {'galaxy': 1, 'system': 21, 'position': 3},
            {'galaxy': 1, 'system': 21, 'position': 1},]

speed = Speed['100%']
mission = Missions['Attack']
#1 hours and 5 minutes
for target in targets:
    ogame.send_fleet(planet, [(Ships['SmallCargo'], 50)], speed, target, mission, {})