#!/usr/bin/env python3

# Hangman game
import random

WORDLIST_FILENAME = "beatles_words.txt"

def loadWords():
    """
    Loads words from a file, returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
	
	Returns:
		wordlist (list): list of words (str).
    """
    print("\nLoading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(f"... {len(wordlist)} words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
	Iterates through a list of words, returns a word from wordlist at random.

	Args:
    	wordlist (list): list of words (str).
	Returns:
		result (str): a random word.
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    """
	Args:
    	secretWord (str): The word the user is guessing.
    	lettersGuessed (list): What letters have been guessed so far.
    Returns:
		result (bool): True if all the letters of secretWord are in lettersGuessed; False otherwise.
    """
    return all(letter in lettersGuessed for letter in secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''
	Args:
    	secretWord (str): The word the user is guessing
    	lettersGuessed (list): The letters that have been guessed so far
    Returns:
		result (str): Comprised of letters and underscores that represents
      				  what letters in secretWord have been guessed so far.
    '''
    wordGuessed = []
    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuessed.append(letter)
        else:
            wordGuessed.append('_ ')
    return ''.join(wordGuessed)

def getAvailableLetters(lettersGuessed):
    '''
	Args:
    	lettersGuessed (list): The letters that have been guessed so far
    Returns:
		result (str): Comprised of letters that represents what letters have not
      				  yet been guessed.
    '''
    string = "abcdefghijklmnopqrstuvwxyz-.'"
    alphabet = []
    
    for e in string.lower():
        alphabet.append(e)        
    
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet.remove(letter)
    
    return ''.join(alphabet)

def hangman(secretWord, lettersGuessed):
	'''
	Args:
		secretWord (string): The secret word to guess.
	Returns:
		result (str): Current state of the game.
	'''
	lives = 8
	while lives > 0:
		print(f'{"-"*25}\nYou have {lives} guesses left.')
		print(f'Available characters: {getAvailableLetters(lettersGuessed)}')
		guess = str(input('Please guess a character: ')).lower()
		if isWordGuessed(secretWord, lettersGuessed) == False:
			if guess in secretWord and guess not in lettersGuessed:
				lettersGuessed.append(guess)
				print(f'Good guess: {getGuessedWord(secretWord, lettersGuessed)}')
			elif guess in lettersGuessed:
				print(f"Oops! You've already guessed that character: {getGuessedWord(secretWord, lettersGuessed)}")
				lettersGuessed.append(guess)
			elif guess not in secretWord:
				print(f'Oops! That character is not in my word: {getGuessedWord(secretWord, lettersGuessed)}')
				lettersGuessed.append(guess)
				lives -= 1
			
def game_result(secretWord, lettersGuessed):
	'''
	Takes in the word user is gussing and a list of guessed characters, returns the result of the game.
	Args:
		secretWord (str): The word the user is guessing.
		lettersGuessed (list): A list of letters the user guessed.
	Returns:
		result (str): The game results.
	'''
	if isWordGuessed(secretWord, lettersGuessed) == False:
		return f'{"-"*25}\nSorry, you ran out of guesses. The word was: {secretWord}'
	else:
		return f'{"-"*25}\nCongratulations, you are a true fan!'

def main():
	'''
	Starts up an interactive game of Hangman.
	* At the start of the game, lets the user know how many letters the secretWord contains.
	* Ask the user to supply one guess (i.e. letter) per round.
	* The user receives feedback immediately after each guess about whether their guess appears in the computers word.
	* After each round, program displays to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
	'''
	wordlist = loadWords()

	# let's play!
	lettersGuessed = []
	secretWord = chooseWord(wordlist).lower()
	print(f'''
****************************************************
 _                _   _           
| |              | | | |          
| |__   ___  __ _| |_| | ___  ___ 
| '_ \ / _ \/ _` | __| |/ _ \/ __|
| |_) |  __/ (_| | |_| |  __/\__ \           
|_.__/ \___|\__,_|\__|_|\___||___/   H A N G M A N

****************************************************

Hello Beatlemaniacs, welcome to the game!
I am thinking of a word that is {len(secretWord)} characters long.
	''')

	hangman(secretWord, lettersGuessed)
	game_result(secretWord, lettersGuessed)

if __name__ == '__main__':
	main()
