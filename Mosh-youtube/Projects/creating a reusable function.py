#message = input(">")
# break message down into parts
#words = message.split(' ')
#emojis = {
#    ":)": "☺",
#    ":(": "☹"
#}
#output = ""
#for word in words:
#    output += emojis.get(word, word) + " "
#print(output)

# make the above into a function
# lines 3 to 10 can be made into a function
# give the function the var 'message'
# functions should not worry about receiving input or printing it

# function takes the parameter 'message'
def  emoji_convert(message):
    words = message.split(' ')
    emojis = {
        ":)": "☺",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    # stores the result of the function in 'output'
    return output


# asks for the users input and stores in 'message'
message = input(">")
# calls the function, and uses the variable 'message' as the parameter.
print(emoji_convert(message))
