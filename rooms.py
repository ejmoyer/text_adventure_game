# use inheritance at least once
# one class per room
class Room(object):

    def __init__(self):
        self.instructions = """
        OBSERVE describes your surroundings,
        SAVE saves your progress. CHANGE ROOM will
        let you move around the map. HELP will display
        this message.
        """

    def desc(self):
        self.keyword = None
        print("Enter room info here.")

    def actions(self):
        self.next_action = input("OBSERVE, SAVE, CHANGE ROOM, HELP ")

class RoomOne(Room):

    def desc(self):
        self.keyword = 'life'
        print("Room One Description")

class RoomTwo(Room):

    def desc(self):
        self.keyword = 'death'
        print("Room Two Description")

class RoomThree(Room):

    def desc(self):
        #self.final_answer = None
        print("Room Three Description")
        #self.final_answer = input("""In existance, only two things are in balance.
        #Speak truth, and pass. Speak falsehood, and be judged. """)

class FinalRoom(Room):
    def desc(self):
        print("Final Room Description")
