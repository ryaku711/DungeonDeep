from entities.npc import NPC

def get_caretaker():
    return NPC(
        name="Elarion, the Caretaker",
        aura="White",
        description="An ancient figure robed in faded cloth, radiating calm power.",
        dialogue=[
            "Elarion: 'Welcome to this place, lost soul. You stand on the threshold of a great trial.'",
            "Elarion: 'Place your hand upon the altar to choose your destiny.'"
        ]
    )
