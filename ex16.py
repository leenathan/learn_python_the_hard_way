# redone 15 June 2015
# Reading and writing files

from sys import argv

script, filename = argv
#establish arguments

print "We're going to erase Mr. %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
#prompt for input

print "Opening the file..."
target = open(filename, 'w')
#sets target variable as opened file, passed by initial argument

print "Truncating the file. Goodbye!"

target.truncate()
#truncates file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2= raw_input("Line 2: ")
line3 = raw_input("Line 3: ")
#prompts for 3 lines

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#writes lines, with new line after each

print "And finally, we close it."
target.close()
#closes file