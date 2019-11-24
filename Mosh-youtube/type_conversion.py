birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

# now for my own
#Ask a user their weight (in pounds), convert it to kilograms and print on the terminal
weight = input('How many pounds do you weigh? ')
kilos = 0.454 * int(weight)
print(weight + ' pounds is the same as ' + str(kilos) + ' kilograms.')