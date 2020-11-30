"""
This is a 1 player dice game played against the computer
"""

import random


class UserInput:
    def __init__(self):
        self.number_of_rolls = 0

    @staticmethod
    def request_to_play():
        play = input('Would you like to play a dice game?\nEnter \'yes\' to play.\n')
        if 'yes' in play:
            return True
        else:
            return False

    def set_number_of_rolls(self):
        self.number_of_rolls = int(input('How many rolls would you like to have in this game?\n'))
        return self.number_of_rolls

    def roll_the_die(self):
        player = Player()
        enter = input('It\'s your roll! Key enter to toss the die.\n')
        if '' in enter:
            return player.take_a_turn()
        else:
            raise TypeError('Only use the enter key to take your turn.')


class Player:
    def __init__(self):
        self.player = 0
        self.computer = 0

    def take_a_turn(self):
        player = DieRoll().return_roll()
        computer = DieRoll().return_roll()
        self.calculate_winner_from_this_round(player, computer)

        return player, computer

    def calculate_winner_from_this_round(self, player, computer):
        if player > computer:
            self.player += 1
        elif computer > player:
            self.computer += 1
        else:
            pass

    def get_total_scores(self):
        return self.player, self.computer

    def get_winner_of_game(self):
        if self.player > self.computer:
            return self.player
        elif self.computer > self.player:
            return self.computer
        else:
            return 'Draw'


class DieRoll:
    def __init__(self):
        self.roll = random.randint(1, 6)
        self.return_roll()

    def return_roll(self):
        return self.roll


def main():
    start = UserInput()
    if start.request_to_play() is False:
        exit()
    num = start.set_number_of_rolls()
    pass
    start.roll_the_die()


if __name__ == '__main__':
    main()
