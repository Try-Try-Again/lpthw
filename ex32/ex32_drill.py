#assign a list containing integers to a variable
the_count = [1, 2, 3, 4, 5]
#assign a list containing strings to a variable
fruits = ['apples', 'oranges', 'pears', 'apricots']
#assign a list containing both integers and strings to a variable
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
#do every item in 'the_count', do the following:
for number in the_count:
    #print a string
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we dont know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
# assign an empty list to a variable
elements = []

print(f"Adding numbers to the list.")
#append is a function that lists understand
#use append to add elements to a list one item at a time.
elements.append(0)
elements.append(1)
elements.append(2)
elements.append(3)
elements.append(4)
elements.append(5)

# now we can print them out too
#For every item in 'elements', do the following:
for i in elements:
    print(f"Element was: {i}")
