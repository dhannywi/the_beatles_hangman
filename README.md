# The Beatles Hangman
![The Beatles](https://github.com/dhannywi/the_beatles_hangman/blob/main/beatles_img.jpg)

The Beatles Hangman is "The Beatles" themed interactive Hangman wordgame.

Using Beatles lyrics data from [The Guardian’s datablog](https://www.theguardian.com/music/datablog/2010/nov/16/beatles-lyrics-words-music-itunes), I decided to add a twist to the interactive Hangman wordgame that I did for  MITx: 6.00.1x “Introduction to Computer Science and Programming Using Python” course.

For this “The Beatles Hangman” game, the second player will be the computer, who will be picking a word at random. The user has 8 guesses and with each guess the computer will print out the result and remaining available characters. These are words found in The Beatles' lyrics, so we’ll see if you are a true fan! ;)

You can download the code and text file to start playing, but don't forget to put both files in the same folder so the program will load properly.
Have fun playing the game!

A successful game will look similar to the example below:

```
Loading word list from file...
   1175 words loaded.

****************************************************
 _                _   _           
| |              | | | |          
| |__   ___  __ _| |_| | ___  ___ 
| '_ \ / _ \/ _` | __| |/ _ \/ __|
| |_) |  __/ (_| | |_| |  __/\__ \           
|_.__/ \___|\__,_|\__|_|\___||___/   H A N G M A N

****************************************************

Hello Beatlemaniacs, welcome to the game!
I am thinking of a word that is 7 characters long.
------------
You have 8 guesses left.
Available characters: abcdefghijklmnopqrstuvwxyz-.'

Please guess a character: a
Good guess: _ _ _ _ _ a_ 
------------
You have 8 guesses left.
Available characters: bcdefghijklmnopqrstuvwxyz-.'

Please guess a character: e
Oops! That character is not in my word: _ _ _ _ _ a_ 
------------
You have 7 guesses left.
Available characters: bcdfghijklmnopqrstuvwxyz-.'

Please guess a character: t
Good guess: _ _ _ t_ a_ 
------------
You have 7 guesses left.
Available characters: bcdfghijklmnopqrsuvwxyz-.'

Please guess a character: m
Good guess: _ _ _ tma_ 
------------
You have 7 guesses left.
Available characters: bcdfghijklnopqrsuvwxyz-.'

Please guess a character: i
Oops! That character is not in my word: _ _ _ tma_ 
------------
You have 6 guesses left.
Available characters: bcdfghjklnopqrsuvwxyz-.'

Please guess a character: w
Oops! That character is not in my word: _ _ _ tma_ 
------------
You have 5 guesses left.
Available characters: bcdfghjklnopqrsuvxyz-.'

Please guess a character: h
Oops! That character is not in my word: _ _ _ tma_ 
------------
You have 4 guesses left.
Available characters: bcdfgjklnopqrsuvxyz-.'

Please guess a character: s
Good guess: _ _ stma_ 
------------
You have 4 guesses left.
Available characters: bcdfgjklnopqruvxyz-.'

Please guess a character: k
Oops! That character is not in my word: _ _ stma_ 
------------
You have 3 guesses left.
Available characters: bcdfgjlnopqruvxyz-.'

Please guess a character: o
Good guess: _ ostma_ 
------------
You have 3 guesses left.
Available characters: bcdfgjlnpqruvxyz-.'

Please guess a character: h
Oops! You've already guessed that character: _ ostma_ 
------------
You have 3 guesses left.
Available characters: bcdfgjlnpqruvxyz-.'

Please guess a character: p
Good guess: postma_ 
------------
You have 3 guesses left.
Available characters: bcdfgjlnqruvxyz-.'

Please guess a character: n
Good guess: postman
------------
Congratulations, you are a true fan!

```
