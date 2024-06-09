import json
import os
from classes_we_ll_be_using import *

#WEAPONS!!!
Small_dagger = Items.Weapons("Small dagger", 20, "Weapon", "The very thing you begin your journey with.", 10)
Big_gender_dagger = Items.Weapons("Big (gender) dagger", 40, "Weapon", "An upgrade! Not that impressive, but still progress.", 20)
Big_boy_bat = Items.Weapons("Big boy bat", 60, "Weapon", "Despite the name, it can be used by anyone.", 25)
Big_sword = Items.Weapons("Big sword", 50, "Weapon", "Yeah, well...what were you expecting? Slightly stronger than the big gender dagger.", 30)
Pixel_sword = Items.Weapons("Pixel sword", 80, "Weapon", "Ooh, blocky!", 40)
Sparkle_sword =  Items.Weapons("Sparkle sword", 90, "Weapon", "Makes me wanna cry...", 50)
Mime_sword = Items.Weapons("Mime sword", 100, "Weapon", "Ceci n'est pas une épée (This is not a sword). (it's invisible, but does a lot of damage anyway.)", 60)
Ink_sword = Items.Weapons("Ink sword", 150, "Weapon","Weird thing from a weird guy!", 65)
Robot_sword = Items.Weapons("Robot sword", 200, "Weapon", "I stole this from the kits...don't tell!", 70)
Garden_shears = Items.Weapons("Garden shears", 99999999, "Weapon", "Totally not a reference to one of the most depressing games every made. Can only be used once. It does a lot of damage, but it's still fragile.", 99999999999999999999999999)

#Charms
Cyclops_eye = Items.Charms("Cyclops' eye", "Charm", ["Increases ATK by +24"], "You thought something pretty was going to be a charm? Nah.", 5)
Book = Items.Charms("Book", "Charm", ["Increases HP Limit by +100"], "Wikipedia.", 7)
Big_bag_of_nothing = Items.Charms("Big bag of nothing","Charm", ["Nothing sorry"],"HAHAHAHAHA!!! PRANKED!!! - Little boy", 1)
Fashion_magazine = Items.Charms("Fashion magazine","Charm",["Increases HP limit by +200"],"Ceci n'e-wait, this IS an authentic French magazine from Chanel! Smell the perfume samples and relax~", 50)
Eiffel_Tower = Items.Charms("Eiffel Tower", "Charm", ["Increases ATK by +77"], "Merci beaucoup.", 100)
Fear_of_falling = Items.Charms("Fear of falling", "Charm", ["Increases ATK by +200"], "Ok, I know it's not something pleasant to fit what it is, BUT-*thud*", 99999999999999999999999999)
Arachnophobia = Items.Charms("Arachnophobia", "Charm", ["Bragging rights"], "The feeling of conquering your fears. Literally.", 99999999999999999999999999)
Claustrophobia = Items.Charms("Claustrophobia", "Charm", ["FEAR."], "Ok, I know it came from the spider but it's just for dramatic effect. You're in a maze, right? It makes sense.", 99999999999999999999999999)
Spider_eyes = Items.Charms("Spider eyes", "Charm", ["Disgust"], "Okay, ew.", 99999999999999999999999999)

#FOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD!!!
Apple = Items.Food("Apple", 30, "Food", "The staple of restoration.", 2)
Croissant = Items.Food("Croissant", 50, "Food", "Cute, but also a fun treat.", 4)
Baguette = Items.Food("Baguette", 100, "Food", "Long boy.", 5)
Crepes = Items.Food("Crepes", 120, "Food", "Soft and fluffy.", 6)
Choux = Items.Food("Choux", 115, "Food", "The staple of restoration.", 8)
Macaron = Items.Food("Macaron", 75, "Food", "I'm sorry most of the food is French, but it has to be for now.", 10)


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