#Ex25: Even more practice
#re-re-done 4 Oct 2015

"""This does not consider capitalization. Capitalized letters throw off the sorting function, I believe."""

def break_words(stuff):
	"""This function will break up words for us.\n
	Is this how you distinguish help? Yes, use \"\"\" for help dialog!"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	"""prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words and then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)	
	
