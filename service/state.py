import pymongo
from models import DadJoke, DadJokes


class MongoManager:

    def __init__(self, host, port, name, coll):
        self.host = host
        self.port = port if type(port) == int else int(port) 
        self.name = name
        self._coll = coll
        self.cnst = f'mongodb://{self.host}:{self.port}/'
        self.client = pymongo.MongoClient(self.cnst)
        self.db = self.client[self.name]
        self.coll = self.db[self._coll]

    def insert_one(self, joke: DadJoke):
        joke = joke.dict(exclude_none=True)
        _id = joke.pop("id")
        joke.update({"_id": _id})
        return self.coll.insert_one(joke)

    def find_one_by_id(self, joke_id: str):
        joke = self.coll.find_one({"_id": joke_id})
        if not joke:
            return None

        _id = joke.pop("_id")
        joke.update({"id": _id})        
        return DadJoke(**joke)
        
    def find_all(self):
        jokes = []
        for joke in self.coll.find():
            joke["id"] = joke.pop("_id")
            jokes.append(DadJoke(**joke))
        return DadJokes(jokes=jokes)

    def replace_one(self, joke):
        joke = joke.dict(exclude_none=True)
        joke["_id"] = joke.pop("id")
        self.coll.replace_one({"_id": joke["_id"]},joke)
        joke["id"] = joke.pop("_id")
        return DadJoke(**joke)

    def delete_one(self, joke_id):
        res = self.coll.delete_one({"_id": joke_id})
        return res.deleted_count == 1