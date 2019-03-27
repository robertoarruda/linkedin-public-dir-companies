from pymongo import MongoClient


class ClientDB():

    __MONGO = 'mongodb://<user>:<password>@<host>:<port>'

    def __init__(self):
        client = MongoClient(self.__MONGO)
        self.db = client.intexfy_source
