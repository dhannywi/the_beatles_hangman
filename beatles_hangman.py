#!/usr/bin/env python3

import random

WORDLIST_FILENAME = "beatles_words.txt"

def loadWords():
    """
    Loads words from a file, returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    Args:
        None
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
    Function checks user's guess against the secret word, and return boolean value.
    Args:
    	secretWord (str): The word the user is guessing.
    	lettersGuessed (list): What letters have been guessed so far.
    Returns:
        result (bool): True if all the letters of secretWord are in lettersGuessed; False otherwise.
    """
    return all(letter in lettersGuessed for letter in secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    Function checks user's guess against secret word, and return what was guessed so far as a string.
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
    Function iterates through a list of guessed letters and returns remaining letters available for guessing.
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

def hangman(secretWord):
    '''
    Function 
    Args:
	secretWord (string): The secret word to guess.
    Returns:
	result (str): Current state of the game.
    '''
    # count lives
    mistakesMade = 0
    lettersGuessed = []

    # game start!
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you are a true fan!')
            break
        else:
            print('------------')
            print('You have', 8 - mistakesMade, 'guesses left.')
            print('Available characters:', getAvailableLetters(lettersGuessed))
            guess = str(input('Please guess a character: ')).lower()
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that character:", getGuessedWord(secretWord, lettersGuessed))
            elif guess not in secretWord:
                print("Oops! That character is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesMade += 1
        if 8 - mistakesMade == 0:
            print('------------')
            print('Sorry, you ran out of guesses. The word was: ', secretWord)
            break
        else:
        	continue

def main():
    '''
    Starts up an interactive game of Hangman.
    * At the start of the game, lets the user know how many letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user receives feedback immediately after each guess about whether their guess appears in the computers word.
    * After each round, program displays to the user the partially guessed word so far, 
      as well as letters that the user has not yet guessed.
    '''
    wordlist = loadWords()

    # let's play!
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

    hangman(secretWord)

if __name__ == '__main__':
    main()
