from fastapi import APIRouter, Body
from ..models.Item import Item

item_route = APIRouter()

@item_route.post("/item/")
def create_item(item: Item = Body(...)):
    try:
        return item
    except Exception as e:
        print(e)
        return {"error": str(e)}

@item_route.get("/item/")
def get_item():
    return "Amo a la eam"