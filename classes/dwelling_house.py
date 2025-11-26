class DwellingHouse:
    def __init__(self,rooms:int,each_room:int):
        self.rooms = rooms
        self.each_rooms = each_room
        self.__vacant = self.rooms*self.each_rooms


    def __str__(self):
        return f"in this house have {self.rooms} rooms and {self.each_rooms} each room"

    @property
    def vacant(self):
        return self.__vacant



    #
