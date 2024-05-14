import json
import os 

class NPCs():
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

dogwater = NPCs("Dogwater","Resident species.")
Angry_lost_tech_student = NPCs("Angry lost Tech student","Forces you to finish their homework.")
with open("npcs.json", "r") as f:
    data = json.load(f)
    ##Call classes in here


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("npcs.json")
os.rename(new_file, "npcs.json")