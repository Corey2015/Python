# -*- coding: utf-8
from pymongo import MongoClient


class mongoOP(object):
    def __init__(self):
        self.client = MongoClient(host="127.0.0.1", port=27017)
        self.collection = self.client["test"]["t252"]

    def insert(self, list):
        ret = self.collection.insert(list)
        print(ret)

    def query(self, list):
        ret = self.collection.find_one(list)
        print(ret)


def main():
    my_mongo = mongoOP()
    my_mongo.insert({"name": "xiaowang", "age": 18})
    my_mongo.query({"name": "xiaowang"})
    

if __name__ == "__main__":
    main()
