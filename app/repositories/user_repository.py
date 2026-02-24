from typing import Optional
from sqlalchemy.orm import Session
from app.models.users import User

class UserRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, user_data: dict) -> User:
        user = User(**user_data)
        self._db.add(user)
        self._db.flush()
        return user

    def update(self, user_obj : User, clean_data: dict) -> User :
        for key, value in clean_data.items():
            if hasattr(user_obj, key):
                setattr(user_obj, key, value)
        self._db.flush()
        self._db.refresh(user_obj)
        return user_obj

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> Optional[User]:
        return self._db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self._db.query(User).filter(User.email == email).first()

    def delete(self, user: User) -> None:
        self._db.delete(user)
        self._db.flush()

    def get_all(self, page:int , limit:int) -> list[type[User]]:
        skip = (page - 1) * limit
        return self._db.query(User).offset(skip).limit(limit).all()












