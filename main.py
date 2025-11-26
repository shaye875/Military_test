from fastapi import FastAPI,File,UploadFile
from soldier_to_room import *
from classes.dwelling_house import DwellingHouse
import csv
import uvicorn
from classes.maneger import Maneger
from scllite import *

app = FastAPI()

@app.post('/assignWithCsv')
def import_csv(file:UploadFile = File()):
    with open(file.filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        soldiers = []
        for rwu in reader:
            soldiers.append(obj_soldier(int(rwu[0]),str(rwu[1]),str(rwu[2]),str(rwu[3]),str(rwu[4]),int(rwu[5])))
        house1 = DwellingHouse(10,8)
        house2 = DwellingHouse(10,8)
        Maneger.add_houses(house1)
        Maneger.add_houses(house2)
        lists = lists_vacant_and_waiting(soldiers,[house1,house2])
        json = {"vavcat":len(lists[0]),"waiting":len(lists[1])}
        for soldier in lists[0]:
            Maneger.add_soldier_in_romms(soldier)

        for soldier in lists[1]:
            Maneger.add_waiting(soldier)
        for list in lists:
            for soldier in list:
                json[soldier.first_name+" "+soldier.last_name] = f"have placas?:{soldier.placement}"
        return json


@app.get("/waitingLi")
def wait():
    list =  sorting_waiting(Maneger.soldiers_waiting)
    json = {}
    for soldier in list:
        json[soldier.first_name+" "+soldier.last_name] = soldier.distance_base

    return json


@app.get("/search/{id}")
def id_in_room(id):
    list = []
    list+=Maneger.soldiers_in_rooms
    list+=Maneger.soldiers_waiting
    for soldier in list:
        if soldier.id == id:
            return {soldier.id:soldier.placement}


@app.post("/initializeScheme")
def keeping_db(file:UploadFile = File()):
    with open(file.filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        conn = create_db_add_conected()
        cursor = conn.cursor()
        cursor.execute("create table soldier(id integer,first_name text,last_name text,gender text,city text,distance_base integer)")
        for row in reader:
           cursor.execute("insert into soldier (id,first_name,last_name,gender,city,distance_base)values(?,?,?,?,?,?)",row)
           conn.commit()
        cursor.execute("select * from soldier")
        return cursor.fetchall()





