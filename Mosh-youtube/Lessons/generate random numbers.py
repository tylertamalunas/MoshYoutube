import random

# picks 3 random numbers
for i in range(3):
    print(random.random())
# picks 3 random numbers from 10 to 20
for a in range(3):
    print(random.randint(10, 20))

# picks a random person from the list
members = ['John', 'Mary', 'Tyler', 'Bill']
leader = random.choice(members)
print(leader)