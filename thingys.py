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
class Charms():
    def __init__(self,name:str,type:str,benefits:list,description:str) -> None:
        self.name = name
        self.type = type
        self.benefits = benefits
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.type}, {self.benefits}, {self.description}"
class Food():
    def __init__(self,name:str,hp_restored:int,type:str,description:str) -> None:
        self.name = name
        self.hp_restored = hp_restored
        self.type = type
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.hp_restored}, {self.type}, {self.description}"

    
#WEAPONS!!!
Small_dagger = Weapons("Small dagger", 20, "Weapon", "The very thing you begin your journey with.")
Big_gender_dagger = Weapons("Big (gender) dagger", 40, "Weapon", "An upgrade! Not that impressive, but still progress.")
Big_boy_bat = Weapons("Big boy bat", 60, "Weapon", "Despite the name, it can be used by anyone.")
Big_sword = Weapons("Big sword", 50, "Weapon", "Yeah, well...what were you expecting? Slightly stronger than the big gender dagger.")
Pixel_sword = Weapons("Pixel sword", 80, "Weapon", "Ooh, blocky!")
Sparkle_sword =  Weapons("Sparkle sword", 90, "Weapon", "Makes me wanna cry...")
Mime_sword = Weapons("Mime sword", 100, "Weapon", "Ceci n'est pas une épée (This is not a sword). (it's invisible, but does a lot of damage anyway.)")
Ink_sword = Weapons("Ink sword", 150, "Weapon","Weird thing from a weird guy!")
Robot_sword = Weapons("Robot sword", 200, "Weapon", "I stole this from the kits...don't tell!")
Garden_shears = Weapons("Garden shears", 99999999, "Weapon", "Totally not a reference to one of the most depressing games every made. Can only be used once. It does a lot of damage, but it's still fragile.")

#Charms
Cyclops_eye = Charms("Cyclops' eye", "Charm", ["Increases ATK by +24"], "You thought something pretty was going to be a charm? Nah.")
Book = Charms("Book", "Charm", ["Increases HP Limit by +100"], "Wikipedia.")
Big_bag_of_nothing = Charms("Big bag of nothing","Charm", ["Nothing sorry"],"HAHAHAHAHA!!! PRANKED!!! - Little boy")
Fashion_magazine = Charms("Fashion magazine","Charm",["Increases HP limit by +200"],"Ceci n'e-wait, this IS an authentic French magazine from Chanel! Smell the perfume samples and relax~")
Eiffel_Tower = Charms("Eiffel Tower", "Charm", ["Increases ATK by +77"], "Merci beaucoup.")
Fear_of_falling = Charms("Fear of falling", "Charm", ["Increases ATK by +200"], "Ok, I know it's not something pleasant to fit what it is, BUT-*thud*")
Arachnophobia = Charms("Arachnophobia", "Charm", ["Bragging rights"], "The feeling of conquering your fears. Literally.")
Claustrophobia = Charms("Claustrophobia", "Charm", ["FEAR."], "Ok, I know it came from the spider but it's just for dramatic effect. You're in a maze, right? It makes sense.")
Spider_eyes = Charms("Spider eyes", "Charm", ["Disgust"], "Okay, ew.")

#FOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD!!!
Apple = Food("Apple", 30, "Food", "The staple of restoration.")
Croissant = Food("Croissant", 50, "Food", "Cute, but also a fun treat.")
Baguette = Food("Baguette", 100, "Food", "Long boy.")
Crepes = Food("Crepes", 120, "Food", "Soft and fluffy.")
Choux = Food("Choux", 115, "Food", "The staple of restoration.")
Macaron = Food("Macaron", 75, "Food", "I'm sorry most of the food is French, but it has to be for now.")


with open("thingys.json", "r") as f:
    data = json.load(f)
    data.append(Small_dagger.__dict__)
    data.append(Big_gender_dagger.__dict__)
    data.append(Big_boy_bat.__dict__)
    data.append(Big_sword.__dict__)
    data.append(Pixel_sword.__dict__)
    data.append(Sparkle_sword.__dict__)
    data.append(Mime_sword.__dict__)
    data.append(Ink_sword.__dict__)
    data.append(Robot_sword.__dict__)
    data.append(Garden_shears.__dict__)
    data.append(Cyclops_eye.__dict__)
    data.append(Book.__dict__)
    data.append(Big_bag_of_nothing.__dict__)
    data.append(Fashion_magazine.__dict__)
    data.append(Eiffel_Tower.__dict__)
    data.append(Fear_of_falling.__dict__)
    data.append(Arachnophobia.__dict__)
    data.append(Claustrophobia.__dict__)
    data.append(Spider_eyes.__dict__)
    data.append(Apple.__dict__)
    data.append(Croissant.__dict__)
    data.append(Baguette.__dict__)
    data.append(Crepes.__dict__)
    data.append(Choux.__dict__)
    data.append(Macaron.__dict__)



    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data)

        f.write(json_string)

    os.remove("thingys.json")
    os.rename(new_file, "thingys.json")