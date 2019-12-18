# if there is something inside the parentheses, there needs to be a parameter when the function is called later
def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}!")
    print('Welcome aboard.')


print("Start")
# calls the function with 2 parameters
greet_user("Tyler", "Tamalunas")
greet_user("Mary", "Sue")
print("Finish")
