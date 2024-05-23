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

# generate a monster