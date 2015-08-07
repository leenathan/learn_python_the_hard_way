#redone 19 June 2015
#functions and variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
#Defines function, 2 args
	print "You have %d cheeses!" %cheese_count
	#prints line, referencing first arg
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#prints line, referencing second arg
	print "Man that's enough for a party!"
	print "Get some beer. \n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
#passes numbers directly to function args

print "OR, we can use variables from our script.:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#passes variables to args

print "We can even do math inside, too!:"
cheese_and_crackers(10+20,5+6)
#math first, then run function with results

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#Variables and math! Math performed on variable values, then passed to function

def lee_function(noun, verb, adverb):
	print "%s %s %s \n" % (noun, verb, adverb)

lee_function(raw_input("noun: "),raw_input("verb: "),raw_input("adverb: "))
