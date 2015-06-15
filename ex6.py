#Redone 14 June 2015
#Strings and text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
#prints x variable, recalling the value of the %d format character (10)

print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
#prints joke evaluation, replacing the value of the hilarious variable in the place of %r

w = "This is the left side of..."
e = "a string with a right side."

print w + e
