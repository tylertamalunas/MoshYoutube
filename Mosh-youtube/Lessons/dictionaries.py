#Name: John Smith
#Email:john@gmail.com
#Phone: 1234

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) # this way if you type something that doesnt exist, it will give an error
print(customer.get("birthdate")) # this way wont display anything if it doesnt exist
print(customer.get("birthdate", "Jan 1 1980")) # this will supply a default value to display