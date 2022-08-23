from unittest.mock import patch
# from pytest_mongodb.plugin import mongo_engine
from pytest import mark
import pytest
import sys
from src.zoo_app import view_all, view_det

# @mark.skipif(mongo_engine() == 'mongomock', reason="mongomock does not support that")
class Test_MongoFunctions():


    @pytest.fixture(autouse=True,scope="function")
    def _get_mongo(self, mongodb):
        resp = mongodb.list_collection_names()
        self.mongodb = mongodb

    def test_one(self):
        resp = self.mongodb.list_collection_names()
        print(resp)
        val = list(self.mongodb.mycollection.find({}))
        assert val

    def test_view(self):
        with patch('src.zoo_app.get_collection') as mock_mongo:
            mock_mongo.return_value = self.mongodb.mycollection
            resp = view_all()
            assert resp
    
    def test_view_det(self):
            with patch('src.zoo_app.get_collection') as mock_mongo:
                mock_mongo.return_value = self.mongodb.mycollection
                resp = view_det(1)
                assert resp["data"][0]["Animal_name"] == 'Suriya'

