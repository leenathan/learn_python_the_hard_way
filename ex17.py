#redone 18 June 2015
#More Files 

from sys import argv
from os.path import exists

script, from_filename, to_filename = argv
# to and from files are string variables, not files!

print "Let's edit the source file."
source_file = open(from_filename,'w')
source_file.write(raw_input(">"))
source_file.close()

print "Copying from %s to %s" % (from_filename, to_filename)

#we could do these two on one line, too. How?
#in_file = open(from_filename)
#in_data = in_file.read()

#would this work?
#in_data = open(from_filename).read()

#print "The input file is %d bytes long." % len(in_data)

#print "Does the output file exist? %r" % exists(to_filename)
#print "Ready, hit RETURN to continue. CTRL-C to abort."
#raw_input()

out_file = open(to_filename, 'w')
out_file.write(open(from_filename).read())

print "Alright, all done."

out_file.close()