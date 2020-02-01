from rooms import *

class Map(object):

    def __init__(self, start):
        self.current_scene = start

    def change_scene(self, scene_name):
        self.previous_scene = self.current_scene
        self.current_scene = scene_name

class Engine(object):

    def __init__(self, test):
        self.test = test

    def run(self):
        self.test = RoomOne()
        self.test.desc()

        while self.test != 'end':
            answer = input("What room? 2 or 3, 4? ")
            if answer == '2':
                self.test = RoomTwo()
                self.test.desc()
            elif answer == '3':
                self.test = RoomThree()
                self.test.desc()
            elif answer == '4':
                self.test = FinalRoom()
                self.test.desc()
                self.test = 'end'
            else:
                print("That room doesn't exist.")
        #allow for input
        #change scene depending on input
