from fastapi import APIRouter, Body
from ..models.Stats import Stats

stats_route = APIRouter()

@stats_route.post("/stats/")
def create_stats(stats: Stats = Body(...)):
    try:
        return stats
    except Exception as e:
        print(e)
        return {"error": str(e)}

@stats_route.get("/stats/")
def get_stats():
    return "Amo a la eam"