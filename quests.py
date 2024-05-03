import random
print("You encountered a trader!")

trade = input("Would you like to trade in your weapon for an upgraded weapon? Y/N: ").upper()
if trade == 'Y':
    trader_ans = random.randint(1,3)
    if trader_ans == 1:
        print('The trader accepts the offer!')
    else:
        print('Trader declined :(')
        try_again = input("Try again? Y/N: ").upper()
        if try_again == 'Y':
            