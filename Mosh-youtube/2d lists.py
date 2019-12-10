# 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# basically a list within a list
#matrix[0][1] = 20 # changes row 1 item 2 to from the value 2 to 20
#print(matrix[0][1]) # first [] is which row, second [] is the item in the row, so this is row 1 item 2
# prints out 20
for row in matrix:
    # row = a whole row
    for item in row:
        print(item)
        # nested loop to go through the whole row