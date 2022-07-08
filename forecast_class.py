import math
#------------- Define Classes & Methods --------------------
planets = []

class planet:                                                       # We define the class that contains all the planets info.
    def __init__(self, name, distance, clockwise, rotation, planet_id, cords_x = None, cords_y = None):
        self.name = name                                            # Planet name
        self.distance = distance                                    # Planet distance to the Sun
        self.clockwise = clockwise                                  # True if the planets rotates clockwise
        self.rotation = rotation                                    # Planet Sun rotation per day in deg
        self.cords_x = cords_x
        self.cords_y = cords_y
        self.planet_id = planet_id


    def db_create(self, dict):                                      # Create the db here
        planets.append({                                            # It is a Json NoSql Data model
        "planet_id": self.planet_id,                                # Will be explained further in the documentation
        "planet_name": self.name,
        "planet_description": "Economy is blooming",
        "sun_distance": self.distance,
        "rotation": self.rotation,
        "forecast": dict
        })
        return planets

    def calc_coordinates_xy(self, day):                             # Class Method that will calculate the coordinates of the planet
        if self.clockwise == True:                                  # If the planet rotates clockwise calculates the rotation clockwise
            angle = self.rotation * day
            while angle >= 360:
                angle -=360
        elif self.clockwise == False:                               # If the planes rotates anti-clockwise calculates the rotations anti-clockwise
            angle = self.rotation * day * -1
            while angle <= -360:
                angle +=360
                angle = angle - 360 * -1
        coordinates_xy = {                                  
            "X": self.distance * math.cos(angle),                   # Aclarar que height no significa altura YX--------------
            "Y": self.distance * math.sin(angle)}
        return coordinates_xy                                       # Returns a dictionary as a result


class weather:                                                      # We define the class that contains all the planets info.
    def __init__(self, name, count=0, max_streak=0):
        self.name = name                                            # Planet name
        self.count = count                                          # Planet distance to the Sun
        self.max_streak = max_streak                                # Planet Sun rotation per day in deg


    def counter(self, actual_streak):                               # Method that checks if the forecast is in a current 
        self.count += 1                                             # Streak Ex: It happened 4 times in a row.
        if actual_streak > self.max_streak:
            self.max_streak = actual_streak

    def add_db(self, day_list, x, y, day, day_desc, perimeter):
        day_list.append( {                                          # We save each individual planet forecast in a list
                        "day_id":   day,                            # So we can later insert them into the db as a Json
                        "day":      day,    
                        "cord_x":   x,
                        "cord_y":   y,
                        "day_desc": day_desc,
                        "perimeter":perimeter,
                        "weather":  self.name,

                        })