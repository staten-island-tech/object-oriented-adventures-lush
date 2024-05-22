import json
import os 
from classes_we_ll_be_using import NPCs


dogwater = NPCs("Dogwater","Resident species.")
Angry_lost_tech_student = NPCs("Angry lost Tech student","Forces you to finish their homework.")
Big_boys_mom = NPCs("Big boy's mom","She's mad.")

with open("npcs.json", "r") as f:
    data = json.load(f)
    data.append(dogwater.__dict__)
    data.append(Angry_lost_tech_student.__dict__)
    data.append(Big_boys_mom.__dict__)


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("npcs.json")
os.rename(new_file, "npcs.json")
#mseomg