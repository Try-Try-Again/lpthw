#import the 'exit' function
from sys import exit

#define 'gold_room' function
def gold_room():
    #print a string
    print("This room is full of gold. How much do you take?")

    #assign input to 'choice'
    try:
        choice = int(input("> "))
    except ValueError:
        #call 'dead' with a string as an argument
        dead("Man, learn to type a number.")

    # convert 'choice' to an integer and assign to 'how_much' 
    how_much = choice
    
    #run the following only if 'how_much' is less than 50
    if how_much < 50:
        #print you win
        print("Nice, you're not greedy, you win!")
        #exit the game
        exit(0)
        #otherwise,
    else:
        #run dead with a string as an argumentf
        dead("You greedy bastard!")


#define function 'bear_room'
def bear_room():
    #print some strings
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are going to move the bear?")
    #set 'bear_moved' to 'False'
    bear_moved = False

    #always run loop
    while True:
        #assign input to 'choice'
        choice = input("> ")

        #if choice equals the string 'take honey', do the following - 
        if choice == "take honey":
            #run dead with a string as an argument
            dead("The bear looks at you then slaps your face off.")
#otherwise, choice equals the string 'taunt bear' and 'bear_moved is set to false - 
        elif choice == 'taunt bear' and not bear_moved:
            #print some strings
            print("The bear has moved from the door.")
            print("You can go through it now.")
            #set 'bear_moved' to True
            bear_moved = True
            #if 'choice' = 'taunt bear' and 'bear_moved' is set to True,
        elif choice == "taunt bear" and bear_moved:
            #run 'dead' with a string as an argument
            dead("The bear gets pissed off and chews your leg off.")
            #if 'choice = 'open door', and 'bear_moved' = True, 
        elif choice == "open door" and bear_moved:
            #run 'gold_room'
            gold_room()
            #oherwise,
        else:
            #print a string
            print("I got no idea what that means.")


#define 'cthulhu_room' function
def cthulhu_room():
    #print some strings
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for life or do you eat your head?")

    #assign input 'choice'
    choice = input("> ")

    #if the string 'flee' is in 'choice',
    if "flee" in choice:
        #run the 'start' function
        start()
        #otherwise, if the string 'head' is in 'choice'
    elif "head" in choice:
        #call 'dead' with a string as an argument
        dead("Well that was tasty!")
        #otherwise,
    else:
        #call 'cthulhu_room'
        cthulhu_room()


#define function 'dead', which takes one argument 'why'
def dead(why):
    #print a string containing the 'why' argument
    print(why, "Good job!")
    #exit the game
    exit(0)

#define start function
def start():
    #print some strings
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    #assign input to 'choice'
    choice = input("> ")

    #if 'choice' = 'left', 
    if choice == "left":
        #call 'bear_room'
        bear_room()
        #otherwise, if 'choice' = 'right'
    elif choice == "right":
        #call 'cthulhu_room'
        cthulhu_room()
        #otherwise,
    else:
        #run 'dead' with a string for an argument
        dead("You stumble around the room until you starve.")


#call 'start'
start()
