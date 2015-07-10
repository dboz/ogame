import json
from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

with open('/root/ogame/config.json') as data_file:    
	data = json.load(data_file)
    
  
ogame = OGame(data['uni'], data['user'], data['password'], data['server'])

planets = [33759952, 33763525]

for planet in planets:
	ogame.build(planet, (Defense['PlasmaTurret'], 50))
	ogame.build(planet, (Defense['GaussCannon'], 20))
	ogame.build(planet, (Defense['IonCannon'], 20))
	ogame.build(planet, (Defense['HeavyLaser'], 100))
        #ogame.build(planet, (Defense['LightLaser'], 200))
	#ogame.build(planet, (Defense['RocketLauncher'], 1500))
