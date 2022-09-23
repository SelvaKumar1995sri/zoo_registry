from pydantic import BaseModel
from typing import List
import pymongo
from fastapi import FastAPI,Request
import uvicorn
import sys
sys.path.append("C:\\Users\\selva\\OneDrive\\Desktop\\zoo_fastapi\\")


client = pymongo.MongoClient(
    "mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
mydata = client['mydatabase']
mycollection = mydata['Animals_collection']


def get_collection():
    return mycollection


app = FastAPI()


class Animals(BaseModel):
    roll_no: int
    Animal_name: str
    age: int
    gender: str
    

class AnimalsList(BaseModel):
    data: List[Animals]


def animal_list_serialiazer(animal_list):
    return [animal.dict() for animal in animal_list]


@app.get('/api', tags=['Animals'])
def view_all():
    try:
        col = get_collection()
        val_animal = list(col.find({},{"_id":0}))
        return {"data":val_animal}
    except Exception as e:
        print("error on viewing data " + str(e))


@app.get('/api/viewanimal/{roll_no}', tags=['Animals'])
def view_det(roll_no):
    try:
        col = get_collection()

        output = list(col.find({"roll_no": int(roll_no)},{"_id":0}))
        return {"status": "ok", "data": output}

    except Exception as e:
        print("error on viewing data " + str(e))


@app.post('/api/addanimal/', tags=['Animals'])
def add_det(animal: Animals):
    try:
        col = get_collection()
        col.insert_one(animal.dict())
        return {"status": 200, "data": "Successfully added"}
    except Exception as e:
        print("error on add data " + str(e))


@app.post('/api/addanimals/', tags=['Animals'])
def add_many(request : AnimalsList):
    try:

        col = get_collection()
        tour_list = animal_list_serialiazer(request.data)
        col.insert_many(tour_list)
        return {"status": 200, "data": "Successfully added"}
    except Exception as e:
        print("error on add data " + str(e))


@app.delete('/api/deleteanimal/{roll_no}', tags=['Animals'])
def delete(roll_no):
    try:
        col = get_collection()
        col.delete_many({"roll_no": int(roll_no)})
        return {"data": "Successfully deleted"}
    except Exception as e:
        print("error on viewing data " + str(e))


@app.put('/api/update/{roll_no}', tags=["Animals"])
def update(roll_no, student: Animals):
    try:
        col = get_collection()
        userip = dict(student)
        col.update_many({"roll_no": int(roll_no)}, {"$set": userip})

        return {"data": "Successfully deleted"}

    except Exception as e:
        print("error on viewing data " + str(e))


if __name__ == '__main__':
    uvicorn.run("zoo_app:app", reload=True)
