import random
from classes_we_ll_be_using import Merchant

print("You encountered a merchant!")

def accept(info, ask_trade, trader_ans):
        ask_trade = input("Would you like to trade in your weapon for an upgraded weapon? Y/N: ").upper()
        while ask_trade == 'Y':
            trader_ans = random.randint(1,3)
            if trader_ans == 1:
                trader_ans == 'Yes'
                experience += 10
                print('The trader accepts the offer!')
            else:
                trader_ans == 'No'
                print('Trader declined :(')
                #jsgrosg