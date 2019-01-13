#consider how the phrase dictionary is referenced and worked with. we can do 
#something similar 

"""
how this whole enchilada works:

create  a dictionary(PHRASES) with pairs that each have a python expression for
a key and its english equivilent as a value.

if this script was ran with the added argument of 'english', then make a note
to reverse the questions and answers for the user later. 

have python read a webpage which has one word per line and append each of these
lines (formatted to a string) to a list called 'WORDS'

in a try/except, run a 'while true' inside the loop:
create a variable(snippets) and to it, assign a shuffled list of keys from PHRASES 

for every snippet in snippets:
find the key in PHRASES that shares the value with that snippet and assign its
value to a variable called phrase assign to 'question' and 'answer' - what is
returned from convert(snippet,phrase)

convert:

"""

#import random !!!research random
import random
#import urlopen from urllib.request
from urllib.request import urlopen
#import sys
import sys

#assign url string to WORD_URL
WORD_URL = "http://learncodethehardway.org/words.txt"
#create an empty list called WORDS
WORDS = []
#create a dictionary called PHRASES - they have parts missing - replaced with
# '%%%','***', and '@@@'
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***, ***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
}

# do the want to drill phrases first
#if there are 2 arguments in argv AND the second argument is 'english'...
if len(sys.argv) == 2 and sys.argv[1] == "english":
    #set 'PHRASE_FIRST' to True
    PHRASE_FIRST = True
else:
    #...
    PHRASE_FIRST = False

# load up the words from the website
#for every item in what is returned from"urlopen(WORD_URL).readlines()"....
for word in urlopen(WORD_URL).readlines():
    #take the item, strip it, set the encoding to "utf-8", and append it to WORDS
    WORDS.append(str(word.strip(), encoding="utf-8"))

#define a new function that takes the arguments - snippet, and phrase
def convert(snippet, phrase):
    #this is some new tech - return w.capitalize() for each w in ...
    #return the result of running the .capitalize method of whatever is next from
    #a for-loop. 
    class_names = [w.capitalize() for w in 
            #get a list of random items from 'WORDS' - the list should be 
            #only as long as the count of '%%%' in the string in 'snippet' 
                   random.sample(WORDS, snippet.count("%%%"))]
    #do the same random sample list as above but without the capitalization
    # and for count of '***' in snippet
    other_names = random.sample(WORDS, snippet.count("***"))
    #...
    results = []
    #...
    param_names = []
    #for i's for how ever many "@@@"s there are in the snippet...
    for i in range(0, snippet.count("@@@")):
        #assign param_count a random number between 1 and 3
        param_count = random.randint(1,3)
        #to param_names (which is now empty), append a a random sampled list 
        #from 'WORDS'joined by ','s - the list should be just as long as 
        #long as as 'paran_count'.
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    # for sentence in snippet,
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            #research replace method
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        #create 'snippets', and assign a list of all the keys in 'PHRASES'
        snippets = list(PHRASES.keys())
        #shuffle snippets
        random.shuffle(snippets)
        #for every snippet in snippets (every key in 'phrases')
        for snippet in snippets:
            #go find the key that == whats in the snippet and assign its value
            #to phrase
            phrase = PHRASES[snippet]
            #pass snippet (the string in a list of keys and phrase - the value of 
            #of the dict pair in PHRASES whos key is equal to snippet.
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
