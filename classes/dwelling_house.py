class DwellingHouse:
    def __init__(self,rooms:int,each_room:int):
        self.rooms = rooms
        self.each_rooms = each_room
        self.__vacant = self.rooms*self.each_rooms

    def __str__(self):
        return f"in this house have {self.rooms} rooms and {self.each_rooms} each room"

    @property
    def vacant(self):
        if self.__vacant > 0:
            return True
        return False

    def set_vacant(self):
        self.__vacant-=1

    def soldier_in_house(self):
        vacant = self.vacant
        if vacant:
            self.set_vacant()
            return True
        return False