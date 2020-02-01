from engine import Engine
# use inheritance
# one class per room
class BaseRoom(object):

    def __init__(self):
        self.keyword = None

class RoomOne(BaseRoom):
    pass

class RoomTwo(BaseRoom):
    pass

class RoomThree(BaseRoom):
    pass

class FinalRoom(BaseRoom):
    pass

game = Engine()
game.run()
