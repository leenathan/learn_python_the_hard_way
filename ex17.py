from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on line too, how?
#in_file = open(from_file)

#Read input file - combined from two lines
indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#write output files
open(to_file, 'w').write(indata)

print "Alright, all done."

#out_file.close()
#in_file.close()

