# find the largest number in a list
numbers = [1, 5, 12, 2, 155, 16, 22, 3, 77]
max = numbers[0]
for item in numbers:
    if max <= item:
        max = item
print(max)
