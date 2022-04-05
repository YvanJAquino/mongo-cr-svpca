import os
import httpx
from fastapi import FastAPI, HTTPException
from models import DadJoke, DadJokes
from jokes import Joker
from state import MongoManager

_DB_HOST = os.environ.get("_DB_HOST")
_DB_PORT = os.environ.get("_DB_PORT")
_DB_NAME = os.environ.get("_DB_NAME")
_DB_COLL = os.environ.get("_DB_COLL")

app = FastAPI()
client = httpx.AsyncClient()
joker = Joker(client)
mongo = MongoManager(_DB_HOST, _DB_PORT, _DB_NAME, _DB_COLL)

@app.get("/health")
async def health():
    return {'status': 200}

@app.post("/jokes")
async def create_joke():
    joke = await joker.get()
    mongo.insert_one(joke)
    return joke
    
@app.get("/jokes/{joke_id}")
async def read_joke(joke_id: str):
    joke = mongo.find_one_by_id(joke_id)
    if not joke:
        raise HTTPException(status_code=404, detail=f"Joke {joke_id} not found")
    return joke

@app.get("/jokes")
async def list_jokes():
    return mongo.find_all()

@app.put("/jokes/{joke_id}")
async def update_joke(joke_id: str, joke: DadJoke):
    return mongo.replace_one(joke)

@app.delete("/jokes/{joke_id}", status_code=204)
async def delete_joke(joke_id: str):
    deleted = mongo.delete_one(joke_id)
    if deleted:
        return {"id": joke_id, "status": "deleted"}
    else:
        raise HTTPException(status_code=404, detail=f"Joke {joke_id} was not deleted")
