from fastapi import FastAPI
from starlette.responses import RedirectResponse

# App routes
from .routes.pokemon import pokemon_route
from .routes.trainer import trainer_route
from .routes.npc import npc_route
from .routes.item import item_route
from .routes.stats import stats_route

# app instance
app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# -------- Usuario --------
app.include_router(pokemon_route, prefix="/pokemon", tags=["Pokemon"])
app.include_router(trainer_route, prefix="/trainer", tags=["Trainer"])
app.include_router(npc_route, prefix="/npc", tags=["Npc"])
app.include_router(item_route, prefix="/item", tags=["Item"])
app.include_router(stats_route, prefix="/stats", tags=["Stats"])