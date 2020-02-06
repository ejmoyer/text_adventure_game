from sys import exit

class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name

    def desc(self):
        print("Enter room info here.")

    def actions(self):
        self.next_action = input("OBSERVE, SAVE, CHANGE ROOM, HELP, EXIT ")

class RoomOne(Room):

    def desc(self):
        print("""
        A large connecting room, with many doors on all sides leading to
        other unknown realms. In the center lies an ancient statue, it's head
        and right arm missing. It's left arm is broken off and laying to the
        side, with a small broken scale in hand.
        """)

    def actions(self):
        self.next_action = input("OBSERVE, EXAMINE STATUE, SAVE, CHANGE ROOM, HELP, EXIT ")
        if self.next_action == "EXAMINE STATUE":
            print("""
            The statue looks like an ancient deity worshipped by
            this realm's inhabitants. It resembles a giant humanoid, half of
            the statue being a skeleton, the other half with skin and looking
            much more human. The inscription reads 'Taviin, God of Balance'.
            """)
            self.actions()
        else:
            pass


class RoomTwo(Room):

    def desc(self):
        print("""
        The area has a huge tree in the center, with a large
        hole bored into the center of it, looks like some sort of
        energy in the middle of the hole. The rest of the area is
        overgrown and covered in roots from the large tree.""")

    def actions(self):
        self.next_action = input("OBSERVE, EXAMINE TREE, SAVE, CHANGE ROOM, HELP, EXIT ")
        if self.next_action == 'EXAMINE TREE':
            print("""
            The tree seems to maintain the entire environment
            offering all the needed resources for plants to grow. However,
            there is a shaded area in the far corner of the room where
            plants are shriveled and it is noticibly colder. A skull is
            formed by the energy in the hole of the tree, maybe the tree
            is actually taking energy from the area instead?""")
            self.actions()
        else:
            pass

class RoomThree(Room):

    def desc(self):
        print("""
        A huge atrium with many gateways, every one of them broken, unusable.
        A rusted gate is at the end of the atrium, with glyphs imprinted
        in the walls surrounding it. One of the glyphs I can translate
        says 'LIFE'.
        """)

    def actions(self):
        self.next_action = input("OBSERVE, APPROACH GATE, SAVE, CHANGE ROOM, HELP, EXIT ")
        if self.next_action == "APPROACH GATE":
            self.answer_riddle = input("""
            The gate has an inscription..
            'In existance, only two things are in balance.
            Speak truth, and pass. Speak falsehood, and be judged.'
            ANSWER the question, or WALK away?
             """)

            if self.answer_riddle == 'ANSWER':
                self.final_answer = input("""
                 In existance, only two things are in balance.
                 Speak truth, and pass. Speak falsehood, and be judged.
                 """)
                if self.final_answer == "LIFE AND DEATH".casefold() or "DEATH AND LIFE".casefold():
                     print("""
                     My journey is at an end, I've reached the area beyond
                     death, where true godhood can be attained. I shall stay here and
                     meditate on myself, to work further towards enlightenment.
                     """)
                     exit()
                else:
                    print(f"""
                    The entire area shakes, and the ceiling caves in
                    upon you. Your last dying words are {final_answer}..
                    """)
                    exit()
            else:
                self.actions()
        else:
            pass

class RoomFour(Room):

    def desc(self):
        print("""
        The sand dunes span for miles, this temple is deserted, but the
        sound of chanting in the distance is carried by the wind. The
        statues look like the same statue in the middle of the portal room.
        """)

    def actions(self):
        self.next_action = input("OBSERVE, LISTEN CLOSER, SAVE, CHANGE ROOM, HELP, EXIT ")
        if self.next_action == 'LISTEN CLOSER':
            print("""
            You can hear the words 'beyond existence' in the chanting,
            perhaps the followers of the God of Balance attempted to
            ascend beyond this world somehow? Perhaps the chanting
            comes from those who accomplished their goal..
            """)
            self.actions()
        else:
            pass

class RoomFive(Room):

    def desc(self):
        print("""
        Wires span across the ceiling of this underground. The sound of
        metal moving throughout the tunnels of this area. The stench of
        death reminds you of how dangerous this area really is. A blinking
        light close to you draws your attention.
        """)

    def actions(self):
        self.next_action = input("OBSERVE, APPROACH LIGHT, SAVE, CHANGE ROOM, HELP, EXIT ")
        if self.next_action == 'APPROACH LIGHT':
            print("""
            The blinking light is attached to the body of a
            discarded robotic shell, a small broken status screen nearby
            displays 'IMBALANCE' in bright red letters.
            """)
            self.actions()
        else:
            pass
