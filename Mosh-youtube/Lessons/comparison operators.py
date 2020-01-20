# if temperature is greater than 30
#   it's a hot day
# otherwise if it;s less than 10
#   it's a cold day
# otherwise
#   it's neither hot nor cold

temp = 35

if temp > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# ex
# if name is less than 3 characters long
#   name must be at least 3 characters
# otherwise if it;s more than 50 characters long
#   name can be a maximum of 50 characters
# otherwise
#   name looks good!

name = "Tyler"
print(len(name))

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long.")
else:
    print("Name looks good!")