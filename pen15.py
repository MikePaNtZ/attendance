from pymongo import MongoClient
from dbConfig import dbConfig

class Student:
    def __init__(self):
        self.attended = False
        self.average = 0
        self.db = dbConfig()
        self.studentTable = self.db.table

    def sendToDb(self):
        jsonifyData = {
                     'attended' : self.attended,
                     'average'  : self.average
                    }
        self.studentTable.insert(jsonifyData)
