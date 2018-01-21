# Import function argv from module sys
from sys import argv

# Map arguments to script name, filename
script, filename = argv

# Create file object txt of filename
txt = open(filename)

# Print string, filename
print "Here's your file %r:" % filename
# Read file object, print
print txt.read()
# Close file txt
txt.close()
# Ask for filename
# print "Type the filename again:"
# Assign file_again to user input
# file_again = raw_input("> ")
# 
# Create file object txt_again of file_again
# txt_again = open(file_again)
# 
# Read file object txt_again, print
# print txt_again.read()