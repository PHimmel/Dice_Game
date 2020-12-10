"""
A dice game.

"""

from random import randint
from time import sleep

# sets up counter variables
human_win = 0
comp_win = 0


def get_number_of_rolls():
    return int(input("How many rolls would you like to play?\n"))


def roll_the_die():
    return randint(0, 5) + 1


def dice_turn(user):
    turn = roll_the_die()
    print('{} rolled a {}'.format(user, turn))
    return turn


def determine_round_winner(human, comp):

    if human > comp:
        global human_win
        human_win += 1
        print('You win!\n--------------------')

    elif comp > human:
        global comp_win
        comp_win += 1
        print('Computer wins!\n--------------------')

    else:
        print('Tie!\n--------------------')


def determine_game_winner():
    if human_win > comp_win:
        print('\nThe human won!\n')
    elif comp_win > human_win:
        print('\nThe computer won!\n')
    else:
        print('Tie Die!')


def main():
    rolls = get_number_of_rolls() * 2

    while rolls > 0:
        if rolls % 2 == 0:
            human = dice_turn('You')
            sleep(1)
        else:
            comp = dice_turn('Computer')
            sleep(1)
            determine_round_winner(human, comp)

        rolls -= 1

    sleep(2)
    determine_game_winner()


if __name__ == '__main__':
    main()
