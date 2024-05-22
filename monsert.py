import json
import os
import random
from random import *
from classes_we_ll_be_using import Monster


Cyclops = Monster("Cyclops", 500, 200, ["Big boy bat", "Cyclops' eye", "Apple"], "The guy you found on that one island in Greece.")
Big_boy = Monster("Big boy", 200, 50, ["Big Sword", "Book"], "Big boy. That's all.")
Little_boy = Monster("Little boy", 40, 10, ["Big Bag of Nothing"], "Little boy." )
Wide_boy = Monster("Wide_boy", 250, 20, ["Pixel sword"], "Wide like the Nile.")
Pretty_boy = Monster("Pretty boy", 100, 23, ["Sparkle sword"], "So pretty it hurts.")
Petite_boy = Monster("Petite boy", 50, 25, ["Baguette", "Croissant", "Fashion magazine", "Eiffel Tower", "Crepes", "Choux", "Macaron", "Mime sword"], "Is little guy, but French. Will drop many French things that are beneficial.")
Fally = Monster("Fally", 600, 20, ["Fear of Falling", "Ink sword"], "??????????")
SwiftBot = Monster("SwiftBot", 750, 250, ["Robot Sword"], "Trauma incarnate.")
MalakBot = Monster("MalakBot", 1000, 300, ["Garden shears"], "The final boss. Is singlehandedly responsible for dropping HOS and GPAs.")
Arachnia = Monster("Arachnia", 999, 500, ["Arachnophobia", "Claustrophobia", "Spider eyes", "Web sword"], "????????????????????????")
The_maze = Monster("The maze", 4000, 0, ["Trophy of victory"], "Yeah. C'mon. What are you waiting for?")

with open("monsert.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    data.append(Cyclops.__dict__)
    data.append(Big_boy.__dict__) 
    data.append(Little_boy.__dict__) 
    data.append(Wide_boy.__dict__) 
    data.append(Petite_boy.__dict__)
    data.append(Fally.__dict__)
    data.append(SwiftBot.__dict__) 
    data.append(MalakBot.__dict__) 
    data.append(Arachnia.__dict__)
    data.append(The_maze.__dict__)


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("monsert.json")
os.rename(new_file, "monsert.json")