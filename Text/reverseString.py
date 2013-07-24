"""
reverseString.py -- Reverse a String

Enter a string and the program will reverse it and print it out.
"""

# Used to get command line arguments as sys.argv[].
import sys
# If using Python2, rename raw_input() to input(); no change for Python3.
try:
    input = raw_input
except NameError:
    pass

# Process command line arguments. If none given, ask at run-time.
if len(sys.argv) > 1:
    # sys.argv[0] is the python file being ran; ie, reverseString.py
    phrase = ' '.join(sys.argv[1:])
else:
    phrase = input("Enter a word/phrase: ")

# Output original phrase and the reversed phrase.
print("Original: %s\nReversed: %s" %(phrase, phrase[::-1]))
