import json
import random
from classes_we_ll_be_using import Monster
from classes_we_ll_be_using import Hero


print("As the shadows fade and the hero is faced with the challenge ahead of them...")
name = input("What is your name? ")
print("Welcome to the maze of life, " + name + ".")
print("As you look at what you have in your bindle, you realize you came here unprepared. Let's start with a tutorial.", "go to README.md for instructions")

start = input("To start, press F to walk forward: ").lower()
if start == 'f':
    print("As you walk through the dark maze, you see all kinda of creatures on the walls and in the shadows.")
    print("Suddenly, you run into a monster!")

with open('monsert.json') as f:
    Monsters = json.load(f)
    random_monster = random.choice(Monsters)

print("You encountered a " + random_monster['name'] + "!")
print(f"HP: {random_monster['hp']}")
print(f"Attack: {random_monster['atk']}")
print(f"Drops: {', '.join(random_monster['drops'])}")
print(f"Description: {random_monster['description']}")

attack = input("enter a to attack: ").lower()
if attack == 'a':
    Hero.attack_monster()
    
# generate a monster