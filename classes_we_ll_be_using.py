import random
print("You encountered a merchant!")

class merchant():
    def __init__(self, ask_trade, trader_ans, experience):
        self.ask_trade = ask_trade
        self.trader_ans = trader_ans
        self.experience = experience
    def trade(ask_trade, trader_ans):
        ask_trade = input("Would you like to trade in your weapon for an upgraded weapon? Y/N: ").upper()
        while ask_trade == 'Y':
            trader_ans = random.randint(1,3)
            if trader_ans == 1:
                trader_ans == 'Yes'
                experience += 50
                print('The trader accepts the offer!')
            else:
                trader_ans == 'No'
                print('Trader declined :(')
class Hero:
    def __init__(self, name, health_bar, xp, level, attack, HP):
        self.name = name
        self.health_bar = health_bar
        self.xp = xp
        self.level = level

    def name():
        name = input('What is your name?: ')
        print('Hello' + name)

    def level_up(level, xp):
        if xp == {200, 300, 400, 500, 600, 700, 800, 900, 1000}:
            print("Leveled Up!")
            level = level + 1
            HP += 50
            attack += 50

    def health_bar():
        health = 100
        
        
        

        


