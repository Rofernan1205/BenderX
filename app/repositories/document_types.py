from sqlalchemy.orm import Session
from app.models.documentTypes import DocumentType
from typing import Optional

class DocumentTypeRepository:

    def __init__(self, db: Session):
        self._db = db

    def create(self, doct_type_data : dict) -> DocumentType:
        doct_type = DocumentType(**doct_type_data)
        self._db.add(doct_type)
        self._db.flush()
        return doct_type

    def update(self, doct_type_obj : DocumentType, doct_type_clean: dict) -> DocumentType :
        for key, value in doct_type_clean.items():
            if hasattr(doct_type_obj, key):
                setattr(doct_type_obj, key, value)
        self._db.flush()
        self._db.refresh(doct_type_obj)
        return doct_type_obj

    def get_by_id(self, doct_type_id : int) -> Optional[DocumentType] :
        doct_type_obj = self._db.query(DocumentType).filter(DocumentType.id == doct_type_id).first()
        return doct_type_obj

    def get_by_name(self, doct_type_name : str) -> Optional[DocumentType] :
        doct_type_name = self._db.query(DocumentType).filter(DocumentType.name == doct_type_name).first()
        return doct_type_name

    def get_all(self, page: int , limit: int) -> list[type[DocumentType]] :
        skip = (page - 1)* limit
        return self._db.query(DocumentType).offset(skip).limit(limit).all()





