# Ask the user if they want to convert temperature,
# distance, or weight
unit_type = input("Do you want to convert temperature, distance, or weight?")

# Ask the user if they would like to start in 
# metric or US
starting_unit = str(input("Would you like to start in metric or US units?"))

# Ask the user for their starting value
starting_value = int(input("What is your starting value?"))
# "42" -> 42
# (10°C × 9/5) + 32 = 50°F
# 1 meter = 3.281 feet
# 1 kg = 2.205 lbs
# Convert Units
result = None
strt = None
end = None
if unit_type == "temperature":
    # Convert temp
    if starting_unit == "metric":
        # Celcius -> Farenheit
        strt = "Celcius"
        end = "Farenheit"
        result = (starting_value * 9/5) + 32 
    else:
        # Farenheit -> Celcius
        strt = "Farenheit"
        end = "Celcius"
        result = (starting_value - 32) * 5/9
elif unit_type == "distance":
    # Convert distance
    if starting_unit == "metric":
        # Meters -> Feet
        strt = "Meters"
        end = "Feet"                        
        result = starting_value * 3.281
    else:
        # Feet -> Meters
        strt = "Feet"
        end = "Meters"
        result = starting_value / 3.281
elif unit_type == "weight":
    # Convert weight
    if starting_unit == "metric":
        # Kilograms -> Pounds
        strt = "KG"
        end = "LBS"
        result = starting_value * 2.205
    else:
        # Pounds -> Kilograms
        strt = "LBS"
        end = "KG"
        result = starting_value / 2.205

# Print result with information
# <> unit1 is <> unit2
print ("%s %s is %s %s"%(starting_value, strt, result, end)) 