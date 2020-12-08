"""
A dice game.

"""

from random import randint


def get_number_of_roles():
    return int(raw_input("How many roll would you like to play?\n"))


def roll_the_die():
    return randint(0, 6)

class Game:

    def __init__(self, rolls, winner=0):
        self.rolls = rolls
        self.winner = winner


def main():
    rolls = get_number_of_roles()

    play = Game(rolls,)
