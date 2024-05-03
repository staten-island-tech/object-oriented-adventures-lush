import json
import os
class monsters():
    def __init__(self,name:str,hp:int,atk:int,drops:list,description:str):
            self.name=name
            self.hp=hp
            self.atk=atk
            self.drops=drops # this is what sort of items they drop, be it food or weapons
            self.description=description
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}, {self.drops}, {self.description}"

Cyclops = monsters("Cyclops:", 500, 200, ["Big boy bat", "Cyclops' eye", "Apple"], "The guy you found on that one island in Greece.")
Big_boy = monsters("Big boy:", 200, 50, ["Big Sword", "Book"], "Big boy. That's all.")
Little_boy = monsters("Little boy:", 40, 10, ["Big Bag of Nothing"], "Little boy." )
Wide_boy = monsters("Wide_boy:", 250, 20, ["Pixel sword"], "Wide like the Nile.")
Pretty_boy = monsters("Pretty boy:", 100, 23, ["Sparkle sword"], "So pretty it hurts")
Petite_boy = monsters("Petite boy:", 50, 25, ["Baguette", "Croissant", "Fashion magazine", "Eiffel Tower", "Crepes", "Choux", "Macaron", "Mime sword"], "Is little guy, but French. Will drop many French things that are beneficial.")
Fally = monsters("Fally:", 600, 20, ["Fear of Falling", "Ink sword"], "??????????")
SwiftBot = monsters("SwiftBot", 750, 250, ["Robot Sword"], "Trauma incarnate.")
MalakBot = monsters("MalakBot:", 1000, 300, ["Garden shears"], "The final boss. Is singlehandedly responsible for dropping HOS and GPAs.")
Arachnia = monsters("Arachnia:", 999, 500, ["Arachnophobia", "Claustrophobia", "Spider eyes", "Web sword"], "????????????????????????")

with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    #song_list = [Lush, Retired_from_Sad_New_Career_in_Business, Bury_Me_at_Makeout_Creek, Puberty_2, Be_the_Cowboy, Laurel_Hell, The_Land_Is_Inhospitable_and_So_Are_We]
    song_list = []
    ##Call classes in here
    data.append(Cyclops.__dict__, Big_boy.__dict__, Little_boy.__dict__, Wide_boy.__dict__, Petite_boy.__dict__, Fally.__dict__, SwiftBot.__dict__, MalakBot.__dict__, Arachnia.__dict__)

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")