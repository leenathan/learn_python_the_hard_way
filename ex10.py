#redone 14 June 2015
#What was that?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '''
What is this triple-single-quote business?
'''

print "\n More stuff"
print "Bell: \a IT MAKES SOUNDS!"
print "Backspace: \b yay"
print "Formfeed: \f yay"
print "Return: \r yay"
print "tab: \t yay"

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,

name = "Lee"
print "My \\name \\is \\%s" % name
print "My \\name \\is \\%r" % name

phrase = "\nLee"
phrase2 = "\\backslash\\"

print "The phrase using r is %r" % phrase
print "The phrase2 using r is %r" % phrase2

print "The phrase using s is %s" % phrase
print "The phrase2 using s is %s" % phrase2

