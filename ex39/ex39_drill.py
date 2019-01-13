# create a mapping of state to abbreviation
#make with state names as keys and abbreviations as values
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
#make a list with state abbreviations as keys and cities as values
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
#add some key/value pairs to 'cities'
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
#print out a line
print('-' * 10)
#print a string with the value for key 'NY' in the dict 'cities'
print("NY State has: ", cities['NY'])
#print a string with the value for key 'OR' in the dict 'cities'
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
# print a string with the value for key 'Michigan' from 'states'
print("Michigan's abbreviation is: ", states['Michigan'])
# print a string with the value for key 'Florida' from 'states'
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state the cities dict
print('-' * 10)
# get the abbreviation from the value in dict 'states' and use it as the key for 'cities'
print("Michigan has: ", cities[states['Michigan']])
print("florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
#use a for loop to assign the key/value pair to 'state' and 'abbrev' respectively and...
for state, abbrev in list(states.items()):
    #print a string with 'state' and 'abbrev'
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
#use a for loop to assign the key/value pair to 'abbrev' and 'city' respectively and...
for abbrev, city in list(cities.items()):
    #print a string with 'abbrev' and 'city'
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
# use .get() to assign the item from 'states' to 'state'
state = states.get('Texas')

#if state == false:
if not state:
    #print a string
    print("Sorry, no Texas.")

# get a city with a default value
# use .get() to retieve the value from key 'TX' and assign it to 'city'
# if .get() cant find the key, return 'Does Not Exist' instead
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
