import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense
import datetime

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])


now = datetime.datetime.now()

print "Starting attack 2"
print str(now)

planet = 33759952
targets = [ {'galaxy': 1, 'system': 31, 'position': 4}, 
            {'galaxy': 1, 'system': 31, 'position': 6},
            {'galaxy': 1, 'system': 31, 'position': 7},
            {'galaxy': 1, 'system': 30, 'position': 4},
            {'galaxy': 1, 'system': 30, 'position': 8},
            {'galaxy': 1, 'system': 30, 'position': 9},
            {'galaxy': 1, 'system': 30, 'position': 12},
            {'galaxy': 1, 'system': 29, 'position': 5},
            {'galaxy': 1, 'system': 29, 'position': 7},
            {'galaxy': 1, 'system': 29, 'position': 13},]

speed = Speed['100%']
mission = Missions['Attack']
#2 hours
for target in targets:
    try:
        ogame.send_fleet(planet, [(Ships['SmallCargo'], 50)], speed, target, mission, {})
    except Exception, e:
            print 'Unable to perform target %s: %s: %s' % (target['system'], target['position'], str(e))
            