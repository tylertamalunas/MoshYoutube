"""
User inputs which dice they are rolling and how many, and then this calls the correct function to roll
the dice and show the player their roll.
D20, D12, D10, D8, D6, D4
"""
import random

number_of_dice = input("Number of dice: ")
dice_sides = input("Amount of sides: ")


class Dice:
    def d20(self):  # Should this just be for one dice or also include 2+?
        if number_of_dice == '2':  # maybe change to a while loop, while x <= number_of_dice
            first_roll = random.randint(1, 20)
            second_roll = random.randint(1, 20)
            return first_roll, second_roll
        else:
            first_roll = random.randint(1, 20)
            return first_roll


dice = Dice()
if dice_sides == '20':
    print(dice.d20())
