import pymongo

from client_db import ClientDB
from datetime import datetime


class CompaniesCollection(ClientDB):

    def __init__(self):
        super().__init__()
        self.collection = self.db.linkedin_companies

    def first(self):
        return self.collection.find_one({}, sort=[('_id', pymongo.ASCENDING)])

    def find_by_linkedin(self, linkedin):
        return self.collection.find_one({'linkedin': linkedin})

    def get_next(self, linkedin):
        current = self.find_by_linkedin(linkedin)

        return self.collection.find_one({'_id': {'$gt': current['_id']}},
                                        sort=[('_id', pymongo.ASCENDING)])

    def insert(self, company):
        now = datetime.utcnow()

        return self.collection.insert_one(company, {
            '$setOnInsert': {'insertion_date': now},
            '$set': {'last_update_date': now}})

    def update(self, company):
        now = datetime.utcnow()

        return self.collection.update_one(
            {'linkedin': company['linkedin']},
            {'$set': {**company, 'last_update_date': now}},
            upsert=True
        )
