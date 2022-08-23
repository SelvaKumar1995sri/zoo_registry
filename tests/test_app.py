from urllib import response
from fastapi.testclient import TestClient
import unittest
import pytest
import json
from src.zoo_app import app

client = TestClient(app)

def get_test_profile():
    return json.load(open("test_add_animals.json","r"))
    

def test_view_all():
   response = client.get("/api/")
   assert response.status_code == 200

def test_view_det():
   response = client.get("/api/viewanimal/1")
   assert response.status_code == 200

def test_add():
    data = get_test_profile()
    response = client.post("/api/addanimal/",json= data)
    assert response.status_code == 200
    assert response.json() == {"data":"Successfully added"}

def test_delete():
    response = client.delete("/api/deleteanimal/3")
    assert response.status_code == 200
    assert response.json() == {"data":"Successfully deleted"}

def test_update():

   response = client.put("/api/update/1",data=json.dumps(get_test_profile()))
   assert response.status_code == 200
    