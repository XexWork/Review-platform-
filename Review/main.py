from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import models
from app.database import engine
from app.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
