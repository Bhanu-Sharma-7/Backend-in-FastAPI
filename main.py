from fastapi import FastAPI
from database.connection import engine, Base
from models.user import User
from routes.user import router as user_router


app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(user_router)

@app.get("/")
def home_page():
    return { "message": "This is home page of my curd application" }