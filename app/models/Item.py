from pydantic import BaseModel

from .Stats import Stats

class Item(BaseModel):
    id: int
    name: str
    details: str 
    stats: Stats
    sprite_route: str

