#import sys module
import sys
#assign arguments from argv to 'input_encoding', and 'error'
script, input_encoding, error = sys.argv

#Define main
def main(language_file, encoding, errors):
    # assign next line in 'language_file' to variable 'line'
    line = language_file.readline()
#if line has text in it...
    if line:
        #run function 'print_line' with args: 'line', 'encoding', and 'errors'.
        print_line(line, encoding, errors)
        #go back to main with the same arguments as before.
        return main(language_file, encoding, errors)

#Define a function called 'print_line'
def print_line(line, encoding, errors):
    #remove the whitespace from the text in 'line' and assign it to 'next_lang'
    next_lang = line.strip()
    #encode the text in 'next_lang' with encoding specified in first arg. handle errors as errors. and assign to 'raw_bytes'
    raw_bytes = next_lang.encode(encoding, errors=errors)

    #decode string in 'raw_bytes' and assign to 'cooked_string'
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    #print a string including 'raw_bytes' and 'cooked_string'
    print(raw_bytes, "<===>", cooked_string)


#assign file 'languages.txt' with the encoding 'utf-8' to 'languages'
languages = open("languages.txt", encoding="utf-8")

#run main with 'languages' as its 'language_file' argument and 'error' for it's 'errors' argument
main(languages, input_encoding, error)

# You have 4 concepts to explore
# 1.How modern computers store human languages for display and processing and
#   how Python 3 calls these strings.
# 2.How you must ”encode” and ”decode” Python’s strings into a type called bytes.
# 3.How to handle errors in your string and byte handling.
# 4.How to read code and find out what it means even if you’ve never seen it b4
