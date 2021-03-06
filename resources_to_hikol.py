import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])


planets = [33763767, 33771927, 33777076]
where = {'galaxy': 2, 'system': 333, 'position': 8} #to hikol
speed = Speed['100%']
mission = Missions['Transport']

for planet_id in planets:
	current_resources = ogame.get_resources(planet_id)
	ships = ogame.get_ships(planet_id)
	if ships.get('LargeCargo') > 0:
		resources = {'metal': current_resources.get('metal'), 'crystal': current_resources.get('crystal'), 'deuterium': current_resources.get('deuterium')}
		ogame.send_fleet(planet_id, [(Ships['LargeCargo'], ships.get('LargeCargo'))], speed, where, mission, resources)

		