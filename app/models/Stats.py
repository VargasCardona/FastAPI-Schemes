from pydantic import BaseModel

class Stats(BaseModel):
    ps: int
    vel: int
    atk: int
    defence: int
    atk_spec: int
    defence_spec: int
