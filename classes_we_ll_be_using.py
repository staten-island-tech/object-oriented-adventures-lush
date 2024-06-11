import random
import os
import json
import random
monsters = open("./monsert.json", encoding="utf8")
items = open("./thingys.json", encoding="utf8")
npcs = open("./npcs.json", encoding="utf8")
data_monsters = (json.load(monsters))
data_items = (json.load(items))
data_npcs = (json.load(npcs))


def explore():
    walk = input("Press F to walk forward.").lower()
    if walk == 'f':
        Encounter.generate_opp()

class Encounter():


    class Merchant():
        def __init__(self, name):
            self.name = name 
        def trade():
            print("You encountered a merchant!")
            open('merchant.png')
            ask_trade = input("Would you like to trade in your weapon for an upgraded weapon," +  "? Y or N ").upper()
            while ask_trade == 'Y':
                trader_ans = random.randint(1,3)
                if trader_ans == 1:
                    pass
                    trader_ans == 'Yes'
                    Hero.xp += 50
                    print("+50 XP")
                    Hero.health += 50
                    print("+50 Health Points")
                    print('The trader accepts the offer!')
                    break
                else:
                    trader_ans == 'No'
                    print('Trader declined :(')
                    break
            if ask_trade != 'Y':
                print("Yeah, are you sure?")
            
        class Merchant_shop():

            def __init__(self, name, inventory_items):
                self.name = name
                self.inventory_items = [
                {"name": f"{data_items['name']}", "type": f"{data_items['type']}", "price": 0+{data_items['price']}}
                ]
                #fill in all the items in json item file
                with open('thingys.json') as f:
                    thingys = json.load(f)
                    self.inventory.append(thingys['name'])
            def __str__(self):
                return f"{self.name}, {self.inventory}, {self.inventory_items}"
            def sell_item(item):
                item_forsale = input("Which item would you like to sell: ")
                for item in Hero.inventory:
                    print(f"{item['name']} - {item['price']}")
                    if item_forsale == item['name']:
                        Hero.xp = Hero.xp + 20
                        Hero.money = Hero.money + item['price']
                        print(f"Merchant bought {item['name']} for ${item['price']}. +20 XP! Current XP: {Hero.xp}. Current balance: {Hero.money}")
                        return

            def buy_item(item):
                for item in inventory:
                    print(f"{item['name']} - {item['price']}")
                    buy = input("Which item would you like you buy?:")
                for item in inventory:
                    if buy == {item['name']}:
                        item.append(Hero.inventory)
                        Hero.money = Hero.money - {item['price']}
                        print(f"You bought the {item['name']} for {item['price']}. Current balance: {Hero.money}")
                        return
                        

    class Monster():
        def __init__(self, name:str, hp:int, attack_power:int, drops:list, description:str):
            self.name=name
            self.hp=hp
            self.attack_power=attack_power
            self.drops=drops # this is what sort of items they drop, be it food or weapons
            self.description = description

        class generate_mons():
            def random_monster_gen():
                with open('monsert.json') as f:
                    Monsters = json.load(f)
                random_monster = random.choice(Monsters)
                print("You encountered a " + random_monster['name'] + "!")
                print(f"HP: {random_monster['hp']}")
                print(f"Attack: {random_monster['atk']}")
                print(f"Drops: {', '.join(random_monster['drops'])}")
                print(f"Description: {random_monster['description']}")

            def battle_sequence():
                while True:
                    print("Battle Menu:")
                    print("1. Attack")
                    print("2. Taunt")
                    print("3. Run")
                    choice = input("Choose your move: ")

                    if choice == "1":
                        pass
                        Hero.attack_monster(Hero.name, random.monster)
                    elif choice == "2":
                        pass
                        Hero.taunt(Hero.name , random.monster)
                    elif choice == "3":
                        return
                    else:
                        print("Invalid choice. Please choose a valid option.")
                    if {Encounter.Monster['hp']} <= 0:
                        print("You won! You earned 50 XP! Check your inventory for more items ;)")
                        inventory.append(Encounter.Monster['drops'])
                    if Hero.health <= 0:
                        print("You died. Game over.")
                        break


        def attack(self, player):
            dodge_chance = random.randint(1,64)
            if dodge_chance != 1:
                player.health -= self.attack_power
                print(f"{self.name} attacks {player.name} for {self.atk} damage!")
            elif dodge_chance == 1:
                print(f"{self.name} attacks {player.name}, but {player.name} dodged the attack!")
            Encounter.Monster.generate_mons.battle_sequence()
        
        def take_damage(self, player_attack):
            self.health -= player_attack
            print(f"{Hero.name} attacks {self.name} for {player_attack} damage!")

        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.drops}, {self.description}"
        
    class NPCs():
        def __init__(self, name, description) -> None:
            self.name = name
            self.description = description
        def __str__(self):
            return f"{self.name}, {self.description}"
        def random_npc():
            with open('npcs.json') as f:
                NPCs = json.load(f)
                random_NPCs = random.choice(NPCs)
            print("You encountered a " + random_NPCs['name'] + "!")
            print(f"Description: {random_NPCs['description']}")

        
        


    def generate_opp():       
        encounter = random.randint(1,3)
        if encounter == 1:
            print("As you walk through the dark maze, you see all kind of creatures on the walls and in the shadows.")
            print("Suddenly, you run into a monster!")
            Encounter.Monster.generate_mons.random_monster_gen()
            Encounter.Monster.generate_mons.battle_sequence()
        elif encounter == 2:
                #NPC encounter
            Encounter.NPCs.random_npc()
        elif encounter == 3:
                #you fall into a hole
            print("womp womp. You fell into a hole!")
            print("That's unlucky. I'll help you out!")
            

