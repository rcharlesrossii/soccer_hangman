import random

def game_word():
    """A list of soccer related words is created to be used in the game.

    Returns a randomly selected word from the list of soccer related words.
    """
    word_bank = ['advantage', 'assist', 'chip', 'clear', 'cleat', 'corner', 
'cross', 'crossbar', 'defender', 'dribble', 'football', 'forward', 'goal', 
'goalie', 'halftime', 'handball', 'header', 'keeper', 'linesman', 'match', 
'midfield', 'nutmeg', 'offside', 'pass', 'penalty', 'referee', 'shot', 
'soccer', 'striker', 'sweeeper','tackle', 'volley', 'wing']
    word = random.choice(word_bank)
    return word

def play_game(word):
    """Ask the user to input a letter to be guessed in the game.

    The letter will eitehr be in the word, not in the word, or already guessed.

    Args:
        word (str): This is the word that you are trying to guess in the game.
    """
    guessed = False
    incorrect_attempts = 6
    guessed_letters = []
    word_completion = '_' * len(word)
    print('Welcome to Hangman Soccer Edition!')
    print("(HINT: The words are soccer related and you only are allowed 6 incorrect guesses.)")
    print(display_hangman(incorrect_attempts))
    print(word_completion)
    print("\n")

    while not guessed and incorrect_attempts > 0:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"The letter '{guess}' has already been guessed. Please guess a different letter.")
            elif guess not in word:
                print(f"The letter '{guess}' is not in the word.")
                incorrect_attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"The letter '{guess}' is in the word. Good guess!")
                guessed_letters.append(guess)
                #Create a list of the correct letters guessed in the word
                word_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                #Convert the list back into a string
                word_completion = ''.join(word_list)
                if '_' not in word_completion:
                    guessed = True
        else:
            print("Please enter a single letter guess.")
        print(display_hangman(incorrect_attempts))
        print(word_completion)
        print("\n")
    if guessed:
        print(f"Wow, you guessed the word '{word}' correctly!")
    else:
        print(f"Sorry you did not guess the word. The word was '{word}'.")


def display_hangman(incorrect_attempts):
    """This function uses the number of incorrect attempts remaining to

    determine what to display to the player.

    Args:
        incorrect_attempts (int): The number of incorrect attempts remaining for player.
    """

    stages = {
         0: """
                ___________
               | /        | 
               |/       _( )_
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )_
               |          |
               |         / \\
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |           \\
               |
            """,
        4: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        5: """
                ___________
               | /        |
               |/        ( )
               |          
               |          
               |
            """,
        6: """
                ___________
               |          |
               |
               |
               |
               |
            """
    }
    return stages[incorrect_attempts]


def main():
    play_again = True
    while play_again:
        word = game_word()
        play_game(word)
        response = input("Would you like to play again? (yes/no) ")
        if response == 'yes':
            play_again = True
        elif response == 'no':
            play_again = False
            print("Thank you for playing!")
        else:
            print("I'll take that as a no. Sorry to ask...")
            play_again = False
    
    
if __name__ == "__main__":
    main()
