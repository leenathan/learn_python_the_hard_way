#redone 14 June 2015
#Asking questions

print "how old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and weigh %r." % (age, height, weight)

print "\n\n"
print "How many cookies do you want?",
cookies = int(raw_input())
print "So you want %d cookies? %d dozen?" % (cookies, cookies/12)