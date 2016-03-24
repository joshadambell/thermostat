# Endpoints

## Location

### GET /locations - Get all locations
response - application/json
```
{
  "locations": [
    {
      "id": "1",
      "name": "home",
      "thermostats": [
        {
          "heatSetPoint": 100,
          "fanMode": "off",
          "name": "hall",
          "coolSetPoint": 20,
          "mode": "off",
          "currentTemp": 70,
          "id": "100"
        },
        {
          "heatSetPoint": 100,
          "fanMode": "off",
          "name": "living room",
          "coolSetPoint": 20,
          "mode": "off",
          "currentTemp": 70,
          "id": "101"
        }
      ]
    }
  ]
}
```

### GET /locations/{location_id} - Get a location by id
response - application/json
```
{
  "location": {
    "id": "1",
    "name": "home",
    "thermostats": [
      {
        "heatSetPoint": 100,
        "fanMode": "off",
        "name": "hall",
        "coolSetPoint": 20,
        "mode": "off",
        "currentTemp": 70,
        "id": "100"
      },
      {
        "heatSetPoint": 100,
        "fanMode": "off",
        "name": "living room",
        "coolSetPoint": 20,
        "mode": "off",
        "currentTemp": 70,
        "id": "101"
      }
    ]
  }
}
```

### GET /locations/{location_id}/thermostats - Get all thermostats for a specific location
response - application/json
```
{
  "thermostats": [
    {
      "heatSetPoint": 100,
      "fanMode": "off",
      "name": "hall",
      "coolSetPoint": 20,
      "mode": "off",
      "currentTemp": 70,
      "id": "100"
    },
    {
      "heatSetPoint": 100,
      "fanMode": "off",
      "name": "living room",
      "coolSetPoint": 20,
      "mode": "off",
      "currentTemp": 70,
      "id": "101"
    }
  ]
}
```

### GET /locations/{location_id}/thermostats/{thermostat_id} - Get a thermostat by id for a location
response - application/json
```
{
  "thermostat": {
    "heatSetPoint": 100,
    "fanMode": "off",
    "name": "hall",
    "coolSetPoint": 20,
    "mode": "off",
    "currentTemp": 70,
    "id": "100"
  }
}
```

### PUT /locations/{location_id}/thermostats/{thermostat_id} - Change settings on a thermostat
body - application/json
```
{
  "thermostat": {
    "heatSetPoint": 100,
    "fanMode": "off",
    "name": "hall",
    "coolSetPoint": 20,
    "mode": "off"
  }
}
```
response - application/json
```
{
  "thermostat": {
    "heatSetPoint": 100,
    "fanMode": "off",
    "name": "hall",
    "coolSetPoint": 20,
    "mode": "off"
  }
}
```
