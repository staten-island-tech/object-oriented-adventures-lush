import json
import os
class Items():
    def __init__(self,name:str,type:str,description:str) -> None:
        self.name = name
        self.type = type
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.type}, {self.description}"
    
Small_dagger = Items("Small dagger", )

with open("thingys.json", "r") as f:
    data = json.load(f)
    #data.append(ya.__dict__)

    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data)

        f.write(json_string)

    os.remove("thingys.json")
    os.rename(new_file, "thingys.json")