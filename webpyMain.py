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
        return json.dumps({'locations': [l.serialize() for l in location.locations]})

class apiLocation:
    def GET(self, location_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return web.notfound(self)
        return json.dumps({'location': l[0].serialize()})

class apiLocationThermostats:
    def GET(self,location_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return web.notfound(self)
        return json.dumps({'thermostats': [thermostat.serialize() for thermostat in l[0].getThermostats()]})

class apiLocationThermostat:
    def GET(self,location_id, therm_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return web.notfound(self)
        t = l[0].getThermostat(therm_id)
        if len(t) == 0:
            return web.notfound(self)
        return json.dumps({'thermostat': t[0].serialize()})

    def PUT(self, location_id, therm_id):
        l = location.getLocation(location_id)
        if len(l) == 0:
            return web.notfound(self)
        t = l[0].getThermostat(therm_id)
        if len(t) == 0:
            return web.notfound(self)
        updatedT, err = t[0].updateTherm(json.loads(web.data()))
        if err:
            return web.BadRequest(message=err)
        web.header('Content-Type', 'application/json')
        return json.dumps({'thermostat': updatedT.serialize()})

if __name__ == "__main__":
    app.run()
