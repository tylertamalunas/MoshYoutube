"""
This is the file to call upon when rolling dice
User inputs which dice they are rolling and how many, and then this calls the correct function to roll
the dice and show the player their roll.
"""
import random
from Roll_types.dice_roll import Dice

number_of_dice = input("Number of dice: ")
dice_sides = input("Amount of sides: ")


dice = Dice.sides20()
if dice_sides == 20:
    print(dice)
