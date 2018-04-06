#defines the cheese_and_crackers function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#print fstrings with cheese_and_crackers' arguments
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
#print simple strings
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


#print a string
print("We can just give the function numbers directly:")
#call cheese_and_crackers with two numbers as the arguments
cheese_and_crackers(20, 30)


#print a string
print("OR, we can use variables from our script:")
#declare two variables with numbers for values
amount_of_cheese = 10
amount_of_crackers = 50

#call cheese and crackers with the above variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#print a string
print("We can even do math inside too:")
#call cheese_and_crackers with mathmatical operations as arguments
cheese_and_crackers(10 + 20, 5 + 6)


#print a string
print("And we can combine the two, variables and math:")
#call cheese_and_crackers with mathmatical operations involving the
#previously delcared variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
