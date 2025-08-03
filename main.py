from entities.player import Player
from game.engine import GameEngine
from data.donjon_importer import import_donjon_floor
from game.world import Floor
from data.player_classes import choose_class
from data.npc_dialogue import get_caretaker


def main_menu():
    print("Welcome to Dungeon Deep!")
    while True:
        print("\nMain Menu:")
        print("1. New Game")
        print("2. Continue (Coming Soon)")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            return "new"
        elif choice == "2":
            print("Continue not implemented yet.")
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Try again.")


def start_new_game():
    name = input("Enter your name, brave adventurer: ")
    player = Player(name)

    # load Donjon-designed floor
    floor = import_donjon_floor("assets/maps/Floor 1/Dungeon Deep Floor 1 01.json")

    # Place player in safe starting room
    player.position = next(iter(floor.rooms))
    player.discovered_positions.add(player.position)

    engine = GameEngine(player, floor)

    # Caretaker intro
    caretaker = get_caretaker()
    print("\nAs you awaken, a hooded figure approaches...")
    print(caretaker.talk())

    while True:
        cmd = input("\n(Type 'altar' to place your hand, or 'look' to inspect the room): ").lower()
        if cmd == "altar":
            print("\nYou place your hand on the altar. A warm glow surrounds you...")
            choose_class(player)
            break
        elif cmd == "look":
            print("You see a stone altar glowing faintly.")
            print("You also see:")
            print(caretaker.look())
        else:
            print("Unknown command.")

    print("\n--- Your journey begins! ---")
    engine.render_current_room()

    # Game loop
    while engine.running:
        command = input("\n[Type direction (n/s/e/w/up/down), or 'q' to quit]: ")
        engine.process_input(command)

    print("Thanks for playing!")


def main():
    choice = main_menu()
    if choice == "new":
        start_new_game()


if __name__ == "__main__":
    main()
