from pydantic import BaseModel
import pymongo
from fastapi import FastAPI
import uvicorn
import sys
sys.path.append("C:\\Users\\selva\\OneDrive\\Desktop\\zoo_fastapi\\")
from src.zoo_schema import animal_serial


client=pymongo.MongoClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
mydata=client['mydatabase']
mycollection=mydata['Animals_collection']

def get_collection():
    return mycollection
    

app=FastAPI()

class Animals(BaseModel):
    roll_no:int
    Animal_name:str
    age:int
    gender:str

@app.get('/api/',tags=['Animals'])
def view_all():
    try:
        col = get_collection()
        val_animal =  animal_serial(col.find())
        return val_animal

        
    except Exception as e:
        print("error on viewing data " +str(e))

@app.get('/api/viewanimal/{roll_no}',tags=['Animals'])
def view_det(roll_no):
    try:
        col = get_collection()
        
        output=animal_serial(col.find({"roll_no":int(roll_no)}))
        return {"status": "ok","data":output}
        
    except Exception as e:
        print("error on viewing data " +str(e))
    

@app.post('/api/addanimal/',tags=['Animals'])
def add_det(animal : Animals):
    try:
        mycollection.insert_one(animal.dict())
        return {"data":"Successfully added"}
    except Exception as e:
        print("error on add data " +str(e))


@app.delete('/api/deleteanimal/{roll_no}',tags=['Animals'])
def delete(roll_no):
    try:
        mycollection.delete_many({"roll_no":int(roll_no)})
        return {"data":"Successfully deleted"}
    except Exception as e:
        print("error on viewing data " +str(e))


@app.put('/api/update/{roll_no}',tags=["Animals"])
def update(roll_no,student:Animals):
    try:
        
        userip=dict(student)
        
        mycollection.update_many({"roll_no":int(roll_no)},{"$set":userip})

        return animal_serial(mycollection.find({"roll_no":roll_no}))

    except Exception as e:
        print("error on viewing data " +str(e))

if __name__=='__main__':
    uvicorn.run("zoo_app:app",reload=True,access_log=False)