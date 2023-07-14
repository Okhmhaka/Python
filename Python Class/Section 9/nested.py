# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berline"
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    # In order to nest a dictionary within a dictionary, there has to be another set of {}.
    # Example: Office locations within Germany, and how many annual trips I need to make.
    # Below we have a list nested inside of a dictionary, and the dictionary is nested inside of the travel_log dictionary.
    "Germany": {"office_locations": ["Berlin", "Hamburg", "Stuttgart"], "annual_trips": 4}
}

# Nesting dictionaries inside of a list.
# The first change from above is to change the dictionary {} to list []
# Data types in dictionaries can be mixed up, but there must be a key-value pair for each piece of data.
travel_log = [
    # Next change the key to county, then add the cities visited within that city.
    # For best coding practices, move each key/value pair onto it's own line which is separated by a comma
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},
    # In order to nest a dictionary within a dictionary, there has to be another set of {}.
    # Example: Office locations within Germany, and how many annual trips I need to make.
    # Below we have a list nested inside of a dictionary, and the dictionary is nested inside of the travel_log dictionary.
    {"country": "Germany",
     "office_locations": ["Berlin", "Hamburg", "Stuttgart"],
     "annual_trips": 4}
]
