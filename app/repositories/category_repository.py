from sqlalchemy.orm import Session
from app.models.categories import Category
from typing import Optional
from app.repositories.base_repository import BaseRepository

class CategoryRepository(BaseRepository[Category]):
    def __init__(self, db: Session):
        super().__init__(db, Category)

    def get_by_name(self, name :str) -> Optional[Category]:
        category_obj = self._db.query(Category).filter(Category.name == name).first()
        return category_obj

