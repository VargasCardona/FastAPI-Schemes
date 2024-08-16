from fastapi import APIRouter, Body
from ..models.User import User

user_route = APIRouter()

@user_route.post("/users/")
def create_users(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}

@user_route.get("/users/")
def get_user():
    return "Amo a la eam"