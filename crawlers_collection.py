import pymongo

from client_db import ClientDB


class CrawlersCollection(ClientDB):

    def __init__(self):
        super().__init__()
        self.collection = self.db.linkedin_crawlers

    def last(self):
        return self.collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])

    def update(self, letter, page, sub_page):
        self.collection.update_one({},
                                   {'$set': {'letter': letter,
                                             'page': page,
                                             'sub_page': sub_page}},
                                   upsert=True)
