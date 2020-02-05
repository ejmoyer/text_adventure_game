from rooms import *
from os.path import exists
from sys import exit

class Map(object):

    rooms = {
        'portal': RoomOne('portal'),
        'overgrown area': RoomTwo('overgrown area'),
        'dead end': RoomThree('dead end')
    }

    def __init__(self, start):
        self.current_room = Map.rooms.get(start)

    def change_scene(self, room_name):
        self.current_room = Map.rooms.get(room_name)
        print(self.current_room)

class Engine(object):

    def __init__(self, map):
        self.map = map

    def run(self):

        print("""
        Welcome to my game!
        Type NEW to start a new game.
        Type LOAD to load a previous save.
        Type CREDITS to see who made this game!
        Type EXIT to exit the game.""")

        start_question = input("> ")

        if start_question == "NEW":
            print("Type 'OBSERVE' to get your bearings!")
            self.map.current_room.actions()

        elif start_question == "LOAD":
            if exists('save.txt') == True: #make it save an external file and check for its existence
                save_file = open('save.txt', 'r')
                self.map.current_room = Map.rooms.get(save_file.readline())
                self.map.current_room.actions()

        elif start_question == "EXIT":
            exit()

        else:
            print('Error!')

        while self.map != 'end':

            if self.map.current_room.next_action == 'OBSERVE':
                self.map.current_room.desc()
                self.map.current_room.actions()

            elif self.map.current_room.next_action == 'SAVE':
                save_file = open('save.txt', 'w')
                save_information = f"{self.map.current_room.room_name}"

                save_file.write(save_information)
                save_file.close()
                break

            elif self.map.current_room.next_action == 'CHANGE ROOM':
                next_room = input("PORTAL, OVERGROWN AREA, DEAD END ").lower()
                self.map.change_scene(next_room)
                self.map.current_room.actions()

            elif self.map.current_room.next_action == 'HELP':
                print("""
                OBSERVE describes your surroundings,
                SAVE saves your progress. CHANGE ROOM will
                let you move around the map. HELP will display
                this message.
                """)
                self.map.current_room.actions()

            else:
                print("Error!")
                break

    #    if self.map.current_room.final_answer == "Life and Death" or "Life, Death" or "Life Death":
    #        self.map = FinalRoom()
    #        self.map.current_room.desc()
    #        self.map = 'end'
    #    else:
    #        print("The room fills with fire and you burn to death.")

        #allow for input
        #change scene depending on input
