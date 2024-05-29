import json
import random
from classes_we_ll_be_using import *


def monologue():
    print("in this game you will be fighting the most dangerous monsters. your goal is to complete the maze and defeat the monster and attack him using weapons")
    print("throughout the game you wil have multiple enconters with the merchant. you, as the hero, will be able to gain xp through trade with the merchant")
    print ("if you answer yes to trading with the merchant you wil automatically be given 100 xp")
    print ("for extra instruction and more information, replay the game")
      
print("As the shadows fade and the hero is faced with the challenge ahead of them...")
print("Welcome to the maze of life, " + Hero.name + ".")
print("As you look at what you have in your bindle, you realize you came here unprepared. Let's start with a tutorial.", "go to README.md for instructions")
view_menu = input('press m to view the main menu').lower()
if view_menu == 'm':
    def main_menu():
        print("Game Menu: ")
        print("1. Explore the maze")
        print ("2. View Inventory")
        print("3. Visit Merchant")
        choice = input("What would you like to do? ")
        if choice == '1':
        #		explore_maze()
        elif choice == '2':
            #print inventory data
        else:
            #visit_merchant()

##Variable representing random_monster
def explore():
    start = input("To start, press F to walk forward: ").lower()
    if start == 'f':
        print("As you walk through the dark maze, you see all kind of creatures on the walls and in the shadows.")
        print("Suddenly, you run into a monster!")
        enc = random.randint(1,3)
        if enc == 1:
                #put previous battle code inside of a function, and indicate here
        elif enc == 2:
                #NPC encounter
        else:
                #you fall into a hole
        
def encounter_monster():
    encounter = random.randint(1,3)
    if encounter == 1:
            #put previous battle code inside of a function, and indicate here
    elif encounter == 2:
            #NPC encounter
    else:
            #you fall into a hole

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


 
#use varible inside this function
        


##Add to hero class#


#Generate a random monster and print its data:
with open('monsert.json') as f:
	Monsters = json.load(f)

random_monster = random.choice('monsert.json')


print("You encountered a " + random_monster['name'] + "!")
print(f"HP: {random_monster['hp']}")
print(f"Attack: {random_monster['atk']}")
print(f"Drops: {', '.join(random_monster['drops'])}")
print(f"Description: {random_monster['description']}")

