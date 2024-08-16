from pydantic import BaseModel

class Npc(BaseModel):
    id: int
    name: str
    base_dialog: str 
    is_defeated: bool

