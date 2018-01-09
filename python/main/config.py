# ORBIT configs

ORBIT1_LENGTH = 18
ORBIT1_CRATERS = 20

ORBIT2_LENGTH = 20
ORBIT2_CRATERS = 10


# VEHICLE configs
VEHICLES = {
    "BIKE": {
        "SPEED": 10,
        "CRATER_CROSS_TIME": 0.0334
    },
    "TUKTUK": {
        "SPEED": 12,
        "CRATER_CROSS_TIME": 0.0167
    },
    "CAR": {
        "SPEED": 20,
        "CRATER_CROSS_TIME": 0.05
    }
}


# WEATHER CONDITIONS
WEATHER_CONDITIONS = {
    "sunny": {
        "CATERS_REDUCED": 0.1,
        "CATERS_INCREASED": 0,
        "VEHICLES": ["CAR", "BIKE", "TUKTUK"]
    },
    "rainy": {
        "CATERS_REDUCED": 0,
        "CATERS_INCREASED": 0.2,
        "VEHICLES": ["CAR", "TUKTUK"]
    },
    "windy": {
        "CATERS_INCREASED": 0,
        "CATERS_REDUCED": 0,
        "VEHICLES": ["CAR", "BIKE"]
    }
}
