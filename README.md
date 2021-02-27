# The Beatles Hangman
"The Beatles" themed interactive Hangman wordgame

Using data of Beatles lyrics from The Guardian’s datablog (https://www.theguardian.com/music/datablog/2010/nov/16/beatles-lyrics-words-music-itunes), I decided to add a twist to the interactive Hangman wordgame that I did for  MITx: 6.00.1x “Introduction to Computer Science and Programming Using Python” course.

For this “The Beatles Hangman” game, the second player will be the computer, who will be picking a word at random. The user has 8 guesses and with each guess the computer will print out the result and remaining available characters. These are words found in The Beatles' lyrics, so we’ll see if you are a true fan! ;)

You can download the code and text file to start playing, but don't forget to put both files in the same folder so the program will load properly.
Have fun playing the game!

See below for a sample of a successful game...

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
I am thinking of a word that is 5 characters long.
------------
You have 8 guesses left.
Available characters: abcdefghijklmnopqrstuvwxyz-.'

Please guess a character: o
Oops! That character is not in my word: _ _ _ _ _ 
------------
You have 7 guesses left.
Available characters: abcdefghijklmnpqrstuvwxyz-.'

Please guess a character: f
Oops! That character is not in my word: _ _ _ _ _ 
------------
You have 6 guesses left.
Available characters: abcdeghijklmnpqrstuvwxyz-.'

Please guess a character: e
Good guess: _ _ e_ e
------------
You have 6 guesses left.
Available characters: abcdghijklmnpqrstuvwxyz-.'

Please guess a character: a
Oops! That character is not in my word: _ _ e_ e
------------
You have 5 guesses left.
Available characters: bcdghijklmnpqrstuvwxyz-.'

Please guess a character: n
Oops! That character is not in my word: _ _ e_ e
------------
You have 4 guesses left.
Available characters: bcdghijklmpqrstuvwxyz-.'

Please guess a character: r
Good guess: _ _ ere
------------
You have 4 guesses left.
Available characters: bcdghijklmpqstuvwxyz-.'

Please guess a character: m
Oops! That character is not in my word: _ _ ere
------------
You have 3 guesses left.
Available characters: bcdghijklpqstuvwxyz-.'

Please guess a character: h
Good guess: _ here
------------
You have 3 guesses left.
Available characters: bcdgijklpqstuvwxyz-.'

Please guess a character: t
Oops! That character is not in my word: _ here
------------
You have 2 guesses left.
Available characters: bcdgijklpqsuvwxyz-.'

Please guess a character: e
Oops! You've already guessed that character: _ here
------------
You have 2 guesses left.
Available characters: bcdgijklpqsuvwxyz-.'

Please guess a character: t
Oops! You've already guessed that character: _ here
------------
You have 2 guesses left.
Available characters: bcdgijklpqsuvwxyz-.'

Please guess a character: w
Good guess: where
------------
Congratulations, you are a true fan!
```
