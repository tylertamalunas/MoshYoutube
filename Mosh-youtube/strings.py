# cant use single on this
# course = 'Python's Course for Beginners'
course = "Python's Course for Beginners"
print(course)

#also
course2 = 'Python for "Beginners"'
print(course2)

# multi line string
course3 = '''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
print(course3)

# specific part of string
# negatives start from the end
course4 = 'Python for Beginners'
print(course4[-2])
#for a range separate with 0:4
#it will exclude the last one
print(course4[0:4])
#using the format of 0: will make it print all from the specified character on
print(course4[3:])
# if you exclude the first number :5 it will print all before the specified number
print(course4[:5])
# if both are exluded [:] it prints the whole string
another = course4[:]
print(another)

# example ; what will print?
name = 'Jennifer'
print(name[1:-1])