from fastapi import FastAPI
from .routers import user, recipes, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(recipes.router)
app.include_router(user.router)
