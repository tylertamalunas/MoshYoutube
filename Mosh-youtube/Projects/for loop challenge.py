# print the following using nested loops:
# xxxxx
# xx
# xxxxx
# xx
# xx

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    out = ''
    for count in range(x_count):
        out += 'x'
    print(out)

print('\n')

numb = [2, 2, 2, 2, 7]
for l in numb:
    line = ''
    for item in range(l):
        line += 'x'
    print(line)