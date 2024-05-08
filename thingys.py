import json
import os
class Weapons():
    def __init__(self,name:str,atk:int,type:str,description:str) -> None:
        self.name = name
        self.atk = atk
        self.type = type
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.atk}, {self.type}, {self.description}"
class Items():
    def __init__(self,name:str,type:str,description:str) -> None:
        self.name = name
        self.type = type
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.type}, {self.description}"
    
Small_dagger = Weapons("Small dagger", 20, "Weapon", "The very thing you begin your journey with.")
Big_gender_dagger = Weapons("Big (gender) dagger", 40, "Weapon", "An upgrade! Not that impressive, but still progress.")
Big_boy_bat = Weapons("Big boy bat", 60, "Weapon", "Despite the name, it can be used by anyone.")
Big_sword = Weapons("Big sword", 50, "Weapon", "Yeah, well...what were you expecting? Slightly stronger than the big gender dagger.")
Pixel_sword = Weapons("Pixel sword", 80, "Weapon", "Ooh, blocky!")
Mime_sword = Weapons("Mime sword", 100, "Weapon", "Ceci n'est pas une épée (This is not a sword). (it's invisible, but does a lot of damage anyway.)")
Ink_sword = Weapons("Ink sword", 150, "Weapon","Weird thing from a weird guy!")



with open("thingys.json", "r") as f:
    data = json.load(f)
    #data.append(ya.__dict__)

    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data)

        f.write(json_string)

    os.remove("thingys.json")
    os.rename(new_file, "thingys.json")