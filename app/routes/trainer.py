from fastapi import APIRouter, Body
from ..models.Trainer import Trainer

trainer_route = APIRouter()

@trainer_route.post("/trainer/")
def create_trainers(trainer: Trainer = Body(...)):
    try:
        return trainer
    except Exception as e:
        print(e)
        return {"error": str(e)}

@trainer_route.get("/trainer/")
def get_trainer():
    return "Amo a la eam"