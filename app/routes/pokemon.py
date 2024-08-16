from fastapi import APIRouter, Body
from ..models.Pokemon import Pokemon

pokemon_route = APIRouter()

@pokemon_route.post("/pokemon/")
def create_pokemons(pokemon: Pokemon = Body(...)):
    try:
        return pokemon
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pokemon_route.get("/pokemon/")
def get_pokemon():
    return "Amo a la eam"
