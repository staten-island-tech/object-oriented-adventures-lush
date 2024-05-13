import random
print("You encountered a merchant!")

class merchant():
    def __init__(info, ask_trade, trader_ans, experience):
        info.ask_trade = ask_trade
        info.trader_ans = trader_ans
        info.experience = experience

    def trade(info, ask_trade, trader_ans):
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

        
