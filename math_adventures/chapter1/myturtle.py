# TEST YOUR MATH IN THE SHELL!!

from turtle import *
shape('turtle')


def square(sidelength):
    for i in range(4):
        forward(sidelength)
        right(90)


def triangle(sidelength):
    for i in range(3):
        forward(int(sidelength))
        right(120)


def polygon(sidelength, sides):
    for i in range(sides):
        forward(sidelength)
        right(360/int(sides))

        
def make_ster(sidelength, sides):

    if sides % 2 == 0:
        reps = sides * 2
    else:
        reps = sides
    
    for i in range(reps):
        forward(sidelength)
        right(180-180/int(sides))



#for i in range(60):
#    polygon(5*(i+1), 4)
#    right(5)
make_ster(200, 9)

while True:
    right(10)

done()
