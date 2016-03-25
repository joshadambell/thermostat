#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response
import location

app = Flask(__name__)

@app.route('/locations', methods=['GET'])
def getLocations():
    return jsonify({'locations': [l.serialize() for l in location.locations]})

@app.route('/locations/<string:location_id>', methods=['GET'])
def getLocation(location_id):
    l = location.getLocation(location_id)
    if len(l) == 0 :
        locationNotFound(location_id)
    return jsonify({'location': l[0].serialize()})

@app.route('/locations/<string:location_id>/thermostats', methods=['GET'])
def getLocationThermostats(location_id):
    l = location.getLocation(location_id)
    if len(l) == 0 :
        locationNotFound(location_id)
    return jsonify({'thermostats': [thermostat.serialize() for thermostat in l[0].getThermostats()]})

@app.route('/locations/<string:location_id>/thermostats/<string:therm_id>', methods=['GET'])
def getThermostat(location_id, therm_id):
    l = location.getLocation(location_id)
    if len(l) == 0 :
        locationNotFound(location_id)
    t = l[0].getThermostat(therm_id)
    if len(t) == 0:
        thermostatNotFound(therm_id, location_id)
    return jsonify({'thermostat': t[0].serialize()})

@app.route('/locations/<string:location_id>/thermostats/<string:therm_id>', methods=['PUT'])
def updateTherm(location_id, therm_id):
    if not request.json:
        abort(400)
    l = location.getLocation(location_id)
    if len(l) == 0 :
        locationNotFound(location_id)
    t = l[0].getThermostat(therm_id)
    if len(t) == 0 :
        thermostatNotFound(therm_id, location_id)
    updatedT, err = t[0].updateTherm(request.json)
    if err:
        badRequest(err)
    return jsonify(updatedT.serialize())

# Error messages

def locationNotFound(location_id) :
    abort(404, "location=[{}] does not exist".format(location_id))

def thermostatNotFound(therm_id, location_id) :
    abort(404, "thermostat=[{}] in location=[{}] does not exist".format(therm_id, location_id))

def badRequest(error):
    abort(400, {'error': error})

if __name__ == '__main__':
    app.run(port=8080)
