#read the file and print it
from sys import argv

script, filename = argv

txt = open(filename)

print(f"{filename} contains the following text:")
print(txt.read())
