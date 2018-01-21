from sys import argv

script, input_file = argv

# define function to print entire file
def print_all(f):
	print f.read()

# define function to return to beginning of file object
def rewind(f):
	f.seek(0)

# define function to print one line from file
def print_a_line(line_count, f):
	print line_count, f.readline(),

# create file object from script argument
current_file = open(input_file)

print "First let's print the whole file:\n"

# print file object
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# reset location in file object
rewind(current_file)

# print three lines
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)