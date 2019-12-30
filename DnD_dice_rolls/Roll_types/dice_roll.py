"""
module that holds the different types of dice rolls.
"""
import random

number_of_dice = input("Number of dice: ")
dice_sides = input("Amount of sides: ")


class Dice:
    def sides20(self):  # Should this just be for one dice or also include 2+?
        if number_of_dice == 2:
            first_roll = random.randint(1, 20)
            second_roll = random.randint(1, 20)
            return first_roll, second_roll
        else:
            first_roll = random.randint(1, 20)
            return first_roll


dice = Dice()
print(dice.sides20())
