"""

1 Assignment 7: Cheating at Scrabble
Write a Python script that takes a Scrabble rack as a command-line argument and prints all valid Scrabble words that can be constructed from that rack, along with their Scrabble scores, sorted by score.

1.1 There are a couple of requirements:
. This needs to be able to be run as a command line tool as you’ll see below. (done)
. You need to handle input errors from the user and suggest what that error might be caused by (helpful error messages).
. Implement wildcards as either * or ?.

1.2 Extra Credit:
. Allow a user to specify that a certain letter has to be at a certain location. Your program must work without it so this should be completely optional.
. Specify that certain letters have to be at certain locations. Again this should be completely optional and the hint should be supplied at the command line.

1.4 Tips
. I would recommend that you work on this and try to break down the problems into steps on your own before writing any code. Once you’ve scoped generally what you want to do, start writing some code and if you get stuck, take a step back and go back to thinking about the problem rather than trying to fix lots of errors at the code level.
You should only use the python standard library in this assignment, however any tool in there is fair game.

1.5 Tips Part 2
If you keep getting stuck check out: https://openhatch.org/wiki/Scrabble challenge.
This is where we got the idea for this assignment and it provides some helpful tips for guiding you along the way.
If that link doesn’t work you can use the google cached version here. However I would sincerely recommend that you try to implement this first yourself before looking at the hints on the website.

Good luck!
1.6 Clarifications:
• Locations of certain letters must be specified at the command line, it may not be some sort of user prompt.
• There can be a total of two wild cards.
• Allowing for than 7 tiles is alright, it’d be worth it to think about what the maximum might be but
we won’t count it against you if you don’t.
• you should not be installing any libraries at this point: anything in the standard library is fair game.
• you may download the word file and keep it in your repository so that the program is standalone.

"""


import sys
import os
from collections import OrderedDict

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
word_rack = {}

## Create a list of words
def create_words (word):
    return word.splitlines()

## Create a rack
def create_rack (word, word_dict):
    for i in range(len(word)):
        ## If a letter doesn't exist, add a new key and value 1.
        if word[i] not in word_dict:
            word_dict[word[i]] = 1
        else:
            word_dict[word[i]] += 1
    return word_dict

## Keep scrabble words
def keep_scrabble_words(word_list, word_dict):
    temp_dict = {}
    valid_words = []
    in_word_dict = True
    for word in word_list:
        temp_dict = create_rack(word.lower(),temp_dict)
        #print(temp_dict)
        for key, value in temp_dict.items():
            if key in word_dict:
                if word_dict[key] < value:
                    in_word_dict = False
            else:
                in_word_dict = False
        ## Add a word to the valid word list.
        if in_word_dict == True:
            #print(1)
            valid_words.append(word.lower())
        ## Reset the conditions.
        temp_dict = {}
        in_word_dict = True
    return valid_words


## Add scores for words and return the ordered dictionary by score
def add_scores(word_list):
    dict_w_scores = {}
    for word in word_list:
        score = 0
        for char in word:
            score += scores[char]
        dict_w_scores[word] = score
    ## Sort the dictionary by score
    return OrderedDict(sorted(dict_w_scores.items(), key=lambda x: x[1],reverse=True))



## Load sowpods.txt
try:
    text = open("SOWPODS/sowpods.txt", 'r')
except IOError:
    print("Can't open input file")
    os._exit(1)

sowpods = text.read()
word_list = create_words(sowpods)
word_rack = create_rack(sys.argv[1].lower(), word_rack)
valid_list = keep_scrabble_words(word_list, word_rack)
ordered_dict = add_scores(valid_list)
## Print the results
for key, value in ordered_dict.items():
    print(value, key)
