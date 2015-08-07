#Redone 25 June 2015
#and 7 August 2015
#Functions can return something

def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a,b):
	print "DIVIDING %d / %d: " % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(22,7)
height = subtract(80,7)
weight = multiply(82,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 10))))

print "That becomes: ", what, "Can you do it by hand?"

#age+{height-[weight*(iq/10)]}
#(29 + (73 - (164 * (50 / 10)
#(29 + (73 - (164 * 5)))
#(29 + (73 - (820)))
#(29 + (-747))
#-718

#Age-normalized body ratio:(height/weight)/age
what2 = divide(divide(height,weight),age)

print "Here's your age-normalized body ratio: ",what2,"!"