# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
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
    letters_of_secretWord = []
    for l in secretWord:
        if l not in letters_of_secretWord:
            letters_of_secretWord.append(l)
    letters_well_guessed = []
    for letter in letters_of_secretWord:
        if letter in lettersGuessed:
            letters_well_guessed.append(letter)

    return len(letters_well_guessed) == len(letters_of_secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            print(letter, end=' ')
        else:
            print(' _ ', end=' ')


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_left = ''
    availableLetters = string.ascii_lowercase
    for letters in availableLetters:
        if letters not in lettersGuessed:
            letters_left += letters
    return letters_left


def hangman(secretWord):
    '''
    secretWord: a string
    The user has to guess the secretWord letter by letter. If the guess is wrong s/he loses a life,
    if the guess is right, the guessed letter will be displayed.

    At the start of the program lets the user know the number of letters of the secretWord.
    After every guess, the program shows the updated set of letters which were not guessed yet.
    At the and of the game the user has the possibility to restart the game.
    '''
    lettersGuessed = []
    lives = 8
    print('Welcome to the Game of Hangman')
    print('The Secret Word contains', len(secretWord), 'letters.')
    while isWordGuessed(secretWord, lettersGuessed) == False and lives > 0:
        print('\nAvailable letters:', getAvailableLetters(lettersGuessed))
        x = input('Please guess a letter: ')
        if x not in lettersGuessed:
            lettersGuessed.append(x)
        else:
            print('You already entered this letter. Please enter another one.')
        getGuessedWord(secretWord, lettersGuessed)
        if x not in secretWord:
            lives -= 1
            print('\nWrong guess. The number of lives left:', lives )
    if isWordGuessed(secretWord, lettersGuessed) == True:
        ans = input('Congratulations! You win!\nIf you want to play another game press "y".')
        if ans == 'y':
            hangman(secretWord)
    if lives == 0:
        print('Game Over. The Secret Word was: ' + secretWord + '.')
        if input('If you want to play another game press "y". ') == 'y':
            hangman(secretWord)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

