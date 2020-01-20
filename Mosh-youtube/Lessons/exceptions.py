# try makes it so that you can have the interpreter not show the normal error message, and instead print out a string
# that the creator sets
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')