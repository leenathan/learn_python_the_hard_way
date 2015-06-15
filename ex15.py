#Redone 15 June 2015
#Reading Files

from sys import argv
#imports the arguments module to handle command line args

bunny, puppy = argv
#initializes two command line arguments

filename = raw_input("Gimme a filename: ")
#new raw_input method of getting filename from user

txt = open(filename)
#sets value of txt variable to be the result of opening a file

print "Here's your file %r:" % filename
#Prints text with your filename

print txt.read()
#Reads and prints contents of txt variable (file you provided)

print txt.readlines(10)

txt.close()

#print "Type the filename agian:"
#file_again = raw_input("> ")
#prompts for input to set file_again variable

#txt_again = open(file_again)
#Opens filename and sets variable value

#print txt_again.read()
#Reads and prints contents of txt_again