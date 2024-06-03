import json
import random
from classes_we_ll_be_using import *


def monologue():
    print("in this game you will be fighting the most dangerous monsters. your goal is to complete the maze and defeat the monster and attack him using weapons")
    print("throughout the game you wil have multiple enconters with the merchant. you, as the hero, will be able to gain xp through trade with the merchant")
    print ("if you answer yes to trading with the merchant you wil automatically be given 100 xp")
    print ("for extra instruction and more information, replay the game")
def explore():
    start = input("To start, press F to walk forward: ").lower()
    if start == 'f':

        Encounter.generate_opp()
        if Encounter.generate_opp():
            print("As you walk through the dark maze, you see all kind of creatures on the walls and in the shadows.")
            print("Suddenly, you run into a monster!")
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
    else:
        Encounter.Merchant.trade()

print("As the shadows fade and the hero is faced with the challenge ahead of them...")
print("Welcome to the maze of life, " + Hero.name + ".")
print("As you look at what you have in your bindle, you realize you came here unprepared. Let's start with a tutorial.", "go to README.md for instructions")
view_menu = input('press m to view the main menu').lower()
if view_menu == 'm':
    main_menu()
##Variable representing random_monster

        
        





