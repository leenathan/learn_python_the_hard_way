#import arguments 
from sys import argv

#assigns arguments
script, filename = argv

# assigns file contents to txt variable
txt = open(filename)

# Prints name of file
print "Here's your file %r:" % filename

#prints content of file
print txt.read()


print "Type your filename again:"
#variable assigned to raw input, with prompt symbol
file_again = raw_input("> ")

#set variable equal to input file 
txt_again = open(file_again)

#print contents of file
print txt_again.read()

txt_again.close()

txt.close()
