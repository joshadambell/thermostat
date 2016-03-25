import web, json
import location

urls = (
    '/locations/(.*)/thermostats/(.*)', 'apiLocationThermostat',
    '/locations/(.*)/thermostats', 'apiLocationThermostats',
    '/locations/(.*)', 'apiLocation',
    '/locations', 'apiLocations',
)
app = web.application(urls, globals())

class apiLocations:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps({'locations': [l.serialize() for l in location.locations]})

class apiLocation:
    def GET(self, location_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return locationNotFound(location_id)
        web.header('Content-Type', 'application/json')
        return json.dumps({'location': l[0].serialize()})

class apiLocationThermostats:
    def GET(self,location_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return locationNotFound(location_id)
        web.header('Content-Type', 'application/json')
        return json.dumps({'thermostats': [thermostat.serialize() for thermostat in l[0].getThermostats()]})

class apiLocationThermostat:
    def GET(self,location_id, therm_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return locationNotFound(location_id)
        t = l[0].getThermostat(therm_id)
        if len(t) == 0:
            return thermostatNotFound(location_id)
        web.header('Content-Type', 'application/json')
        return json.dumps({'thermostat': t[0].serialize()})

    def PUT(self, location_id, therm_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return locationNotFound(location_id)
        t = l[0].getThermostat(therm_id)
        if len(t) == 0:
            return thermostatNotFound(location_id)
        updatedT, err = t[0].updateTherm(json.loads(web.data()))
        if err:
            raise web.badrequest(message=err)
        web.header('Content-Type', 'application/json')
        return json.dumps(updatedT.serialize())


# Error messages
def locationNotFound(location_id) :
    raise web.notfound("location=[{}] does not exist".format(location_id))

def thermostatNotFound(therm_id, location_id) :
    raise web.notfound("thermostat=[{}] in location=[{}] does not exist".format(therm_id, location_id))

if __name__ == "__main__":
    app.run()
