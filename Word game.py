# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string
import math

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

#you'll need to change this adress to wherever you stored your word list. 
#you can copy and paste a wordlist I uploaded in this repository. 
WORDLIST_FILENAME = "C:\Users\DELL\Desktop\Luis Angel\Programming\Python\Word Game\ProblemSet4\ProblemSet4\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    word = word.lower()
    points = 0
    for i in word:
        points += SCRABBLE_LETTER_VALUES[i]
    points *= len(word)
    if len(word) == n:
        points += 50
    return points
    #




#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                               # print an empty line
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        #print hand
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]       
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    word = word.lower()
    hand2 = hand.copy()
    for i in word:
        hand2[i] = hand2.get(i, 0) -1
    return hand2

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    validword = ''
    hand2 = hand.copy()
    for i in word:
        hand2[i] = hand2.get(i, 0)-1
        #print hand2   
    for i in hand2:
        if hand2[i] < 0:
            validword = False
            break
    return word in wordList and validword != False

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    total = 0
    for i in hand:
        total += hand[i]
    return total


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    pointsTotal = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print 'Current Hand: ',
        displayHand(hand)
        #print str(y)
        #print (displayHand(hand))
        # Ask user for input
        x = str(raw_input('Enter word, or a "." to indicate that you are finished: '))
        # If the input is a single period:
        if x == '.':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else: 
            # If the word is not valid:
            if isValidWord(x, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print 
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                points = getWordScore(x, n)
                pointsTotal += points
                print '"' + str(x) + '"' + ' earned ' + str(points) +  ' points. Total: ' + str(pointsTotal) + ' points.' 
                print
                # Update the hand 
                hand = updateHand(hand, x)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if x == '.':
        print 'Goodbye! Total score: ' + str(pointsTotal)
    elif calculateHandlen(hand) == 0:
        print 'Ran out of letters. Total score: ' + str(pointsTotal) + ' points.'
    return pointsTotal #this is for playing against AI
    

#
# Problem #5: Playing a game
# 

def playGame(wordList): #wordList se reemplzada por loadWords() ?
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    currentHand = 0
    x = 0
    while x != 'e': #while the user doesn't exit
        x = str(raw_input("Enter 'n' to deal a new hand, 'r' to replay the last hand, or 'e' to end game: "))
        if x == 'e':
            break
        elif x in ('r', 'n'):
            y = str(raw_input("Enter 'me' to play with yourself or 'c' to play with the computer: "))
            if y == 'me': #if he wants to play alone, he plays
                if x == 'n':
                    currentHand = dealHand(HAND_SIZE)
                    playHand(currentHand, wordList, HAND_SIZE)
                elif x == 'r':
                    if currentHand == 0:
                        print 'You have not played a hand yet. Please play a new hand first!'
                    else:  
                        playHand(currentHand, wordList, HAND_SIZE)
                elif x != 'e':
                    print 'Invalid Command.'
            elif y == 'c': #if he wants to play with the computer, first he plays
                if x == 'n':
                    currentHand = dealHand(HAND_SIZE)
                    userPoints = playHand(currentHand, wordList, HAND_SIZE)
                    #userPoints = playHand(currentHand, wordList, HAND_SIZE)
                    print "Now it's my turn!"
                    print
                    #compPlayHand(currentHand, wordList, HAND_SIZE)
                    compPoints = compPlayHand(currentHand, wordList, HAND_SIZE)
                    print 'You scored ' + str(userPoints)
                    print 'The computer scored ' + str(compPoints)
                    if math.floor(userPoints) == math.floor(compPoints):
                        print "You tied! Try again and kick some ass!"
                    elif userPoints > compPoints:
                        print "You've won! Nice! Show them computers you know better!"
                    else:
                        print "Wops! The computer beat you! Don't let it stay that way."
                elif x == 'r':
                    if currentHand == 0:
                        print 'You have not played a hand yet. Please play a new hand first!'
                    else:  
                        userPoints = playHand(currentHand, wordList, HAND_SIZE)
                        compPlayHand(currentHand, wordList, HAND_SIZE)
                    print 'You scored ' + str(userPoints)
                    print 'The computer scored ' + str(compPoints)
                    if math.floor(userPoints) == math.floor(compPoints):
                        print "You tied! Try again and kick some ass!"
                    elif userPoints > compPoints:
                        print "You've won! Nice! Show them computers you know better!"
                    else:
                        print "Wops! The computer beat you! Don't let it stay that way."
                elif x != 'e':
                    print 'Invalid Command.'
            else:
                print 'Invalid Command.'
        else:
                print 'Invalid Command.'
                ###       
     #functions for computer AI#
             #begin#   
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.fo

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    count = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = 'None'
    # For each word in the wordList
    for i in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
       hand2 = hand.copy()
       validword = 0
       for j in i:
            hand2[j] = hand2.get(j, 0)-1     
       for k in hand2:
        if hand2[k] < 0:
            validword -= 1
       if validword == 0:    
            # Find out how much making that word is worth
            points = getWordScore(i, n)
            # If the score for that word is higher than your best score
            if points > maxScore:
                # Update your best score, and best word accordingly
                maxScore = points
                bestWord = i
                count += 1
                if count == 1:
                    break
    
    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    #mano = dealHand(n)
    points = 0
    while compChooseWord(hand, wordList, n) != 'None':    
        print "Computer's current hand: ", 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        print
        print 'The computer played: ' + word
        print 'The computer earned: ' + str(getWordScore(word, n)) + ' points.'
        points += getWordScore(word, n)
        print 'Total points: ' + str(points)
        hand = updateHand(hand, word)
        print 
    print 'Current hand: ',
    displayHand(hand)
    print
    print 'Total points: ' + str(points)
    return points
                ###       
     #functions for computer AI#
              #end#  
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
