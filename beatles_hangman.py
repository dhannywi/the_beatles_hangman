# Hangman game
#

# -----------------------------------

import random

WORDLIST_FILENAME = "beatles_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(letter in lettersGuessed for letter in secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
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
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
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
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('''
****************************************************
 _                _   _           
| |              | | | |          
| |__   ___  __ _| |_| | ___  ___ 
| '_ \ / _ \/ _` | __| |/ _ \/ __|
| |_) |  __/ (_| | |_| |  __/\__ \\           
|_.__/ \___|\__,_|\__|_|\___||___/   H A N G M A N

****************************************************
''')
    print('Hello Beatlemaniacs, welcome to the game!')
    print('I am thinking of a word that is', len(secretWord), 'characters long.')
    
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


# let's play!

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
