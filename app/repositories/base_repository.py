from typing import TypeVar, Generic, Type, Optional, List, Any, Dict
from sqlalchemy.orm import Session

# Definimos un Tipo Genérico vinculado a tus modelos
T = TypeVar('T') # Un Genérico (T) sirve para pasar TIPOS DE DATOS

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self._db = db
        self._model = model

    def create(self, obj_data: Dict[str, Any]) -> T:
        obj = self._model(**obj_data)
        self._db.add(obj)
        self._db.flush()
        return obj

    def update(self, obj: T, clean_data: Dict[str, Any]) -> T:
        for key, value in clean_data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        self._db.flush()
        self._db.refresh(obj)
        return obj

    def get_by_id(self, id: int) -> Optional[T]:
        # Suponemos que todos tus modelos tienen 'id' como PK
        return self._db.query(self._model).filter(self._model.id == id).first()

    def get_all(self, page: int  , limit: int  ) -> List[T]:
        skip = (page - 1) * limit
        return self._db.query(self._model).offset(skip).limit(limit).all()

    def delete(self, obj: T) -> None:
        self._db.delete(obj)
        self._db.flush()

    def save_changes(self, obj: T) -> T:
        """Para guardar cambios directos (como el incremento de secuencia)"""
        self._db.flush()
        self._db.refresh(obj)
        return obj