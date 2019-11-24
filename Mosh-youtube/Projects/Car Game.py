# Car Game!
# Ask for the user input. They can type Help to see what commands are available. The options are start, stop, quit.
# start starts the car. if car is already start say something else
# Stop stops the car. if car already stopped say something different
# Quit ends the program. ignore the case of the letter that the user inputs.
user_input = ""
car_is_on = False

while True:
    # make anything the user inputs into lower case so that it is not case sensitive
    user_input = input('>').lower()
    # when user types help
    if user_input == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    # when the user types start and the car is not turned on already
    elif user_input == 'start' and car_is_on is False:
        print("You hear the engine rumble to life!")
        car_is_on = True
    # when the user types start and the car is already turned on
    elif user_input == 'start' and car_is_on is True:
        print("It's already on, why would you try to turn it on again?")
    # when the user types stop and the car is turned on
    elif user_input == 'stop' and car_is_on is True:
        print("You turned the car off.")
        car_is_on = False
    # when the user types stop and the car is already off
    elif user_input == 'stop' and car_is_on is False:
        print("That didn't do anything...the car seems to already be off.")
    # when quit is typed, the program ends
    elif user_input == 'quit':
        break
    # if the user types anything other than help, start, stop, or quit
    else:
        print("I don't understand that can you try again? Type 'help' if you don't know what to do.")
