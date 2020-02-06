from rooms import Portal, Overgrown, Gate, Temple, Underworld
from os.path import exists
from sys import exit

class Map(object):

    rooms = { #contains room names for change_scene to use
        'portal': Portal('portal'),
        'overgrown area': Overgrown('overgrown area'),
        'dead end': Gate('dead end'),
        'deserted temple': Temple('deserted temple'),
        'machine underworld': Underworld('machine underworld')
    }

    def __init__(self, start):
        self.current_room = Map.rooms.get(start)

    def change_scene(self, room_name):
        """Changes the current scene to the argument given."""
        self.current_room = Map.rooms.get(room_name)

class Engine(object):

    def __init__(self, map):
        self.map = map

    def run(self):
        """Starts the game."""

        print("""
        Welcome to my game!
        Type NEW to start a new game.
        Type LOAD to load a previous save.
        Type EXIT to exit the game.""")

        start_question = input("> ")

        if start_question == "NEW":
            print("Type 'OBSERVE' to get your bearings!")
            self.map.current_room.take_action()

        elif start_question == "LOAD":
            if exists('save.txt') == True:
                save_file = open('save.txt', 'r')
                self.map.current_room = Map.rooms.get(save_file.readline())
                self.map.current_room.take_action()

        elif start_question == "EXIT":
            exit()

        else:
            print('Error!')

        while self.map != 'end':

            if self.map.current_room.next_action == 'OBSERVE':
                self.map.current_room.describe()
                self.map.current_room.take_action()

            elif self.map.current_room.next_action == 'SAVE':
                save_file = open('save.txt', 'w')
                save_information = f"{self.map.current_room.room_name}"

                save_file.write(save_information)
                save_file.close()
                break

            elif self.map.current_room.next_action == 'CHANGE ROOM':
                if self.map.current_room.room_name == 'portal':
                    next_room = input("""
                    PORTAL, OVERGROWN AREA, DESERTED TEMPLE,
                    MACHINE UNDERWORLD, DEAD END """).lower()
                else:
                    next_room = input("PORTAL ").lower()
                self.map.change_scene(next_room)
                self.map.current_room.take_action()

            elif self.map.current_room.next_action == 'HELP':
                print("""
                OBSERVE describes your surroundings,
                SAVE saves your progress. CHANGE ROOM will
                let you move around the map. HELP will display
                this message.
                """)
                self.map.current_room.take_action()

            elif self.map.current_room.next_action == 'EXIT':
                exit()

            else:
                print("Error!")
                break
