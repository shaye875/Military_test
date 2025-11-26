class Soldier:
    def __init__(self,id:int,first_name:str,last_name:str,gender:str,city:str,distance_base:int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance_base = distance_base
        self.__placement = False

    @property
    def placement(self):
        return self.__placement

    def set_placement(self,bool:bool):
        self.__placement = bool




