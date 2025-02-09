import random

MISS = '-'  # _-.: letter not found ⬜
MISSPLACED = 'O'  # O, ?: letter in wrong place 🟨
EXACT = 'X'  # X, +: right letter, right place 🟩

WORD_LENGTH = 5
MAX_ATTEMPTS = 6

# Sets path for all words and target words
ALL_WORDS = 'all_words.txt'
TARGET_WORDS = 'target_words.txt'

def play():
    """Code that controls the interactive game play"""

    # select a word of the day:
    word_of_the_day = get_target_word()

    # build a list of valid words (words that can be entered in the UI):
    valid_words = get_valid_words()

    # sets attempts and score to 0
    attempts = 0
    score = 0

    while attempts < MAX_ATTEMPTS and score == 0:

        # Sets remaining attempts
        remaining_attempts = MAX_ATTEMPTS - attempts

        # Removes an attempt
        attempts = attempts + 1  

        # Informs user how many attempts they have left.
        print("\nYou have " + str(remaining_attempts) + " guesses remaining.")      

        # Get the guess fromn the user
        user_word = ask_for_guess(valid_words)
        
        # Score the user's guess
        score = score_guess(user_word, word_of_the_day, score)

    # Determines win/loss, prints the word of the day    
    scoring_method(score, attempts, word_of_the_day)    
    
    return True

def play_again():
    try_again = input("\nDid you want to try again? Type 'Y' to keep playing! ")

    # If user enters 'Y', play again. If anything else, quit.
    if try_again.upper() == 'Y':
        return True
    else:
        return False
    

def get_valid_words():
    # Reads all words and creates a list
    valid_words = open(ALL_WORDS)
    valid_words = valid_words.read()
    VALID_WORDS = valid_words.split()
    
    return VALID_WORDS


def get_target_word():
    # Reads target_word.txt and creates a list
    word_bank = open(TARGET_WORDS)
    word_bank = word_bank.read()
    WORD_BANK = word_bank.split()
    
    # Chooses a target word from the word bank
    target_word = random.choice(WORD_BANK).upper()
    
    return target_word


def ask_for_guess(VALID_WORDS):

    # Creates a loop in case the user's input isn't valid
    while True:
        # Gets input from user
        user_word = input("What is your 5 letter word?\n")
        user_word = user_word.lower()
    
        # Does a check to see if the inputted word isn't a string, longer than 5 characters or isn't a real word.
        if not user_word.isalpha():
            print("Please enter a word.")
            continue
        elif len(user_word) > 5 or len(user_word) < 5:
            print("Please choose a 5 letter word.\n")
            continue
        elif user_word not in VALID_WORDS:
            print("This is not a real word.\n")
            continue

        # Returns the user word if it passes the checks
        else:
            user_word = user_word.upper()
            return user_word


def score_guess(user_word, word_of_the_day, score):
    hint = []
    # Checks to see if the user word matches the target word first. If it does, adds 1 to score (to print the correct message at the end).
    if user_word == word_of_the_day:
        score = 1
    for letter in range(5):
        # Checks if the letter in user input matches the letter in the word of the day.
        if user_word[letter] == word_of_the_day[letter]:
            hint.append('X')
        # Checks to see if the letter is correct but in the wrong index.
        elif user_word[letter] in word_of_the_day:
            hint.append('O')
        # If the letter is not in the word, it appends '-'.
        else:
            hint.append('-')

    # Capitalises user word and prints it above the hint output - makes it easier to read.
    print(user_word[0], user_word[1], user_word[2], user_word[3], user_word[4])
    print(' '.join(hint))
    hint.clear()
    
    return score

def scoring_method(score, attempts, word_of_the_day):
    # If the score equals 1, the person won. If not, they lost.
    if score == 1:
        print("\nCongratulations you won!")
        print(f"You got it in {attempts} attempt(s).")
    else:
        print("You didn't get the word, better luck next time.")
    
    # Prints what the word of the day was.
    print(f"The word was '{word_of_the_day}'!")

def clear():
    # Creates a function to add blank spaces to clear the console.
    clear = "\n"*50
    print(clear)

def rules():
    # Prints welcome message and rules.
    print("Welcome to the Word Guessing Game!")
    print("You have 6 attempts to guess the random 5 letter word.")
    print("You will get clues each guess to help you: \n\nX = Correct character in the correct spot.\nO = Correct character in the wrong spot. \n- = Character isn't contained in the target word.")
    print("\nGood luck!")

while True:
    # Display the rules
    rules()
    # Runs the main code to play the game
    play()
    restart = play_again()
    # Checks if the player wants to restart
    if restart == False:
        print("Thanks for playing!")
        quit()
    else:
        clear()