# use inheritance
from engine import Engine

# one class per room
class BaseRoom(object):
    self.keyword = None

    def observe_room(self, description):
        print(description)

class RoomOne(BaseRoom):
    self.keyword = 'life'
    super(RoomOne, self).observe_room(
    """Dummy Text"""
    )

class RoomTwo(BaseRoom):
    self.keyword = 'begins'

class RoomThree(BaseRoom):
    self.keyword = 'here'

class FinalRoom(BaseRoom):
    pass

game = Engine()
game.run()
