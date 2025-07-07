from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate

def create_user(user: UserCreate, db: Session):
    db_user = User(
        name = user.name,
        email = user.email
    )

    db.add(db_user)
    db.commit()

    return db_user

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def update_user(user_id: int, updated_data: UserCreate, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = updated_data.name
        user.email = updated_data.email
        db.commit()
        db.refresh(user)
        return user
    return None