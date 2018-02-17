#import argv from the sys module
from sys import argv
#assigns values gathered from argv to some variables.
script, first_name, last_name, home_town = argv

#print a formatted string using variables above
print(f"Greetings {first_name} {last_name}!")
#pep8ified fstring :(
question = f"{first_name}, you should go on vacation, leave {home_town}"
question += " \nWhere would you like to go?"
#assigns user input to a variable and uses the above string as a prompt 
dest = input(question)
#pep8ified string responding to user input
response = f"Alright {first_name}, I'll book your flight from {home_town} to "
response += f"{dest}!"

#print the string above
print(response)
