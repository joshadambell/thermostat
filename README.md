# Endpoints

### GET /locations - Get all locations
##### responses
- 404 Not Found
- 200 OK - application/json

  ```
  {
    "locations": [
      {
        "id": "1",
        "name": "home",
        "thermostats": [
          {
            "coolSetPoint": 20,
            "currentTemp": 68,
            "fanMode": "off",
            "heatSetPoint": 100,
            "id": "100",
            "mode": "off",
            "name": "hall"
          },
          {
            "coolSetPoint": 20,
            "currentTemp": 71,
            "fanMode": "off",
            "heatSetPoint": 100,
            "id": "101",
            "mode": "off",
            "name": "living room"
          }
        ]
      }
    ]
  }
  ```

### GET /locations/{location_id} - Get a location by id
##### responses
- 404 Not Found
- 200 OK - application/json

  ```
  {
    "location": {
      "id": "1",
      "name": "home",
      "thermostats": [
        {
          "coolSetPoint": 20,
          "currentTemp": 68,
          "fanMode": "off",
          "heatSetPoint": 100,
          "id": "100",
          "mode": "off",
          "name": "hall"
        },
        {
          "coolSetPoint": 20,
          "currentTemp": 71,
          "fanMode": "off",
          "heatSetPoint": 100,
          "id": "101",
          "mode": "off",
          "name": "living room"
        }
      ]
    }
  }
  ```

### GET /locations/{location_id}/thermostats - Get all thermostats for a specific location
##### responses
- 404 Not Found
- 200 OK - application/json

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
##### responses
- 404 Not Found
- 200 OK - application/json

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

### PUT /locations/{location_id}/thermostats/{thermostat_id} - Change settings on a thermostat. Some or all fields
##### body

 ```
  {
    "heatSetPoint": 100,
    "fanMode": "off",
    "name": "hall",
    "coolSetPoint": 20,
    "mode": "off"
  }
  ```

##### responses
- 404 Not Found
- 400 Bad Request - invalid data
- 200 OK - application/json

  ```
  {
    "heatSetPoint": 100,
    "fanMode": "off",
    "name": "hall",
    "coolSetPoint": 20,
    "mode": "off"
  }
  ```
