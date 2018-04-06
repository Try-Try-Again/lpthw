#import the argv function from the 'sys' library
from sys import argv

#define the arguments that are being passed into argv
script, input_file = argv

def print_all(f):
    print(">>> f=", f)
    print(f.read())
    print("<<< f=", f)

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

#define the 'current_file' variable and assign a value from opening a file 
current_file = open(input_file)

#print a string
print("First let's print the whole file:\n")

#call the 'print_all' function with 'current_file' as the argument
print_all(current_file)

#print a string
print("Now let's rewind, kind of like a tape.")

#call the 'rewind' function with 'current_file' as the arguement
rewind(current_file)

#print some text
print("Let's print three lines:")

#define the 'current_line' variable and assign it the value 1
#current line =1
current_line = 1
#call the 'print_a_line' function with 'current_line' and 'current_file'
#as arguments
print_a_line(current_line, current_file)

#increment the value of the 'current_line' variable by 1
#current line = 2
current_line += 1
#call the 'print_a_line' function with 'current_line' and 'current_file'
#as arguments
print_a_line(current_line, current_file)

#increment the value of the 'current_line' variable by 1
#current line = 3
current_line += 1
#call the 'print_a_line' function with 'current_line' and 'current_file'
#as arguments
print_a_line(current_line, current_file)
