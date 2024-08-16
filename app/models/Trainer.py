from pydantic import BaseModel

class Trainer(BaseModel):
    id: int
    name: str
    party: Pokemon
    badges: str

