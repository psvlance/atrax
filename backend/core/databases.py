import pymongo

from bson.json_util import dumps

from backend.core.settings import SETTINGS


class Database:
    def __init__(self):
        self.mongo = pymongo.MongoClient(SETTINGS.DATABASE_URL)
