# use inheritance at least once
# one class per room
class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name

    def desc(self):
        self.keyword = None
        print("Enter room info here.")

    def actions(self):
        self.next_action = input("OBSERVE, SAVE, CHANGE ROOM, HELP, EXIT ")

class RoomOne(Room):

    def desc(self):
        print("Room One Description")

class RoomTwo(Room):

    def desc(self):
        print("Room Two Description")

class RoomThree(Room):

    def desc(self):
        print("Room Three Description")

    def actions(self):
        self.next_action = input("OBSERVE, APPROACH GATE, SAVE, CHANGE ROOM, HELP, EXIT ")
        if self.next_action == "APPROACH GATE":
            self.final_answer = input("""In existance, only two things are in balance.
            Speak truth, and pass. Speak falsehood, and be judged. """)

class FinalRoom(Room):
    def desc(self):
        print("Final Room Description")