class Hero:
    name = input("What is your name? ")

    def __init__(self, name, level, attack_power, health, xp):
        self.name = name
        self.xp = xp
        self.level = level
        self.attack_power = attack_power
        self.health = health
    def __str__(self):
        return f"{self.name}, {self.xp}, {self.level}, {self.attack_power}, {self.health}"
    def taunt(self, random_monster):
        taunt = input("You say to the monster, ")
        print(self.name + ' taunts ' + random_monster.name)
        response  = random.randint(1,3)
        if response == 1:
            print(random_monster.name + ' gets angry and attacks')
        elif response == 2:
            print(random_monster.name + ' cries and runs away...?')
        else:
            print("Wow. You really thought that was gonna work?")
        Encounter.Monster.attack()
        Encounter.Monster.generate_mons.battle_sequence()


    def level_up(level, health, attack_power, xp):
        if xp == {200, 400, 800, 1000}:
            level = level + 1
            health += 50
            attack_power += 50

    def attack_monster(self, monster):
        dodge_chance = random.randint(1,64)
        if dodge_chance != 1:
            monster.health -= self.attack_power
            print(f"{self.name} attacks {monster.name} for {self.attack_power} damage!")
        elif dodge_chance == 1:
            print(f"{self.name} attacks {monster.name}, but {monster.name} dodged the attack!")
        Encounter.Monster.attack()
        Encounter.Monster.generate_mons.battle_sequence()

    def win(self, monster):
        if monster.health <= 0:
            xp = xp+50
            print("You won the challenge!")
            print("+50 XP")

    def lose(self):
        if self.health <= 0:
            print("Game Over")


item = ""
class Items():
    class Weapons():
        def __init__(self,name:str,atk:int,type:str,description:str,price:int) -> None:
            self.name = name
            self.atk = atk
            self.type = type
            self.description = description
            self.price = price
        def __str__(self):
            return f"{self.name}, {self.atk}, {self.type}, {self.description}, {self.price}"
    class Charms():
        def __init__(self,name:str,type:str,benefits:list,description:str,price:int) -> None:
            self.name = name
            self.type = type
            self.benefits = benefits
            self.description = description
            self.price = price
        def __str__(self):
            return f"{self.name}, {self.type}, {self.benefits}, {self.description}, {self.price}"
    class Food():
        def __init__(self,name:str,hp_restored:int,type:str,description:str,price:int) -> None:
            self.name = name
            self.hp_restored = hp_restored
            self.type = type
            self.description = description
            self.price = price
        def __str__(self):
            return f"{self.name}, {self.hp_restored}, {self.type}, {self.description}, {self.price}"
inventory = []
class Inventory():
    def add_item():
        choice = input("Would you like to buy this item? Y or N")
        if choice == "Y":
            inventory.append(item)
        elif choice == "N":
            print("Purchase declined")
            
    def sell_item():
        choice = input("Would you like to sell this item? Y or N")
        if choice == "Y":
            inventory.remove(item)
    
    def view():
        choice = input("Choose an item to view information.")
        if choice == data_items['name'] & data_items['type'] == "Weapon":
            print(f"{choice['name']}")
            print(f"Attack: {choice['atk']}")
            print(f"Type: {choice['type']}")
            print(f"Description: {choice['description']}")
        elif choice == data_items['name'] & data_items['type'] == "Charm":
            print(f"{choice['name']}")
            print(f"Type: {choice['type']}")
            print(f"Benefits: {choice['benefits']}")
            print(f"Description: {choice['description']}")              
        if choice == data_items['name'] & data_items['type'] == "Weapon":
            print(f"{choice['name']}")
            print(f"HP restored: {choice['hp_restored']}")
            print(f"Type: {choice['type']}")
            print(f"Description: {choice['description']}")