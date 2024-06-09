import json
import random
from classes_we_ll_be_using import *
from typeslow import *


monologue = "in this game you will be fighting the most dangerous monsters. your goal is to complete the maze and defeat the monster and attack him using weapons. throughout the game you will have multiple enconters with the merchant. you, as the hero, will be able to gain xp through trade with the merchant. if you answer yes to trading with the merchant you will automatically be given 100 xp. for extra instruction and more information, replay the game. As the shadows fade and the hero is faced with the challenge ahead of them... Welcome to the maze of life, " + Hero.name + ". As you look at what you have in your bindle, you realize you came here unprepared. Let's start with a tutorial. go to README.md for instructions"



def explore():
    start = input("To start, press F to walk forward: ").lower()
    if start == 'f':
        Encounter.generate_opp()

def shop_menu(self, player, inventory, prices):
	while True:
        print(f“Welcome to {merchant_shop.name}”)
        print(“Available items: “)
        for item in inventory:
            print(f”{item.name}: {prices[item]}”)
            print(“Shop Menu: “)
            print(“1. Buy an item” )
            print(2. Sell an item”)
            print(“3. Trade an item”)
            print(“4. Return to main menu”)

        Deal = input(“What would you like to do: “)
        if choice == ‘1’:
            merchant_shop.buy_item()
        elif choice == ‘2’:
            merchant_shop.sell_item()
        elif choice == ‘3’:
            merchant_shop.trade_item()
        elif choice == ‘4’:
            break

def main_menu():
    print("Game Menu: ")
    print("1. Explore the maze")
    print("2. View Inventory")
    print("3. Visit Merchant")
    choice = input("What would you like to do? ")
    if choice == '1':
        explore()
        print_s(monologue)
        print("that was a good move")
    elif choice == '2':
        print(inventory)
    else:
        Encounter.Merchant.trade()
        print("oueeff that was a bad move")

view_menu = input('press m to view the main menu: ').lower()
if view_menu == 'm':
    main_menu()



##Variable representing random_monster

        
        





