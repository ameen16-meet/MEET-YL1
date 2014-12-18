def palindrome(word):
	b = word [::-1]
	if (word == b):
		print('PALINDROME')
	else:
		print('Thank you, come again.')
word=input("enter a word")
palindrome(word)