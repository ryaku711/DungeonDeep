from colorama import Fore, Style, init
init(autoreset=True)


class GameEngine:
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.running = True

    def render_current_room(self):
        room = self.world.get_room(self.player.position)
        if room:
            room.visited = True
            print(f"\n{room.description}")

            # Print exits
            exits = self.world.get_exits(self.player.position)
            exit_strings = []
            for direction, status in exits.items():
                if status == "open":
                    exit_strings.append(direction)
                elif status == "locked":
                    exit_strings.append(f"({direction})")
            if exit_strings:
                print(f"[Exits: {', '.join(exit_strings)}]")
            else:
                print("[No visible exits]")

            if room.type == "enemy":
                print("You sense danger... maybe a fight is coming.")
            elif room.type == "treasure":
                print("You might want to investigate!")
            elif room.type == "trap":
                print("Better watch your step.")
        else:
            print("\nYou cannot go that way.")

    def process_input(self, command):
        command = command.lower().strip()

        movement = {
            "n": (0, -1), "north": (0, -1),
            "s": (0, 1), "south": (0, 1),
            "e": (1, 0), "east": (1, 0),
            "w": (-1, 0), "west": (-1, 0),
        }

        if command in movement:
            dx, dy = movement[command]
            new_pos = (self.player.position[0] + dx, self.player.position[1] + dy)
            if self.world.get_room(new_pos):
                self.player.move(dx, dy)  # ✅ use the player's move method
                self.render_current_room()
            else:
                print("\nYou can't go that way.")
        elif command in ("u", "up", "d", "down"):
            print("\nThere's no staircase here.")
        elif command == "q":
            self.running = False
        elif command == "status":
            self.show_status()
        elif command == "map":
            self.render_minimap()
        else:
            print("\nUnknown command. Try 'north', 'n', 'east', 'e', etc.")

    def show_status(self):
        print(f"\n{self.player.name}'s Status")
        print(f"HP: {self.player.hp}/{self.player.max_hp}")
        print("Stats:")
        for stat, value in self.player.stats.items():
            print(f"  {stat}: {value}")

    def render_minimap(self, size=5):
        px, py = self.player.position
        half = size // 2

        print("\n[Minimap]")
        for y in range(py - half, py + half + 1):
            room_row = ""
            conn_row = ""

            for x in range(px - half, px + half + 1):
                pos = (x, y)
                room = self.world.get_room(pos)

                # Room layer (top line)
                if pos == self.player.position:
                    room_row += Fore.CYAN + "[X]" + Style.RESET_ALL
                elif pos in self.player.discovered_positions and room:
                    if room.type == "enemy":
                        room_row += Fore.RED + "[!]" + Style.RESET_ALL
                    elif room.type == "treasure":
                        room_row += Fore.YELLOW + "[?]" + Style.RESET_ALL
                    elif room.type == "safe":
                        room_row += Fore.GREEN + "[S]" + Style.RESET_ALL
                    elif room.type == "boss":
                        room_row += Fore.MAGENTA + "[B]" + Style.RESET_ALL
                    else:
                        room_row += Fore.WHITE + "[ ]" + Style.RESET_ALL
                else:
                    room_row += "   "

                # East connection
                if x < px + half:
                    east_pos = (x + 1, y)
                    if (
                            pos in self.player.discovered_positions
                            and east_pos in self.player.discovered_positions
                            and self.world.get_room(east_pos)
                            and self.world.get_room(pos)
                    ):
                        room_row += Fore.WHITE + "-" + Style.RESET_ALL
                    else:
                        room_row += " "

            print(room_row)

            # South connections (between rows)
            if y < py + half:
                for x in range(px - half, px + half + 1):
                    south_pos = (x, y + 1)
                    if (
                            (x, y) in self.player.discovered_positions
                            and south_pos in self.player.discovered_positions
                            and self.world.get_room((x, y))
                            and self.world.get_room(south_pos)
                    ):
                        conn_row += Fore.WHITE + " | " + Style.RESET_ALL
                    else:
                        conn_row += "   "

                    if x < px + half:
                        conn_row += " "

                print(conn_row)
