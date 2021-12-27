from words_list import word_list, easy_words_list, medium_words_list, hard_words_list
import random


def checking_integer(input_value):
    if input_value.isdegit():
        return True
    else:
        return False


def display_start_game():
    """Printing start msg."""
    print("Welcome to Hangman Game. There are three levels available;")
    print("Easy level (4-5 letters) enter 1")
    print("Medium level (6 letters) enter 2")
    print("Hard level (7 letters) enter 3")
    print("Random level enter 4")
    print("You can quit the game anytime with '5'.")
    user_level = input("Please choosing game level: ")
    return user_level


def pick_the_word(level):
    """ using random function to pick word from list """

    if level == "1":
        chosen_word = random.choice(easy_words_list)
        # word_length = len(chosen_word)
    elif level == "2":
        chosen_word = random.choice(medium_words_list)
        # word_length = len(chosen_word)
    elif level == "3":
        chosen_word = random.choice(hard_words_list)
        # word_length = len(chosen_word)
    elif level == "4":
        chosen_word = random.choice(word_list)

    return chosen_word


def generate_display(word, word_length):
    """ At starting of the game replace each letter from guessing word with '_' and display to user. """
    display = []
    for position in range(word_length):
        display.append('_')
    print(f"{' '.join(display)}")
    return display


def update_display(display, user_guess, correct_word):
    """replacing '-' with correct letter into guessing word"""
    word_length = len(correct_word)
    for position in range(word_length):
        letter = correct_word[position]
        if letter == user_guess:
            display[position] = letter
    print(f"{' '.join(display)}")


# def show_letters(display, user_guess, word_length, guess_right):
#     if guess_right:
#         for position in range(word_length):
#             letter = display[position]ƒ√
#             display[position] = letter
#         print(f"{' '.join(display)}")
#     else:
#         for position in range(word_length):
#             print(f"{' '.join(display)}")


def checking_letter(word, user_guess):
    """Checking user guess letter with main guessing word. """

    if user_guess in word:
        print(f"You've entered: {user_guess}. It's correct.")
        return True
    else:
        print(
            f"You guessed {user_guess}, that's not in the word. You lose a life.")
        return False


def restart_game(user_decistion, replay):
    if user_decistion == 'y' or user_decistion == 'yes':
        print("restart the game")
        replay = False
        return replay
    elif user_decistion == 'n' or user_decistion == 'no':
        print("Good bye!")
        replay = True
        return replay
    else:
        print("invalid value")
