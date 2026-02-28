from typing import List
from sqlalchemy.orm import Session
from pydantic import ValidationError as PydanticError
from app.repositories.category_repository import CategoryRepository
from app.core.exceptions import ValidationError, NotFoundError
from app.schemas.category_schema import CategoryCreate, CategoryUpdate,CategoryResponse

class CategoryService:
    def __init__(self, db: Session):
        self._db = db
        self._rep = CategoryRepository(db)

    def create_category(self, category_data: dict) -> CategoryResponse:
        try:
            validated_data = CategoryCreate(**category_data)
            category_obj = self._rep.get_by_name(validated_data.name)
            if category_obj:
                raise ValidationError(F"La categoria {category_obj.name} ya existe")
            # Preparar datos para la DB
            db_data = validated_data.model_dump()
            new_category_obj = self._rep.create(db_data)
            return CategoryResponse.model_validate(new_category_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def update_category(self,category_id : int, category_data: dict ) -> CategoryResponse:
        try:
            validated_data = CategoryUpdate(**category_data)
            category_obj = self._rep.get_by_id(category_id)
            if not category_obj:
                raise NotFoundError(f'La categoria {category_id} no existe')

            # Preparar datos para la db
            clean_update_data = validated_data.model_dump(exclude_unset=True)
            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            update_category_obj = self._rep.update(category_obj, clean_update_data)
            return CategoryResponse.model_validate(update_category_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def get_category(self, category_id: int) -> CategoryResponse:
        category_obj = self._rep.get_by_id(category_id)
        if not category_obj:
            raise NotFoundError(f'La categoria {category_id} no existe')
        return CategoryResponse.model_validate(category_obj)

    def get_all_categories(self, page: int = 1, limit: int = 20) -> List[CategoryResponse]:
        categories = self._rep.get_all(page, limit)
        return [CategoryResponse.model_validate(category) for category in categories]


    def delete_category(self, category_id: int) -> None:
        category_obj = self._rep.get_by_id(category_id)
        if not category_obj:
            raise NotFoundError(f'La categoria {category_id} no existe')
        if category_obj.name == "General" and category_obj.id == 1:
            raise ValidationError(f"No se puede eliminar categoria {category_obj.name}")
        self._rep.delete(category_obj)
