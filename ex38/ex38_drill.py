#assign 1 string to to 'ten_things'
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print a string
print("Wait there are not 10 things in that list. Let's fix that.")

#split the string on every 'space' (' ') and put each split in list 'stuff'
stuff = ten_things.split(' ')
#assign 8 strings to list 'more_stuff'
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

#while the lenth of 'stuff' does not equal 10, do the following
while len(stuff) != 10:
    #pop off the first item from 'more_stuff', and assign it to 'next_one'
    next_one = more_stuff.pop()
    #print a string and 'next_one'
    print("Adding: ", next_one)
    #append next_one to stuff
    stuff.append(next_one)
    #print an 'f' string with the length of 'stuff'
    print(f"There are {len(stuff)} items now.")

#print a string and 'stuff'
print("There we go: ", stuff)

#print another string
print("Let's do some things with stuff.")

#print the second item in stuff
print("stuff[1]", stuff[1])
#print the last thing on the list
print("stuff[-1]", stuff[-1]) # whoa! fancy
#pop off the last thing on the list and print it
print("stuff.pop()", stuff.pop())
#join all the items in stuff together with spaces (' ') and print it
print(' '.join(stuff)) # what? cool!
#join items 3 to 5(not 5) together with '#' and print it
print('#'.join(stuff[3:5])) # super stellar!
