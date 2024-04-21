#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

all_cities = fs.all(City)
print("All Cities: {}".format(len(all_cities.keys())))
for state_key in all_cities.keys():
    print(all_cities[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# Create a new City
new_city = City()
new_city.name = "Lagos"
fs.new(new_city)
fs.save()
print("New State: {}".format(new_city))

# # All States
# all_states = fs.all(State)
# print("All States: {}".format(len(all_states.keys())))
# for state_key in all_states.keys():
#     print(all_states[state_key])

# # All Cities
# all_cities = fs.all(City)
# print("All States: {}".format(len(all_cities.keys())))
# for state_key in all_cities.keys():
#     print(all_cities[state_key])

# # Create another State
# another_state = State()
# another_state.name = "Nevada"
# fs.new(another_state)
# fs.save()
# print("Another State: {}".format(another_state))

# # Create another City
# another_city = City()
# another_city.name = "Nevada"
# fs.new(another_city)
# fs.save()
# print("Another State: {}".format(another_city))

# # All States
# all_states = fs.all(State)
# print("All States: {}".format(len(all_states.keys())))
# for state_key in all_states.keys():
#     print(all_states[state_key])

# All Cities
all_cities = fs.all(City)
print("All States: {}".format(len(all_cities.keys())))
for state_key in all_cities.keys():
    print(all_cities[state_key])

# Delete the new State
fs.delete(new_state)

# # Delete the new City
# fs.delete(new_city)

# print("Only state ...")
# # All States
# all_states = fs.all(State)
# print("All States: {}".format(len(all_states.keys())))
# for state_key in all_states.keys():
#     print(all_states[state_key])
