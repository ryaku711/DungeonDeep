class NPC:
    def __init__(self, name, aura_color, description, dialogue=None):
        self.name = name
        self.aura_color = aura_color
        self.description = description
        self.dialogue = dialogue or []

    def look(self):
        return f"({self.aura_color} Aura) {self.name} - {self.description}"

    def talk(self):
        return "\n".join(self.dialogue)
