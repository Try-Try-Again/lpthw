#assign value "10" to variable named " types of people
types_of_people = 10
#assign a formatted string referencing "types of people" to variable "x"
x = f"There are {types_of_people} types of people."

#assign simple strings to the following variables
binary = "binary"
do_not = "don't"
#assign a formatted string referencing "binary" and "do_not"
y = f"Those who know {binary} and those who {do_not}."

#print variables "x" and "y"
print(x)
print(y)

#print formatted strings referencing some variables
print(f"I said: {x}") #1
print(f"I also said: '{y}'") #2

#assign a boolean value to variable "hilarious"
hilarious = False

#assign a formated string without with empty brackets
joke_evaluation = "Isn't that joke so funny?! {}"

#print joke_evaluation with "hilarious" inserted using the format method
print(joke_evaluation.format(hilarious))

#assign strings to theses variables
w = "This is the left side of..."
e = "a string with a right side."

#concantonate the two previous strings and print the result
print(w + e)

#the "+" symbol can be used to concantinate two strings
