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

    def get_by_code(self, doct_type_code : str) -> Optional[DocumentType] :
        doct_type_code = self._db.query(DocumentType).filter(DocumentType.code == doct_type_code).first()
        return doct_type_code

    def get_by_active(self) -> list[type[DocumentType]]:
        doct_types = self._db.query(DocumentType).filter(DocumentType.is_active == True).all()
        return doct_types


    def get_all(self, page: int , limit: int) -> list[type[DocumentType]] :
        skip = (page - 1)* limit
        return self._db.query(DocumentType).offset(skip).limit(limit).all()

    def delete(self, document_type: DocumentType ) -> None :
        self._db.delete(document_type)
        self._db.flush()

    def get_for_increment(self, doct_type_id: int) -> Optional[DocumentType] :
        """
        Bloquea el registro en la DB hasta que termine la transacción.
        Esto evita que dos ventas obtengan el mismo número de factura.
        """
        return self._db.query(DocumentType).filter(DocumentType.id == doct_type_id).with_for_update().first()

    def save_changes(self, doct_type_data : DocumentType) -> DocumentType :
        self._db.add(doct_type_data)
        self._db.flush()
        self._db.refresh(doct_type_data)
        return doct_type_data







