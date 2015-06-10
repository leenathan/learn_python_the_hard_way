'''i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
'''

def countup(max, incrementer):
	
	#define numbers
	numbers = []
	i=0
	
	#while loop for incrementing
	for i in range(0, max): #for loop can't be incrememnted by anything other than 1!
		numbers.append(i)
		
		i = i+ incrementer
	
	for num in numbers:
		print num


countup(20,2)
