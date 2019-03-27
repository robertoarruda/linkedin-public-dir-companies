import pymongo

from client_db import ClientDB


class ScrapersCollection(ClientDB):

    def __init__(self):
        super().__init__()
        self.collection = self.db.linkedin_scrapers

    def last(self):
        return self.collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])

    def update(self, linkedin):
        self.collection.update_one({},
                                   {'$set': {'current': linkedin}},
                                   upsert=True)
