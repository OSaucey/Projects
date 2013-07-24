"""
pigLatin.py -- Pig Latin

Pig Latin is a game of alterations played on the English language game. To
create the Pig Latin form of an English word the initial consonant sound is
transposed to the end of the word and an ay is affixed (Ex.: "banana" would
yield anana-bay). Read Wikipedia for more information on rules.

TODO: Handle punctuation, possessive nouns, et al.
"""

# Used to get command line arguments as sys.argv[].
import sys
# If using Python2, rename raw_input() to input(); no change for Python3.
try:
    input = raw_input
except NameError:
    pass

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] # Didn't include y
pigList = list()

# Process command line arguments. If none given, ask at run-time.
if len(sys.argv) > 1:
    # sys.argv[0] is the python file being ran; ie, reverseString.py
    phraseList = sys.argv[1:]
else:
    phraseList = input("Enter a word/phrase: ").split(" ")

# Take each word from the phrase ...
for word in phraseList:
    # and find the index of the first vowel letter.
    for index, letter in enumerate(word):
        if letter in vowels:
            break
    
    # If the word starts with a vowel, add 'way' to the end ...
    if index == 0:
        pig = word + 'way'
    # otherwise, move the set of consonents to the end, add 'ay', and fix
    # capitolization if needed.
    else:
        pig = (word[index:] + word[:index] + 'ay').lower()
        if word[0].isupper():
            pig = pig.capitalize()
   # Add the pig latin version of the word to the list.
    pigList.append(pig)

# Turn the lists (english and pig latin) in sentences with spaces and output.
phrase = ' '.join(phraseList)
piggy = ' '.join(pigList)
print("Original: %s\nPigified: %s" % (phrase, piggy))
