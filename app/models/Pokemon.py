from pydantic import BaseModel
from item import Item

class Pokemon(BaseModel):
    id: int
    name: str
    item: Item 
    stats: Stats

