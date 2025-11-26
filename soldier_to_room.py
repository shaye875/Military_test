from classes.soldier import Soldier
from classes.dwelling_house import DwellingHouse
from classes.dwelling_house_A import DwellingHouseA
from classes.dwelling_house_B import DwellingHouseB
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
    for house in houses:
        bool = house.soldier_in_house()
        if bool == True:
         for soldier in soldiers:
                  if soldier.distance_base == distance_base[0]:
                      soldier.set_placement(True)
                      vacant.append(soldier)
                      distance_base.pop(0)

        else:
            break

    for soldier in soldiers:
      if distance_base:
        if soldier.distance_base == distance_base[0]:
            waiting.append(soldier)
            distance_base.pop(0)
    return [vacant,waiting]



#
# def lists_vacant_and_waiting(soldiers:list,houses:list):
#     soldiers1 = soldiers
#     vacant =  []
#     waiting = []
#     while soldiers1:
#        max = 0
#        for item in soldiers1:
#
#         if item.distance_base > max:
#             max = item.distance_base
#             soldiers1.remove(item)
#        wait = True
#        for house in houses:
#         bool = house.soldier_in_house()
#         if bool == True:
#             wait = False
#             for item in soldiers:
#                 print(item.distance_base)
#                 if item.distance_base == max:
#                     item.set_placement(True)
#                     vacant.append(item)
#             break
#        if wait == True:
#         waiting+=soldiers1
#         soldiers1 = []
#     return [vacant,waiting]

s = Soldier(1,"w","r","d","s",6)
s1 = Soldier(1,"w","r","d","s",5)
s2 = Soldier(1,"w","r","d","s",4)
s3 = Soldier(1,"w","r","d","s",3)
a = DwellingHouse(1,2)
s4 = Soldier(1,"w","r","d","s",7)
print(lists_vacant_and_waiting([s,s1,s2,s3,s4],[a]))
# print(a.vacant)




