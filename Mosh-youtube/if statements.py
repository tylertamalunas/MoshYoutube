# look at conditions.txt
# if its hot
#   its a hot day
#   drink plenty of water
# otherwise
#   its a cold day
#   wear warm clothes
# otherwise
# its a lovely day
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day')

print('\n')

# example
# price of a house is $1M
# if buyer has good credit
#   they need to put down 10%
# otherwise
#   they need to put down 20%
# print the down payment
price_of_house = 1000000
good_credit = True
#good_credit = False

if good_credit:
    down_payment = price_of_house * 0.10
else:
    down_payment = price_of_house * 0.20
print(f"The buyer needs to put a down payment of ${down_payment}.")

