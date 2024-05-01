class monsters():
    def __init__(self,name,hp,atk,drops,description):
            self.name=name
            self.hp=hp
            self.atk=atk
            self.drops=drops # this is what sort items they drop, be it food or weapons
            self.description=description
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}, {self.drops}, {self.description}"

Cyclops = monsters("Cyclops:", 500, 200, ["Big boy bat", "Cyclops' eye", "Apple"], "The guy you found on that one island in Greece.")
Big_boy = monsters("Big boy:", 200, 50, ["Big Sword", "Book"], "Big boy. That's all.")
Little_boy = monsters("Little_boy:", )
Wide_boy = monsters("Wide_boy:", 250, 20, ["Pixel sword"], "Wide like the Nile.")
Petite_boy = monsters("Petite_boy:", 50, 25, ["Baguette", "Croissant", "Fashion magazine", "Eiffel Tower", "Crepes", "Choux", "Macaron", "Mime sword"], "Is little guy, but French. Will drop many French things that are beneficial.")
Fally = monsters("Fally:", 600, 20, ["Fear of Falling", "Ink sword"], "??????????")
