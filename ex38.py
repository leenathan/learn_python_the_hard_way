# Originally done 17 Feb 2017

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one) #Append next one to stuff. Could also be append(stuff, next_one), i think,
	print "Theres %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1];
print stuff[-1] #Fancy!
print stuff.pop()
print ' '.join(stuff) #neat!
""" This takes the whole stuff array and slaps a ' ' between all the elements. Translation: Join stuff with ' ' in between.
Like join(' ',stuff) - "Call join with ' ' and stuff"

"""
print '#'.join(stuff[3:5]) #stellar!