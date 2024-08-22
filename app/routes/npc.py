from fastapi import APIRouter, Body
from ..models.Npc import Npc

npc_route = APIRouter()

@npc_route.post("/npc/")
def create_npc(npc: Npc = Body(...)):
    try:
        return npc
    except Exception as e:
        print(e)
        return {"error": str(e)}

@npc_route.get("/npc/")
def get_npc():
    return "Amo a la eam"