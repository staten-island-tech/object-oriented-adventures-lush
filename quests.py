import random
print("You encountered a merchant!")

class merchant():
    def __init__(info, entity, ask_trade, experience):

    def encounter(info):
        print('You encountered a' +entity+):

    def accept(info, ask_trade):
        ask_trade = input("Would you like to trade in your weapon for an upgraded weapon? Y/N: ").upper()
        while ask_trade == 'Y':
            trader_ans = random.randint(1,3)
            if trader_ans == 1:
                print('The trader accepts the offer!')
                return trader_ans
            else:
                print('Trader declined :(')

    def Level_up(ask_trade, experience):
        super()__init__()