# if there is something inside the parentheses, there needs to be a parameter when the function is called later
def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}!")
    print('Welcome aboard.')


print("Start")
# calls the function with 2 parameters
greet_user("Tyler", "Tamalunas")
# the first_name= and last_name= are the keyword arguments. parameter order does not matter if using keyword arguments.
greet_user(last_name="Moraz", first_name="Sue")

# below is where keyword arguments are helpful,
# calc_cost(total=50, shipping=5, discount=0.1)
# keyword arguments must come AFTER positional arguments if both are used int he same line
# correct func(5, cost=12)
# wrong func(price=5, 12)
print("Finish")

