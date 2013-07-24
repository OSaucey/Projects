"""
template.py -- Template Creator and README Updater

Parses the list of avaliable projects, allows the user to select the one to be
worked on, creates the barebones file, and updates the README with the link.

TODO: Parse README.md to get category, name, and description; ignore completed.
      Get search phrase from user and list all matching projects; user picks.
	  Ask user for filename.
	  Create corresponding python file in correct directory and update README.
""" 

bareTemplate = '''"""
+filename -- +programName

+description

TODO: 
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
    # sys.argv[0] is the python file being ran; ie, +filename
    args = ' '.join(sys.argv[1:])
else:
    args = input("Enter arguments: ")
	

'''

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


#Remove this and implementing here