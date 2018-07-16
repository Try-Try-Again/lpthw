# assign nil to "i"
#create empty list called "numbers"

#while i is less than six, do the following:
def counter(count, stepsize): 
    numbers = []
    for i in range(0, count * stepsize, stepsize):
        #print a formatted string 'i'
        print(f"At the top i is {i}")
        #append current 'i' to the list
        numbers.append(i)

        #print a string with the value of 'numbers'
        print("Numbers now: ", numbers)
        #print a formatted string with 'i'
        print(f"At the bottom i is {i}")


    #print string
    print("The numbers: ")

    #while theres stuff in 'numbers', pop off an item from 'numbers' and
    #put it in num, and then do the following
    for num in numbers:
        #print 'num'
        print(num)


counter(11, 10)
counter(7, 4)
counter(9, 9)
