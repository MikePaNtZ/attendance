from pymongo import MongoClient

class dbConfig:
    def __init__(self):
      self.ip = 'mb-creations.net'
      self.port  = 27017
      self.connection = MongoClient(self.ip, self.port)
      self.table = self.connection.test_db.students
