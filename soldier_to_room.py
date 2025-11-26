from classes.soldier import Soldier
from classes.dwelling_house import DwellingHouse

def obj_soldier(id:int,first_name:str,last_name:str,gender:str,city:str,distance_base:int):
    soldier = Soldier(id,first_name, last_name, gender, city, distance_base)
    return soldier

def obj_house(rooms:int,each_room:int):
    house = DwellingHouse(rooms,each_room)
    return house

def buot(list:list[int]):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] < list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

    return list


def lists_vacant_and_waiting(soldiers:list,houses:list):
    vacant = []
    waiting = []
    distance_base = []
    for soldier in soldiers:
        distance_base.append(soldier.distance_base)
    distance_base = buot(distance_base)
    count =0
    for house in houses:
        count+=house.vacant
    while len(vacant) < count:
        for soldier in soldiers:
            if soldier.distance_base == distance_base[0]:
                soldier.set_placement(True)
                distance_base.pop(0)
                vacant.append(soldier)
                break

    for soldier in soldiers:
      if distance_base:
        if soldier.distance_base == distance_base[0]:
            waiting.append(soldier)
            distance_base.pop(0)
    return [vacant,waiting]













