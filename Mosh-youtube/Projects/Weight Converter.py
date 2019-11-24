weight = int(input('Weight: '))
units = input('(L)bs or (K)g: ')


# could also use if unit.upper() == "L":
if units.upper() == "L":
    l_to_k = weight * 0.45
    print(f'You are {l_to_k} kilograms.')
elif units.upper() == "K":
    k_to_l = weight / 0.45
    print(f'You are {k_to_l} pounds.')
else:
    print("I didn't get that.")