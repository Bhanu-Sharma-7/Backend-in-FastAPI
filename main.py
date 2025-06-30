from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from database import Sessionlocal
from models.user import User, UserEmail

app = FastAPI()

session = Sessionlocal()

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    password: str
    emails: Optional[List[str]] = []

class UserEmailResponse(BaseModel):
    id: int
    email: str
    user_id: int

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    addresses: List[UserEmailResponse] = []

    class Config:
        from_attributes = True

@app.get('/profile/{first_name}/', response_model=UserResponse)
def view_profile(first_name: str):
    user_obj = session.query(User).filter(User.first_name == first_name).first()
    if not user_obj:
        return {"message": "not found"}
    
    return {
        "id": user_obj.id,
        "first_name": user_obj.first_name,
        "last_name": user_obj.last_name,
        "addresses": user_obj.user_emails,
        "password": user_obj.password
    }

@app.post('/users/', response_model=UserResponse)
def create_user(user: UserCreate):
    email_objs = [UserEmail(email=e) for e in user.emails]
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.password,
        user_emails=email_objs 
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    usr_response = {
        "id": new_user.id,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "addresses": new_user.user_emails
    }
    return usr_response

@app.get('/')
def starting_page():
    return {"message": "FastAPI is running+++++"}
