import json
from game.world import Floor, Room
from entities.npc import Caretaker

# Keyword mapping from Donjon summaries to internal room types
summary_to_type = {
    "trap": "trap",
    "treasure": "treasure",
    "hidden treasure": "treasure",
    "fire trap": "trap",
    "empty": "normal",
    "monster": "enemy",
    "spider": "enemy",
    "goblin": "enemy",
    "duergar": "enemy",
    "rat": "enemy",
    "darkmantle": "enemy",
    "shriek": "enemy",
    "boss": "boss",
}

def infer_room_type(summary):
    summary = summary.lower()
    for keyword, rtype in summary_to_type.items():
        if keyword in summary:
            return rtype
    return "normal"

def import_donjon_floor(json_path, level=1):
    with open(json_path, "r") as f:
        data = json.load(f)

    floor = Floor(level=level, width=100, height=100)
    floor.rooms = {}

    first_valid_pos = None

    for room in data.get("rooms", []):
        if not room or "col" not in room or "row" not in room:
            continue

        x, y = room["col"], room["row"]
        pos = (x, y)

        # Use room name or summary as description
        desc = room.get("contents", {}).get("detail", {}).get("room_features", "A featureless room.")
        summary = room.get("contents", {}).get("summary", "")

        room_type = infer_room_type(summary)

        room_obj = Room(x=x, y=y, description=desc, room_type=room_type)

        # Place Caretaker in the first valid room
        if not first_valid_pos:
            first_valid_pos = pos
            room_obj.npc = Caretaker()

        floor.rooms[pos] = room_obj

    return floor
