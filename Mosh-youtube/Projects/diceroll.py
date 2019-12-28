"""
Exercise to generate random dice rolls. 2 dice. class called dice, method called roll. every time roll is called it
makes a tuple.

"""
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # don't need to write (first, second) to let it know its a tuple


dice = Dice()  # create an object of the Dice() type
print(dice.roll())
