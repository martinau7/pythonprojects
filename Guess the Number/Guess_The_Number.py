"""
The number guessing game
"""

import random

total_attempts = []


def show_score():
    if not total_attempts:
        print('Currently, a high score hasn\'t been achieved, be the first one!')
    else:
        print(f'The current high score is {min(total_attempts)} attempts')


def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print('Hello and welcome to the number guessing game')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, Would you like to play the guessing game?'
        '(Enter Yes/No): ')
    if wanna_play.lower() != 'yes':
        print('No worries, have a nice day! ')
    else:
        show_score()
    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number from 1 to 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please insert a number from the given range above. ')
            attempts += 1
            total_attempts.append(attempts)

            if guess == rand_num:
                print('Nice, you guessed the correct number! ')
                print(f'It took you {attempts} attempts')
                wanna_play = input('Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s fine, have a good one! ')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower ')
                elif guess < rand_num:
                    print('It\'s higher')
        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again.. ')
            print(err)


if __name__ == '__main__':
    start_game()
