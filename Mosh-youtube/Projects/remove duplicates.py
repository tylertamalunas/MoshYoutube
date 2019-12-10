# Write a program to remove duplicates in a list
list = [1, 1, 5, 14, 22, 22, 22, 11, 4, 5, 12, 7, 4, 44, 15]
uniques = []
# if the number isnt in the uniques list, it adds the number to the list, and then sorts it
for number in list:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)