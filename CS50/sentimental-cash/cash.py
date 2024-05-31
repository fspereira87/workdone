# TODO

from cs50 import get_float


def calculate_change():
    change = get_float("Change owed: ")

    while change < 0:

        change = get_float("Change owed: ")


    cents = round(change*100)

    count =0
    coins = [25,10,5,1]

    for coin in coins:
        count += cents//coin
        cents %=coin

    return count

result = calculate_change()
print (result)



