from hashlib import new
import json
import forecast_class as fr
import forecast_functions as tr 



#------------- Initial Variables-----------------------------

show_results = True                                         # Display Challenge Results if True
export_results = True                                       # Exports a Json with the results (For the api)
file_name = 'Forecast.json'                                 # Name of the file that is going to be saved
day = 0                                                     # Starting day
total_days = 3600                                           # Day limit
sun_x, sun_y = 0, 0                                         # Sun X and Y crds


#----------- Define Starting variables-----------------------

weather_streak = 0                                          # Here variables are defined
last_weather = ""                                           # We give them values to declare the variable type
days_record_planet_a = []                                   
days_record_planet_b = []
days_record_planet_c = []
max_perimeter =   {
        "max_value": 0,
        "count":     0,
        "days":     [],
        }

#---------- Define Variables inside Classes ---------------
                                                            # Variables we dont know yet will be defined as null
planet_a = fr.planet("Ferengui", 500, True, 1, 1)           # Planet Ferengui is planet A
planet_b = fr.planet("Betasoide", 2000, True, 3, 2)         # Planet Betasoide is planet B
planet_c = fr.planet("Vulcano", 1000, False, 5, 3)          # Planet Vulcano is planet C
                                                            # We define the 4 different weathers
weather_a, weather_b, weather_c, weather_d = fr.weather("optimo"), fr.weather("lluvia"), fr.weather("sequia"), fr.weather("normal")

#----------Run our defined method calc_coordinates_xy ----- 
#----------to define the coordinates of each planet -------
#---- This is looped by the amount of days to calculate ---

while day <= total_days:
    planet_a.cords_x = planet_a.calc_coordinates_xy(day).get("X")       # Calculate the Coordinates of Ferengui     "X"
    planet_a.cords_y = planet_a.calc_coordinates_xy(day).get("Y")       # Calculate the Coordinates of Ferengui     "Y"
    planet_b.cords_x = planet_b.calc_coordinates_xy(day).get("X")       # Calculate the Coordinates of Betasoide    "X"
    planet_b.cords_y = planet_b.calc_coordinates_xy(day).get("Y")       # Calculate the Coordinates of Betasoide    "Y"
    planet_c.cords_x = planet_c.calc_coordinates_xy(day).get("X")       # Calculate the Coordinates of Vulcano      "X"
    planet_c.cords_y = planet_c.calc_coordinates_xy(day).get("Y")       # Calculate the Coordinates of Vulcano      "Y"

    weather = tr.forecast(planet_a.cords_x,                             # We run our Forecast function to determine
                          planet_a.cords_y,                             # Which climate corresponds to the combination
                          planet_b.cords_x, 
                          planet_b.cords_y, 
                          planet_c.cords_x, 
                          planet_c.cords_y, 
                          sun_x, 
                          sun_y)

    new_perimeter = tr.area (planet_a.cords_x,                          # We want to know the perimeter 
                             planet_a.cords_y,                          # if it rains, it will help us find
                             planet_b.cords_x,                          # how much pressure there is 
                             planet_b.cords_y,                          # (Exersice 3)
                             planet_c.cords_x, 
                             planet_c.cords_y, )
                                                                        # Compare the results with the other perimeters
    max_perimeter = tr.perimeter_counter(max_perimeter, new_perimeter, day)
    
    if last_weather == weather:                                         # How many times in a row did we have this same forecast
        weather_streak += 1
    else:
        weather_streak = 1

    if  weather == "optimo":                                            # Prepares the results to later insert them to 
        weather_a.counter(weather_streak)                               # The database (JSON, NOSQL)
        weather_a.add_db(days_record_planet_a, planet_a.cords_x, planet_a.cords_y, day, 'Nice day', new_perimeter)
        weather_a.add_db(days_record_planet_b, planet_b.cords_x, planet_b.cords_y, day, 'Nice day', new_perimeter)
        weather_a.add_db(days_record_planet_c, planet_c.cords_x, planet_c.cords_y, day, 'Nice day', new_perimeter)
    elif weather == "lluvia":
        weather_b.counter(weather_streak) 
        weather_b.add_db(days_record_planet_a, planet_a.cords_x, planet_a.cords_y, day, 'Nice day', new_perimeter)
        weather_b.add_db(days_record_planet_b, planet_b.cords_x, planet_b.cords_y, day, 'Nice day', new_perimeter)
        weather_b.add_db(days_record_planet_c, planet_c.cords_x, planet_c.cords_y, day, 'Nice day', new_perimeter)
    elif weather == "sequia":
        weather_c.counter(weather_streak) 
        weather_c.add_db(days_record_planet_a, planet_a.cords_x, planet_a.cords_y, day, 'Nice day', new_perimeter)
        weather_c.add_db(days_record_planet_b, planet_b.cords_x, planet_b.cords_y, day, 'Nice day', new_perimeter)
        weather_c.add_db(days_record_planet_c, planet_c.cords_x, planet_c.cords_y, day, 'Nice day', new_perimeter)
    elif weather == "normal":
        weather_d.counter(weather_streak) 
        weather_d.add_db(days_record_planet_a, planet_a.cords_x, planet_a.cords_y, day, 'Nice day', new_perimeter)
        weather_d.add_db(days_record_planet_b, planet_b.cords_x, planet_b.cords_y, day, 'Nice day', new_perimeter)
        weather_d.add_db(days_record_planet_c, planet_c.cords_x, planet_c.cords_y, day, 'Nice day', new_perimeter)

    last_weather = weather                                              # Sets last_weather to compare in the next loop
    day += 1                                                            # +1 day, counter for the loop

                                                                        # Prints the results of the challenge
if show_results is True:
    print("----------------- Total Talues ----------------------")
    print("", weather_a.name, ": ", weather_a.count, "\n", weather_b.name, ": ", weather_b.count, "\n", weather_c.name, ": ", weather_c.count, "\n", weather_d.name, ": ", weather_d.count)
    print("----------------- Max times in a row -----------------")
    print("", weather_a.name, ": ", weather_a.max_streak,"\n", weather_b.name, ": ", weather_b.max_streak, "\n", weather_c.name, ": ", weather_c.max_streak, "\n", weather_d.name, ": ", weather_d.max_streak)
    print("----------------- Max Perimeter ----------------------")
    print("Max Perimeter: ", max_perimeter["max_value"], "\nHow many times: ", max_perimeter["count"], "\nWhich days: ", max_perimeter["days"])
    print("-----------------------------------------------------")

#------ Saves results into a local json -------------------------

fr.planets = planet_a.db_create(days_record_planet_a)                   # Saves each combination to the NOSQL Database
fr.planets = planet_b.db_create(days_record_planet_b)                   # Everything is appended here to each planet
fr.planets = planet_c.db_create(days_record_planet_c)

if export_results is True:
    with open(file_name, 'w') as f:                                     # Saved as .Json
        f.truncate(0)
        json.dump(fr.planets, f)

    
