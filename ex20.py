#redone 22 June 2015
#Functions and Files

#import arguments
from sys import argv

#set variable arguments
script, input_file = argv

#function to write 3 lines to a file
def write_line(f):
	file_to_write = open(f,'w')
	file_to_write.write(raw_input("1> "))
	file_to_write.write("\n")
	file_to_write.write(raw_input("2> "))
	file_to_write.write("\n")
	file_to_write.write(raw_input("3> "))
	file_to_write.close()

#define print_all function. Reads and prints an entire file, passed via an argument.
def print_all(f):
	print f.read()

#define rewind function. 'Seeks' to first line of file, passed via an argument.
def rewind(f):
	f.seek(0)
	
#define print_a_line function. Passed a line number and a file, prints the current line. I don't think line_count does anything to the readline function. Readline just inherently goes sequentially from \n to \n.
def print_a_line(line_count, f):
	print line_count, f.readline()
	
#calls write file, to write to the file that was called in the ex20.py CLI command. I can write to the input file, to ensure that the rest of the exercise is reading lines properly.
print "Write to test.txt"
write_line(input_file)
	
#sets current_file as the opened file passed in the initial CLI command
current_file = open(input_file)

print "First let's print the whole file: \n"

#uses print_all to print entire file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#uses rewind to seek to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

#prints file line by line, using print_a_line function. 
current_line = 1
print_a_line(current_line, current_file)

#+= operator increments argument to variable called.
current_line += 1
print_a_line(current_line, current_file)

#reworked to use +=
current_line += 1
print_a_line(current_line, current_file)