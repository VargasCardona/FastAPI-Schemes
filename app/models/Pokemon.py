from pydantic import BaseModel

from .Item import Item
from .Stats import Stats

class Pokemon(BaseModel):
    id: int
    name: str
    item: Item 
    stats: Stats
    sprite_route: str
