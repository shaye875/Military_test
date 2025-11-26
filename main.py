from fastapi import FastAPI,File,UploadFile
from soldier_to_room import *
from classes.dwelling_house import DwellingHouse
import csv
import uvicorn
app = FastAPI()

@app.post('/assignWithCsv')
def import_csv(file:UploadFile = File()):
    with open(file.filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        soldiers = []
        for rwu in reader:

            soldiers.append(obj_soldier(int(rwu[0]),str(rwu[1]),str(rwu[2]),str(rwu[3]),str(rwu[4]),int(rwu[5])))
        houme1 = DwellingHouse(8,10)
        houme2 = DwellingHouse(8,10)
        lists = lists_vacant_and_waiting(soldiers,[houme1,houme2])
        json = {"vavcat":len(lists[0]),"waiting":len(lists[1])}

        for list in lists:
            for soldier in list:
                json[soldier.first_name+" "+soldier.last_name] = f"have placas?:{soldier.placement}"
        return json
