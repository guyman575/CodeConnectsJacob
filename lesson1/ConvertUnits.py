# Ask the user if they want to convert tempurature,
# distance, or weight
unit_type = "tempurature"

# Ask the user if they would like to start in 
# metric or US
starting_unit = "metric"

# Ask the user for their starting value
starting_value = 42

# Convert Units
result = None
if unit_type == "tempurature":
    # Convert temp
    if starting_unit == "metric":
        # Celcius -> Farenheit
        pass
    else:
        # Farenheit -> Celcius
        pass
elif unit_type == "distance":
    # Convert distance
    if starting_unit == "metric":
        # Meters -> Feet
        pass
    else:
        # Feet -> Meters
        pass
elif unit_type == "weight":
    # Convert weight
    if starting_unit == "metric":
        # Kilograms -> Pounds
        pass
    else:
        # Pounds -> Kilograms
        pass

# Print result with information
