message = input(">")
# break message down into parts
words = message.split(' ')
emojis = {
    ":)": "☺",
    ":(": "☹"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
