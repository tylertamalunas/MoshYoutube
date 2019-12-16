# write code that will take user input number and convert to string words
# Phone: 1234
# output: One Two Three Four

# make a variable to record user input
phone_number = input("Phone: ")
# dictionary that will convert a number into the word
numb_to_string = {
    "1": "One",
    "0": "Zero",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
# variable that will hold the converted numbers
output = ""
# loop that goes through each character in the variable "phone_number"
for character in phone_number:
    # converts the number to its word, and adds it into the variable "output". Adds a space between each one and puts
    # an ! if there is something other than a number input
    output += numb_to_string.get(character, "!") + " "
print(output)

