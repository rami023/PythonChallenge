

def area(x1, y1, x2, y2, x3, y3):                                   # Function defined to calculate the area
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

def is_inside(x1, y1, x2, y2, x3, y3, x, y):                        # Checks if it is inside the triangle. 
    A = area (x1, y1, x2, y2, x3, y3)                               # Calculate area of ABC 
    A1 = area (x, y, x2, y2, x3, y3)                                # Calculate area of PBC    
    A2 = area (x1, y1, x, y, x3, y3)                                # Calculate area of PAC
    A3 = area (x1, y1, x2, y2, x, y)                                # Calculate area of PAB                                                                 
    if(A == A1 + A2 + A3):                                          # Check sum of A1 / A2 / A3 is same as A
        return True                                                 
    else:                                                           
        return False

def is_straight(coordinates_bundle):                                # Checks if the line is straight
    (x0, y0), (x1, y1) = coordinates_bundle[0], coordinates_bundle[1]
    for i in range(2, len(coordinates_bundle)):                     # Loops for each coordinate
        x, y = coordinates_bundle[i]                        
        if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):            
            return False                                            # Returns False if not
    return True                                                     # Returns True if it is a straight line

def perimeter_counter(max_perimeter, new_perimeter, day):           # Function that returns the current log of the 
    if max_perimeter["max_value"] > new_perimeter:                  # Highest perimeter (Only the highest one)
        return  max_perimeter                                       # Returns: Perimeter, ocurrences, days that happened

    elif max_perimeter["max_value"] == new_perimeter:
        max_perimeter.update({"count": int(max_perimeter["count"] +1)})
        day_list = max_perimeter["days"]
        day_list.append(day)
        max_perimeter.update({"days": day_list})
        return  max_perimeter

    elif max_perimeter["max_value"] < new_perimeter:
        max_perimeter.update({"max_value": new_perimeter})
        max_perimeter.update({"count": 1})
        max_perimeter.update({"days": [day]})
        return  max_perimeter

def forecast (planet1_x,                                            # Function that calculates the forecast of the planets
              planet1_y,                                            # In this case all share the same rules, so they all get the  
              planet2_x,                                            # Same output.
              planet2_y,                                                
              planet3_x, 
              planet3_y, 
              sun_location_x, 
              sun_location_y):

    coordinates = [[planet1_x, planet1_y],                          # Define X Y of each planet
                   [planet2_x, planet2_y],  
                   [planet3_x, planet3_y]]

    straight = is_straight(coordinates)                             # Is it a straight line? If not, it is a triangle
    
    if straight is True:                                            # Does this line passes through the sun?
        coordinates = [[planet1_x, planet1_y],
                       [planet2_x, planet2_y],
                       [planet3_x, planet3_y], 
                       [sun_location_x, sun_location_y]]

        straight = is_straight(coordinates)

        if straight is True:                                        # Result 1
            return "sequia"
        elif straight is False:                                     # Result 2
            return "optimo"   

    elif straight is False:                                         # If it is a triangle
        in_triangle = is_inside(planet1_x,                          # Is the sun inside it?
                                planet1_y, 
                                planet2_x, 
                                planet2_y, 
                                planet3_x, 
                                planet3_y, 
                                sun_location_x, 
                                sun_location_y)
        if in_triangle is True:                                     
            return "lluvia"                                         # Result 3
        elif in_triangle is False: 
            return "normal"                                         # Reuslt 4


