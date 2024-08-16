from fastapi import APIRouter, Body
from ..models.Pokemon import Pokemon

user_route = APIRouter()

@user_route.post("/pokemon/")
def create_users(user: Pokemon = Body(...)):
    try:
        return pokemon
    except Exception as e:
        print(e)
        return {"error": str(e)}

@user_route.get("/Pokemon/")
def get_pokemon():
    return "Amo a la eam"
