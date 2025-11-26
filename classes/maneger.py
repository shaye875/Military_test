class Maneger:
    soldiers_in_rooms = []
    soldiers_waiting = []
    houses = []

    @classmethod
    def add_soldier_in_romms(cls,soldier):
        cls.soldiers_in_rooms.append(soldier)


    @classmethod
    def add_waiting(cls,soldier):
        cls.soldiers_waiting.append(soldier)

    @classmethod
    def add_houses(cls,house):
        cls.houses.append(house)
