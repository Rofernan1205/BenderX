from sqlalchemy.orm import Session

from app.models.users import User

class UserRepository:
    def __init__(self, db: Session):
        self._db = db


    def get_by_id(self, id: int) -> User | None:
        return self._db.query(User).filter(User.id == id).first()


    def get_by_username(self, username: str) -> User | None:
        return self._db.query(User).filter(User.username == username).first()


    def get_all(self) -> list[type[User]]:
        return self._db.query(User).all()


    def create_user(self, user_data: dict) -> User | None:
        user = User(**user_data)
        self._db.add(user)
        self._db.flush()
        return user

    def update(self, user: User) -> User:
        """
        Recibe la CLASE (objeto ya modificado por el servicio).
        No necesitamos el dict aquí porque SQLAlchemy ya sabe qué cambió.
        """
        self._db.flush()
        self._db.refresh(user)
        return user


    def delete(self, user: User) -> None:
        self._db.delete(user)
        self._db.flush()
        






