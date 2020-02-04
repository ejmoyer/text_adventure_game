from rooms import *
from os.path import exists

class Map(object):

    def __init__(self, start):
        self.current_scene = start

    def change_scene(self, scene_name):
        self.previous_scene = self.current_scene
        self.current_scene = scene_name

class Engine(object):

    def __init__(self, map):
        self.map = map

    def run(self):

        if exists('save.txt') == False: #make it save an external file and check for its existence
            self.map = RoomOne()
            print("Welcome to my game! Say 'OBSERVE' to get your bearings!")
            current_number = '1'
            self.map.actions()
        else:
            save_file = open('save.txt', 'r')
            current_number = save_file.readline()
            #self.map = 
            #self.map.actions()

        while self.map != 'end':

            if self.map.next_action == 'OBSERVE':
                self.map.desc()
                self.map.actions()

            elif self.map.next_action == 'SAVE':
                save_file = open('save.txt', 'w')
                save_information = f"{current_number}\n {self.map}"

                save_file.write(save_information)
                save_file.close()
                break

            elif self.map.next_action == 'CHANGE ROOM':
                answer = input("What room? 1, 2 or 3? ")

                if answer == current_number:
                    print("I am already here.")

                elif answer == '1':
                    self.map = RoomOne()
                    current_number = '1'
                    self.map.actions()

                elif answer == '2':
                    self.map = RoomTwo()
                    current_number = '2'
                    self.map.actions()

                elif answer == '3':
                    self.map = RoomThree()
                    current_number = '3'
                    self.map.actions()
                    break

                else:
                    print("That room doesn't exist.")

            elif self.map.next_action == 'HELP':
                print("""
                OBSERVE describes your surroundings,
                SAVE saves your progress. CHANGE ROOM will
                let you move around the map. HELP will display
                this message.
                """)
                self.map.actions()

            else:
                print("Error!")
                break

    #    if self.map.final_answer == "Life and Death" or "Life, Death" or "Life Death":
    #        self.map = FinalRoom()
    #        self.map.desc()
    #        self.map = 'end'
    #    else:
    #        print("The room fills with fire and you burn to death.")

        #allow for input
        #change scene depending on input
