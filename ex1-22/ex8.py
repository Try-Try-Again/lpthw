#makes a simple string with curly braces in them
formatter = "{} {} {} {}"

#prints the string declared above in formatted form - makeing the curly braces
#places to add stuff.
#adds simple numbers to 'formatter'
print(formatter.format(1, 2, 3, 4))
#adds english words for 1, 2, 3, and 4
print(formatter.format("one", "two", "three", "four"))
#adds boolean values in the curly braces
print(formatter.format(True, False, False, True))
#formatterception! puts formatter in each set of curly braces.
print(formatter.format(formatter, formatter, formatter, formatter))
#formats 'formatter' to sing a frank zappa masterpiece

print(formatter.format(
    "Watch out where",
    "the huskies go",
    "and don't you eat that",
    "yellow snow..."
))
