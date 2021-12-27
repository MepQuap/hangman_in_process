import random
from words_list import word_list
from all_functions import generate_display, pick_the_word, checking_letter, update_display
from all_functions import display_start_game,  restart_game
from hangman_art_list import logo, stages

import os

level_list = ["1", "2", "3", "4", "5", "exit"]

program_status = True


while program_status:

    game_is_finished = False
    user_lives = len(stages) - 1
    display = []
    all_guess_letters = ""

    print(logo)
    user_level = display_start_game()

    if user_level not in level_list:
        print("Invalid enter. Please enter 1, 2, 3, 4, or 5: ")
        continue
    if user_level == "5" or user_level == "exit":
        print(f"You enter {user_level} for exiting the game. Good bye.")
        program_status = True
        break

    while not game_is_finished:

        chosen_word = pick_the_word(user_level).lower()
        word_length = len(chosen_word)

        os.system("clear")
        # Testing code
        print(
            f'Pssst, the solution is {chosen_word} & word lenght is {word_length}')

        display = generate_display(chosen_word, word_length)

        while user_lives > 0:

            guess = input("Guess a letter: ")

            # checking guessing letter is a character or not.
            if not guess.isdigit():
                if guess in all_guess_letters:
                    print(f"You already enter this {guess} letter.")
                    continue

                if checking_letter(chosen_word, guess):
                    update_display(display, guess, chosen_word)
                    all_guess_letters.join(guess)
                else:
                    update_display(display, guess, chosen_word)
                    all_guess_letters.join(guess)
                    user_lives -= 1
            else:
                print("Invalid enter. Please enter character/letter.")
                continue

            print(stages[user_lives])

        if user_lives == 0:
            game_is_finished = True
            print("You lose")

        if "_" not in display:
            game_is_finished = True
            print("You win.")

        replay = input("Would you like to play again? Y/N : ")
        game_is_finished = restart_game(replay.lower(), game_is_finished)
        if not game_is_finished:
            print("Restarting the game")
            user_lives = len(stages) - 1
            display = []
            all_guess_letters = ""
        else:
            program_status = False
            break
