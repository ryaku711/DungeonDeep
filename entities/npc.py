class NPC:
    def __init__(self, name, description="",dialogue=None, aura=None):
        self.name = name
        self.description = description
        self.aura = aura or ""
        self.dialogue = dialogue or []

    def look(self):
        return f"{self.aura} {self.name}: {self.description}".strip()

    def talk(self):
        return "\n".join(self.dialogue)

    def interact(self, player):
        return f"{self.name} nods silently."

# Special NPC: Caretaker
class Caretaker(NPC):
    def __init__(self):
        super().__init__(
            name="Elarion, the Caretaker",
            aura="White Aura",
            description="An ancient figure robed in faded cloth, radiating calm power.",
            dialogue=[
                "Elarion: 'Welcome to this place, lost soul. You stand on the threshold of a great trial.'",
                "Elarion: 'Place your hand upon the altar to choose your destiny.'"
            ]
        )

    def interact(self, player):
        return (
            "The Caretaker says:\n"
            "\"Welcome, traveler. You must be confused... but you are safe here.\n"
            "Place your hand upon the altar when you are ready to choose your path.\"\n"
        )

class Shopkeeper(NPC):
    def __init__(self):
        super().__init__(
            name="John",
            description="Just your typical vendor",
            aura="(White Aura)"
        )