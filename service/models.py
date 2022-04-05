from typing import Optional, List
from pydantic import BaseModel

class DadJoke(BaseModel):
    id: str
    joke: str
    status: Optional[int]

class DadJokes(BaseModel):
    jokes: List[Optional[DadJoke]]