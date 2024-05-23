import random
import json
monsters = open("./monsert.json", encoding="utf8")
print("You encountered a merchant!")

class Merchant():
    def __init__(info, ask_trade, trader_ans, xp):
        info.ask_trade = ask_trade
        info.trader_ans = trader_ans
        
    def trade(info, ask_trade, trader_ans):
        ask_trade = input("Would you like to trade in your weapon for an upgraded weapon? Y/N: ").upper()
        while ask_trade == 'Y':
            trader_ans = random.randint(1,3)
            if trader_ans == 1:
                trader_ans == 'Yes'
                xp += 50
                print("+50 XP")
                health += 50
                print("+50 Health Points")
                print('The trader accepts the offer!')
            else:
                trader_ans == 'No'
                print('Trader declined :(')
                break

class Hero:
    def __init__(self, name, level, attack_power, health, xp):
        self.name = name
        self.xp = xp
        self.level = level
        self.attack_power = attack_power
        self.health = health

    def level_up(level, health, attack_power, xp):
        if xp == {200, 400, 800, 1000}:
            level = level + 1
            health += 50
            attack_power += 50

    def attack_monster(self, monster):
            monster.health -= self.attack_power
            print(f"{self.name} attacks {monster.name} for {self.attack_power} damage!")

    def win(self, monster):
        if monster.health <= 0:
            level = level + 1
            print("You won the challenge!")

    def lose(self):
        if self.health <= 0:
            print("Game Over")
        
class Monster():
    def __init__(self, name:str, hp:int, attack_power:int, drops:list, health:int, description:str):
        self.name=name
        self.hp=hp
        self.attack_power=attack_power
        self.drops=drops # this is what sort of items they drop, be it food or weapons
        self.description = description
    
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.damage = 0

    def generate_monster():
        while True:
            random_monster = random.choice(data)
            print(f"{self.name} has appeared!")

    def attack(self, player):
        player.health -= self.attack_power
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")

    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}, {self.drops}, {self.description}"