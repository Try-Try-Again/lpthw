#import argv from the sys module
from sys import argv

#unpacks arguments from arg-v and assign those values to two variable
#script, filename = argv

#opens text file and assigns it to a variable
#txt = open(filename)

#prints an fstring including the filename
#print(f"Here's your file {filename}:")
#print the file inside the txt using the read method
#print(txt.read())

#print a basic string
print("Type the filename again:")
#assign value from input to file_again with a custom prompt
file_again = input("> ")


#open whatever file was assigned to file_again using input and assign it's
#contents to txt_again
txt_again = open(file_again)

#print out the file instide text_again using the read method
print(txt_again.read())

#on excercise 5
#here we go!
#wheeeeee!!!!
