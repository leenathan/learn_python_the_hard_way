from sys import argv

#handle arguments passed when calling script
script, input_file = argv

#define print function
def print_all(f):
	print f.read()

#define rewind function - go to line 0	
def rewind(f):
	f.seek(0)

#define print a line 	
def print_a_line(line_count, f):
	print line_count, f.readline()

#open file referenced when calling script
current_file = open(input_file)

print "First let's print the whole file: \n"

#call print_all
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#rewind to line 0
rewind(current_file)

print "Let's print three lines:"

#set current line, print it
current_line = 1
print_a_line(current_line, current_file)

#increment line, print it
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
