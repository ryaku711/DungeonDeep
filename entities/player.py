import random

class Player:
    def __init__(self, name):
        self.name = name
        self.name_class = None
        self.hp = 0
        self.max_hp = 0
        self.mana = 0
        self.max_mana = 0

        self.stats = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0,
            "STA": 0,
            "DEF": 0,
        }

        self.skills = {}
        self.position = (0, 0)
        self.discovered_positions = set()

    # ... rest unchanged ...


    def move(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)
        self.discovered_positions.add(self.position)

    def roll_stats(self):
        def roll_4d6_drop_lowest():
            rolls = sorted([random.randint(1, 6) for _ in range(4)])
            return sum(rolls[1:])

        return {
            "STR": roll_4d6_drop_lowest(),
            "DEX": roll_4d6_drop_lowest(),
            "CON": roll_4d6_drop_lowest(),
            "INT": roll_4d6_drop_lowest(),
            "WIS": roll_4d6_drop_lowest(),
            "CHA": roll_4d6_drop_lowest(),
            "STA": roll_4d6_drop_lowest(),
            "DEF": roll_4d6_drop_lowest(),
        }
