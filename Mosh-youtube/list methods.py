numbers = [5, 2, 1 , 7, 4]
# append adds to the end of the list
numbers.append(13)
print(numbers)
# insert inserts a number into the specified spot
numbers.insert(2, 22)
print(numbers)
# removes from the list
numbers.remove(5)
print(numbers)
# clears out everything from the list
numbers.clear()
print(numbers)

numbers = [5, 2, 1 , 7, 4]
# removes the last item in the list
numbers.pop()
print(numbers)
# prints the index that the specified number is at
print(numbers.index(5))
# tells you true or false if the number is in the list
print(50 in numbers)

numbers = [5, 2, 1, 5, 7, 4]
# tells howe many times the object is in the list
print(numbers.count(5))
# sorts the list in ascending order
numbers.sort()
print(numbers)
# descending order
numbers.reverse()
print(numbers)
# copies the list to another variable
numbers2 = numbers.copy()
print(numbers2)