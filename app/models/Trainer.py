from pydantic import BaseModel

from .Pokemon import Pokemon

class Trainer(BaseModel):
    id: int
    name: str
    party: Pokemon
    badges: str

