from pymongo import MongoClient

class dbConfig:
    def __init__(self):
      self.ip = 'localhost'
      self.port  = 27017
      self.connection = MongoClient(self.ip, 27017)
      self.table = self.connection.test_db.students
