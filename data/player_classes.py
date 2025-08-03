# data/player_classes.py
from colorama import Fore, Style

PLAYER_CLASSES = {
    "1": {
        "name": "Fighter",
        "description": "Tough melee warrior. High HP and Strength.",
        "stats": {"STR": 15, "DEX": 12, "CON": 14, "INT": 8, "WIS": 10, "CHA": 10},
        "hp": 20,
        "mana": 5,
        "starting_skills": {"Swordsmanship": 1, "Shield": 1}
    },
    "2": {
        "name": "Rogue",
        "description": "Agile and stealthy. Fast and clever.",
        "stats": {"STR": 10, "DEX": 16, "CON": 12, "INT": 12, "WIS": 10, "CHA": 12},
        "hp": 14,
        "mana": 10,
        "starting_skills": {"Stealth": 1, "Backstab": 1}
    },
    "3": {
        "name": "Wizard",
        "description": "Master of spells. High mana, fragile body.",
        "stats": {"STR": 8, "DEX": 12, "CON": 10, "INT": 16, "WIS": 14, "CHA": 10},
        "hp": 10,
        "mana": 20,
        "starting_skills": {"Magic Missile": 1, "Fireball": 1}
    }
}

def print_class_box(cls):
    print(Fore.YELLOW + f"\n╔═════════════════════════════╗")
    print(f"║ {cls['name']:^27} ║")
    print("╠═════════════════════════════╣")
    print(f"║ {cls['description']:<27} ║")
    print("╠═════════════════╦═══════════╣")
    print(f"║ HP: {cls['hp']:<13}║ Mana: {cls['mana']:<7}║")
    print("╠═════════════════╩═══════════╣")
    print("║ Stats:                       ║")
    for stat, val in cls['stats'].items():
        print(f"║   {stat}: {val:<2}                   ║")
    print("╠═════════════════════════════╣")
    print("║ Starting Skills:             ║")
    for skill in cls['starting_skills']:
        print(f"║   {skill:<24}║")
    print("╚═════════════════════════════╝" + Style.RESET_ALL)

def choose_class(player):
    while True:
        print(Fore.CYAN + "\n╔════════════════╗")
        print("║ Choose Your Class ║")
        print("╚════════════════╝" + Style.RESET_ALL)

        for key, cls in PLAYER_CLASSES.items():
            print(f"{key}. {cls['name']} - {cls['description']}")

        print("\nType the number to choose, or 'info <number>' to view details.")
        choice = input("Your choice: ").strip().lower()

        if choice.startswith("info"):
            parts = choice.split()
            if len(parts) == 2 and parts[1] in PLAYER_CLASSES:
                print_class_box(PLAYER_CLASSES[parts[1]])
            else:
                print("Invalid class number.")
        elif choice in PLAYER_CLASSES:
            cls = PLAYER_CLASSES[choice]
            player.name_class = cls['name']
            player.stats.update(cls['stats'])
            player.hp = cls['hp']
            player.max_hp = cls['hp']
            player.mana = cls['mana']
            player.max_mana = cls['mana']
            player.skills = {skill: 1 for skill in cls['starting_skills']}
            print(Fore.GREEN + f"\nYou have chosen the path of the {cls['name']}." + Style.RESET_ALL)
            break
        else:
            print("Invalid input.")