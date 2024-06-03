import random
import json
import json
import random
monsters = open("./monsert.json", encoding="utf8")
items = open("./thingys.json", encoding="utf8")
npcs = open("./npcs.json", encoding="utf8")
data = (json.load(monsters), json.load(items), json.load(npcs))

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
            ask_trade = input("Would you like to trade in your weapon for an upgraded weapon," +  "?").upper()
            while ask_trade == 'Y':
                trader_ans = random.randint(1,3)
                if trader_ans == 1:
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

                def battle_menu():
                    print("Battle Menu:")
                    print("1. attack")
                    print("2. taunt")
                    print("3. run")
                    move = input("Choose your move: ")	
                    if move == '1':
                        Hero.attack_monster(random_monster)
                    elif move == '2':
                        Hero.taunt(random_monster)
                    else:
                        print("You run away from the monster")     


        def attack(self, player):
            player.health -= self.attack_power
            print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")

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
            print(f"HP: {random_NPCs['hp']}")
            print(f"Attack: {random_NPCs['atk']}")
            print(f"Drops: {', '.join(random_NPCs['drops'])}")
            print(f"Description: {random_NPCs['description']}")
            print("'" + input(("just make them what you want them to say ;)")) + "'")
            print("             Ok              Bye")

        
        


    def generate_opp():       
        encounter = random.randint(1,3)
        if encounter == 1:
            Encounter.Monster.generate_mons()
                #put previous battle code inside of a function, and indicate here
            open_battle_menu = input("To open the battle menu, press B").lower()     
            if open_battle_menu == "b":
                Encounter.Monster.generate_mons.battle_menu()
        elif encounter == 2:
                #NPC encounter
            Encounter.NPCs.random_npc()
        elif encounter == 3:
                #you fall into a hole
            print("womp womp")
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
            xp = xp+50
            print("You won the challenge!")
            print("+50 XP")

    def lose(self):
        if self.health <= 0:
            print("Game Over")


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
        if choice == items['name'] & items['type'] == "Weapon":
            print(f"{choice['name']}")
            print(f"Attack: {choice['atk']}")
            print(f"Type: {choice['type']}")
            print(f"Description: {choice['description']}")
        elif choice == items['name'] & items['type'] == "Charm":
            print(f"{choice['name']}")
            print(f"Type: {choice['type']}")
            print(f"Benefits: {choice['benefits']}")
            print(f"Description: {choice['description']}")              
        if choice == items['name'] & items['type'] == "Weapon":
            print(f"{choice['name']}")
            print(f"HP restored: {choice['hp_restored']}")
            print(f"Type: {choice['type']}")
            print(f"Description: {choice['description']}")