"""
A dice game.

"""

from random import randint
from time import sleep

# list for counting wins/losses/ties
#human_wins = []


def get_number_of_rolls():
    return int(input("How many rolls would you like to play?\n"))


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

# main logic for determining winner
def compare_list_positions(wins):

    if wins[0] > wins[1]:
        print('You win!')
        #human_wins.append(1)
    elif wins[0] > wins[1]:
        print('Computer win!')
        #human_wins.append(0)
    else:
        print('Tie!')
        #human_wins.append(None)


def main():
   rolls = get_number_of_rolls() * 2
   score = []

   while rolls > 0:
        if rolls % 2 == 0:
            turn = dice_turn('You')
            score.append(turn)
        else:
            turn = dice_turn('computer')
            score.append(turn)
            compare_list_positions(score)
            score = []
        sleep(1)
        rolls -= 1

    #print(human_wins)


if __name__ == '__main__':
    main()
