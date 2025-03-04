programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])
print()

# Empty dictionary
empty_dictionary = {}

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
print()

capitals = {
    "France": "Paris",
    "Nigeria": "Abuja",
    "Germany": "Berlin",
    "Japan": "Tokyo",
}

# Nested List and Dictionary in Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Little", "Dijon"],
        "total_visits": 12
    },
    "Nigeria": {
        "cities_visited": ["Bariga", "Ajah", "Lekki"],
        "total_visits": 3
    }
}

print(travel_log["France"])
print(travel_log["France"]['cities_visited'])
