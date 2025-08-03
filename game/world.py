import random

class Floor:
    def __init__(self, level=1, width=7, height=7):
        self.level = level
        self.width = width
        self.height = height
        self.rooms = [[None for _ in range(width)] for _ in range(height)]
        self.safe_room_pos = None
        self.boss_room_pos = None

        self.generate_floor()

    def generate_floor(self):
        all_positions = [(x, y) for y in range(self.height) for x in range(self.width)]
        random.shuffle(all_positions)

        # 1. Place safe room
        self.safe_room_pos = all_positions.pop()
        x, y = self.safe_room_pos
        self.rooms[y][x] = Room(x, y, "safe", "This is a well-lit safe room. You feel at ease.")

        # 2. Place boss room
        self.boss_room_pos = all_positions.pop()
        x, y = self.boss_room_pos
        self.rooms[y][x] = Room(x, y, "boss", "A powerful aura fills the air... the boss awaits!")

        # 3. Place traps, enemies, treasures
        traps = 3 + self.level  # scales with floor
        enemies = 4 + self.level
        treasures = 2 + self.level

        def place_type(type_, count, description):
            for _ in range(count):
                if not all_positions:
                    return
                x, y = all_positions.pop()
                self.rooms[y][x] = Room(x, y, type_, description)

        place_type("trap", traps, "You sense danger... a trap is nearby.")
        place_type("enemy", enemies, "You hear growling from the shadows...")
        place_type("treasure", treasures, "Something shiny catches your eye.")

        # 4. Fill in remaining normal rooms
        for y in range(self.height):
            for x in range(self.width):
                if self.rooms[y][x] is None:
                    self.rooms[y][x] = Room(x, y, "normal")

    def get_room(self, position):
        x, y = position
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.rooms[y][x]
        return None

    def get_exits(self, position):
        x, y = position
        directions = {
            "north": (x, y - 1),
            "south": (x, y + 1),
            "east": (x + 1, y),
            "west": (x - 1, y)
        }
        exits = {}
        for dir_name, pos in directions.items():
            room = self.get_room(pos)
            if room:
                # Let's say locked doors are marked on the room, e.g. room.locked_doors = ['east']
                # For now, no locked doors - all open
                exits[dir_name] = "locked" if getattr(room, "locked", False) else "open"
        return exits

class Room:
    def __init__(self, x, y, room_type="normal", description=None, npc=None):
        self.x = x
        self.y = y
        self.type = room_type
        self.npc = npc
        self.visited = False
        self.locked = False
        self.description = description or self.generate_description()

    def generate_description(self):
        base = f"You are in a room at ({self.x}, {self.y})."
        type_descriptions = {
            "normal": "Nothing stands out here.",
            "safe": "You feel safe here.",
            "boss": "A fearsome presence lurks nearby.",
            "trap": "You feel uneasy... something's wrong.",
            "enemy": "You hear movement nearby...",
            "treasure": "You see something valuable!",
        }
        return f"{base} {type_descriptions.get(self.type, '')}"


class World:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.map = [[None for _ in range(width)] for _ in range(height)]
        self.generate_rooms()

    def generate_rooms(self):
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x] = Room(x, y)

        # Place a few special rooms manually
        self.map[1][1] = Room(1, 1, "stairs_down")
        self.map[2][3] = Room(3, 2, "trap")
        self.map[3][3] = Room(3, 3, "enemy")
        self.map[4][2] = Room(2, 4, "treasure")

    def get_room(self, position):
        x, y = position
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x]
        return None
