is_hot = True
is_cold = False

if is_hot:
    print("it's a hot day, drink plenty water")
elif is_cold:
    print("enjoy your day, wear thick cloths")
else:
    print("it's a lovely day")


# Write a python code to calculate the down payment of a house.
# if the buyer has good credit, down payment should be 10% of the price,
# if the buyer does not have good credit, down payment should be 20% of the price

price = 1000000
good_credit = False
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'down payment: ${down_payment}')

# LOGICAL OPERATORS
# if buyer has high income and good credit, He is eligible for loan

has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print('eligible for loan')
elif has_high_income or has_good_credit:
        print("you are good to go")
else:
    if has_high_income and not has_good_credit:
        print('you are not eligible')






