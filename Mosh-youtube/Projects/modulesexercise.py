# original code
#numbers = [10, 3, 6, 2]
#max = numbers[0]
#for number in numbers:
#    if number > max:
#        max = number
#print(max)


# write a function called find_max()
# takes a list and returns largest number in list
# put function in separate module called utils
# import utils into current module and call the function
# get result and print to terminal

import utils

numbers = [10, 3, 6, 2]
print(utils.find_max(numbers))
