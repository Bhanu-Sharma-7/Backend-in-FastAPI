from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut
from services.user import (
    create_user,
    get_all_users,
    get_user_by_id,
    delete_user,
    update_user
)
from database.connection import get_db

router = APIRouter()

@router.post('/user', response_model=UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/users/", response_model=list[UserOut])
def fetch_all_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{user_id}", response_model=UserOut)
def fetch_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    success = delete_user(user_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.put("/users/{user_id}", response_model=UserOut)
def modify_user(user_id: int, updated_data: UserCreate, db: Session = Depends(get_db)):
    user = update_user(user_id, updated_data, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user