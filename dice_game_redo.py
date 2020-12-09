"""
A dice game.

"""

from random import randint
from time import sleep


def get_number_of_rolls():
    return int(raw_input("How many roll would you like to play?\n"))


def roll_the_die():
    return randint(0, 5) + 1


def dice_turn(user):
    turn = roll_the_die()
    print('{} rolled a {}'.format(user, turn))
    return turn

# class Game:
#
#     def __init__(self, rolls, winner=0):
#         self.rolls = rolls
#         self.winner = winner


def main():
    rolls = get_number_of_rolls() * 2

    while rolls > 0:
        if rolls % 2 == 0:
            user = 'You'
        else:
            user = 'Computer'
        number = dice_turn(user)

        sleep(1)
        rolls -= 1


if __name__ == '__main__':
    main()
