import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)

ogame = OGame(data['uni'], data['user'], data['password'], data['server'])

where = {'galaxy': 1, 'system': 33, 'position': 4}
speed = Speed['100%']
mission = Missions['Transport']

#Move resources from hikol to squre

planet_id = 33763525
current_resources = ogame.get_resources(planet_id)
resources = {'metal': current_resources.get('metal'), 'crystal': current_resources.get('crystal'), 'deuterium': current_resources.get('deuterium')}
ogame.send_fleet(planet_id, [(Ships['LargeCargo'], 500)], speed, where, mission, resources)
		