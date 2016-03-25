import random

locations = []

def addLocation(location):
    locations.append(location)
    return

def getLocation(id):
    return [location for location in locations if location.id == id]

def init() :
    l = location('1','home')
    addLocation(l)
    l.addThermostat(thermostat('hall', '100'))
    l.addThermostat(thermostat('living room', '101'))

class location:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.thermostats = []

    def getThermostats(self):
        return self.thermostats

    def getThermostat(self, id):
        return [thermostat for thermostat in self.thermostats if thermostat.id == id]

    def addThermostat(self, therm):
        self.thermostats.append(therm)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'thermostats': [thermostat.serialize() for thermostat in self.thermostats],
        }

class thermostat:
    fanModes = ['auto', 'off']
    modes = ['cool', 'heat', 'off']

    cool = 'cool'
    heat = 'heat'
    off = 'off'
    auto = 'auto'

    highTemp = 100
    lowTemp = 30

    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.currentTemp = 70
        self.mode = self.off # cool, heat, off
        self.coolSetPoint = 20
        self.heatSetPoint = 100
        self.fanMode = self.off # off or auto

    def updateTherm(self, therm):
        err = self.validateData(therm)
        if err:
            return "", err

        name = therm.get('name')
        if name:
            self.name = name
        mode = therm.get('mode')
        if mode:
            self.mode = mode
        coolSetPoint = therm.get('coolSetPoint')
        if coolSetPoint:
            self.coolSetPoint = coolSetPoint
        heatSetPoint = therm.get('heatSetPoint')
        if heatSetPoint:
            self.heatSetPoint = heatSetPoint
        fanMode = therm.get('fanMode')
        if fanMode:
            self.fanMode = fanMode
        return self, ""

    def validateData(self, therm):
        err = self.validateTemperatures(therm)
        if err:
            return err
        if therm.get('fanMode') and therm.get('fanMode') not in self.fanModes:
            return 'unknown fanMode'
        if therm.get('mode') and therm.get('mode') not in self.modes:
            return 'unknown mode'

    def validateTemperatures(self, therm):
        print therm.get('coolSetPoint')
        if therm.get('coolSetPoint') and (therm.get('coolSetPoint') < self.lowTemp or therm.get('coolSetPoint') > self.highTemp):
            return "invalid cool temperature set point"
        if therm.get('heatSetPoint') and (therm.get('heatSetPoint') < self.lowTemp or therm.get('heatSetPoint') > self.highTemp):
            return "invalid heat temperature set point"
        return


    def serialize(self):
        self.currentTemp = random.randint(60,80)
        return {
            'id': self.id,
            'name': self.name,
            'currentTemp': self.currentTemp,
            'mode': self.mode,
            'coolSetPoint': self.coolSetPoint,
            'heatSetPoint': self.heatSetPoint,
            'fanMode': self.fanMode,
        }

init()
