print("are you smart?")
smart = input("> ")
if smart.lower() == "yes" or smart.lower() == "y":
    print("spell it")
    it = input("> ")
    if it.lower() == "it":
        print("Hey, you're smart!")
    else:
        print("Nope, you're dumb :P")
else:
    print("Well, at least you're self aware :D")

