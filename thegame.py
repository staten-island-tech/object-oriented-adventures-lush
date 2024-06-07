import json
import random
from classes_we_ll_be_using import *
from typeslow import *


monologue = "in this game you will be fighting the most dangerous monsters. your goal is to complete the maze and defeat the monster and attack him using weapons. throughout the game you will have multiple enconters with the merchant. you, as the hero, will be able to gain xp through trade with the merchant. if you answer yes to trading with the merchant you will automatically be given 100 xp. for extra instruction and more information, replay the game. As the shadows fade and the hero is faced with the challenge ahead of them... Welcome to the maze of life, " + Hero.name + ". As you look at what you have in your bindle, you realize you came here unprepared. Let's start with a tutorial. go to README.md for instructions"

#print_s(monologue)

inventory.append("Small dagger")
def explore():
    start = input("To start, press F to walk forward: ").lower()
    if start == 'f':
        Encounter.generate_opp()



def main_menu():
    print("Game Menu: ")
    print("1. Explore the maze")
    print ("2. View Inventory")
    print("3. Visit Merchant")
    choice = input("What would you like to do? ")
    if choice == '1':
        explore()
    elif choice == '2':
        print(inventory)
        Inventory.view()
    else:
        Encounter.Merchant.trade()

view_menu = input('press m to view the main menu: ').lower()
if view_menu == 'm':
    main_menu()

##Variable representing random_monster

        
        





