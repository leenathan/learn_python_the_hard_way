from sys import argv

script, filename = argv

#assign filename to variable
file = open(filename)

#read file
print "Hey, sweet file. Here's what it says."
print file.read()

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#open with write permissions
print "Opening the file..."
target = open(filename, 'w')

#clear contents
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#write lines
target.write("%s \n %s \n %s \n " % (line1, line2, line3))

#close file
print "And finally, we close it."
target.close()
