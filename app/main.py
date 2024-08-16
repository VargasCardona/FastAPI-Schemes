from fastapi import FastAPI
from starlette.responses import RedirectResponse

# App routes
from .routes.pokemon import pokemon_route

# app instance
app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# -------- Usuario --------
app.include_router(pokemon_route, prefix="/pokemon", tags=["Pokemon"])
