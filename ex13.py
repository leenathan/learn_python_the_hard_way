#redone 14 June 2015
# Parameters, unpacking, variables

from sys import argv

script, first, second, third = argv

fourth = raw_input("Fourth?")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "The fourth variable is:", fourth