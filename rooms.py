# use inheritance at least once
# one class per room
class Room(object):

    def desc(self):
        self.keyword = None
        print("Enter room info here.")

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
        print("Room Three Description")

class FinalRoom(Room):
    def desc(self):
        print("Final Room Description")
