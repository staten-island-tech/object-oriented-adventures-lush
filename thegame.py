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

start = input("To start, press F to walk forward: ").lower()
if start == 'f':
    print("As you walk through the dark maze, you see all kind of creatures on the walls and in the shadows.")
    print("Suddenly, you run into a monster!")

##Variable representing random_monster
    
with open('monsert.json') as f:
    Monsters = json.load(f)
    random_monster = random.choice(Monsters)

print("You encountered a " + random_monster['name'] + "!")
print(f"HP: {random_monster['hp']}")
print(f"Attack: {random_monster['atk']}")
print(f"Drops: {', '.join(random_monster['drops'])}")
print(f"Description: {random_monster['description']}")


def provoke():
    provoke = input("enter a to attack: ").lower()
    if provoke == 'a':
        Hero.attack_monster(Hero
                            .self, Monster.self)

provoke()

#use varible inside this function
        
Merchant.trade()