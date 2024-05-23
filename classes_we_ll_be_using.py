import json
import random
monsters = open("./monsert.json", encoding="utf8")
items = open("./thingys.json", encoding="utf8")
npcs = open("./npcs.json", encoding="utf8")
data = (json.load(monsters), json.load(items), json.load(npcs))
print("You encountered a merchant!")



class Merchant():
    def __init__(self, name):
       self.name = name    
    def trade(self, Hero):
        ask_trade = input("Would you like to trade in your weapon for an upgraded weapon, {Hero.self.name}, ?").upper()
        while ask_trade == 'Y':
            trader_ans = random.randint(1,3)
            if trader_ans == 1:
                trader_ans == 'Yes'
                Hero.xp += 20
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

inventory = []
class Monster():
    def __init__(self, name:str, hp:int, attack_power:int, drops:list, description:str):
        self.name=name
        self.hp=hp
        self.attack_power=attack_power
        self.drops=drops # this is what sort of items they drop, be it food or weapons
        self.description = description

    def generate_monster():
        while True:
            random_monster = random.choice(data[0]['name'])
            print(random_monster , "has appeared!")


    def attack(self, player):
        player.health -= self.attack_power
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")

    def take_damage(self,player,player_attack):
        self.health -= player_attack
        print(f"{player.name} attacks {self.name} for {player_attack} damage!")

    def random_monster(self):
            random_monster = random.choice(data)
            print(f"{self.name} has appeared!")
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}, {self.drops}, {self.description}"
  
class NPCs():
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.description}"
item = ""
class Items():
    class Weapons():
        def __init__(self,name:str,atk:int,type:str,description:str) -> None:
            self.name = name
            self.atk = atk
            self.type = type
            self.description = description
        def __str__(self):
            return f"{self.name}, {self.atk}, {self.type}, {self.description}"
    class Charms():
        def __init__(self,name:str,type:str,benefits:list,description:str) -> None:
            self.name = name
            self.type = type
            self.benefits = benefits
            self.description = description
        def __str__(self):
            return f"{self.name}, {self.type}, {self.benefits}, {self.description}"
    class Food():
        def __init__(self,name:str,hp_restored:int,type:str,description:str) -> None:
            self.name = name
            self.hp_restored = hp_restored
            self.type = type
            self.description = description
        def __str__(self):
            return f"{self.name}, {self.hp_restored}, {self.type}, {self.description}"
class Inventory():
    def add_item():
        choice = input("Would you like to buy this item? Y or N")
        if choice == "Y":
            inventory.append(item)
            
    def sell_item():
        choice = input("Would you like to sell this item? Y or N")
        if choice == "N":
            inventory.remove(item)