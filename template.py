"""
+filename -- +program_name

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

