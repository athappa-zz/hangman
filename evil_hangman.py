#!/usr/bin/env python 

'''
Evil Hangman


Hat Tip: http://nifty.stanford.edu/2011/schwarz-evil-hangman/Evil_Hangman.pdf
'''

from collections import Counter
import sys

prompt = '>>> '
value_error_msg = 'Please pick a number.'

#Take .txt and add all the words from it into a list
with open('dictionary.txt', 'r') as f:
	dictionary = [line.strip() for line in f]




######################
##### User Inputs
######################

#Introduction to the game
raw_input("Welcome to Hangman! Press <Enter> to continue...")

#Add instructions
while True:
	print("Do you want the instructions for how to play sticks? Y/N")
	instructions_ans = raw_input(prompt)

	if instructions_ans.upper() == 'Y':
		print '''
		Add instructions for how to play Hangman
		'''
		break

	elif instructions_ans.upper() == 'N':
		break

	else:
		print "Please answer with a Y or N."

#Prompt for word length
while True:
	try:
		print("What word length would you like to use?")
		word_length = int(raw_input(prompt))

		if 4<=word_length<=20:
			print ("Ok, we are looking for words of length %s.") % (word_length)
			break
		elif word_length < 4:
			print ("Please pick a longer word length.")
		elif word_length > 20:
			print ("Please pick a shorter word length.")

	except ValueError:
		print value_error_msg

#Prompt for number of guesses
while True:
	try:
		print("How many chances do you want?")
		num_guesses = int(raw_input(prompt))

		if num_guesses < 0:
			print ("You have %s chances.") % (num_guesses)
		elif num_guesses < 0:
			print ("Pick a positive number")
		elif num_guesses == 0:
			print ("Pick a non-zero, positive number.")

	except ValueError:
		print value_error_msg

#Running total of the number of words in the word list




######################
##### End User Inputs
######################




#Input: List of words
#Output: Dictionary of form {'Word': [('length',x),('w',1),('o',1),('r',1),('d',1)]}
#Issue to solve: It double counts letters that appear more than once

dictionary = {}
def add_to_dictionary(list_of_words):


	for word in list_of_words:
		if word not in dictionary:
			dictionary[word] = {}
			dictionary[word] = [('length',len(word))]

		for letter in word:

			dictionary[word].append((letter, word.count(letter)))



			#letter_count = Counter()


			#dictionary[
		#x, list_of_words.count(x)
	return dictionary

add_to_dictionary(dictionary)


dictionary_subset = {k, dictionary[k]) if k[0][1] == word_length)



subset = {key:value for key, value in dict.items() if dict[key][0][1] == word_length}

#subset = {key:value for key, value in dict.items if value[0][1] == 7}














