from fastapi import FastAPI
from starlette.responses import RedirectResponse

# App routes
from .routes.user import user_route

# app instance
app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# -------- Usuario --------
app.include_router(user_route, prefix="/users", tags=["Usuarios"])