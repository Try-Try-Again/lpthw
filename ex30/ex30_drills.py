#assign numbers to three variables
people = 40
cars = 30
trucks = 45


#if there are more cars than people....
if cars > people:
    print("We should take the cars.")
    #if there are less cars than people,...
elif cars < people:
    print("We should not take the cars")
    #if neither of those conditions were satisfied...
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
elif people < trucks or people < cars:
    print("Where did y'all come from?")
else:
    print("Fine, let's stay home then.")
