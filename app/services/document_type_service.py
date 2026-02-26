from typing import List
from sqlalchemy.orm import Session
# from app.models.documentTypes import DocumentType
from app.repositories.document_types_repository import DocumentTypeRepository
from app.core.exceptions import NotFoundError, ValidationError
from pydantic import ValidationError as PydanticError
from app.schemas.document_type_schema import DocumentTypeCreate, DocumentTypeUpdate,DocumentTypeResponse


class DocumentTypeService:
    def __init__(self, db: Session):
        self._db = db
        self._repo = DocumentTypeRepository(db)

    def create_doct_type(self, doct_type_data: dict) -> DocumentTypeResponse:  # Retornamos el Schema de salida
        try:

            validated_data = DocumentTypeCreate(**doct_type_data)

            # 2. Lógica de negocio (Verificar duplicados)
            if self._repo.get_by_code(validated_data.code):
                raise ValidationError(f"El tipo de documento '{validated_data.code}' ya existe.")

            # 3. Preparar datos para la DB
            db_data = validated_data.model_dump()

            # 5. Persistencia
            new_doct_type_obj = self._repo.create(db_data)

            return DocumentTypeResponse.model_validate(new_doct_type_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)


    def update_doct_type(self, doct_type_id: int, doct_type_data: dict) -> DocumentTypeResponse:
        try:
            # 1. Validar entrada
            validated_data = DocumentTypeUpdate(**doct_type_data)

            # 2. Buscar si existe el usuario original
            doct_type_obj = self._repo.get_by_id(doct_type_id)
            if not doct_type_obj:
                raise NotFoundError(f"El tipo de documento {doct_type_id} no existe.")

            # 3. Detectar cambios reales (exclude_unset)
            clean_update_data = validated_data.model_dump(exclude_unset=True)

            if not clean_update_data:
                raise ValidationError("No se enviaron datos válidos para actualizar.")

            updated_doct_type_obj = self._repo.update(doct_type_obj, clean_update_data)

            # 5. Actualizar en el repositorio
            updated_user_obj = self._repo.update(doct_type_obj, clean_update_data)

            return DocumentTypeResponse.model_validate(updated_user_obj)

        except PydanticError as e:
            raise ValidationError.from_pydantic(e)

    def get_all_doct_type(self, page: int = 1, limit: int = 20) -> List[DocumentTypeResponse]:
        doct_types = self._repo.get_all(page=page, limit=limit)
        return [DocumentTypeResponse.model_validate(doct_type) for doct_type in doct_types]


    def get_next_sequence_formatted(self, doct_type_id: int) -> str:
        # 1. BLOQUEO (Llama al Repo con el candado
        doc_type = self._repo.get_for_increment(doct_type_id)

        if not doc_type:
            raise ValidationError("Tipo de documento no existe.")

        # Convierte el número 5 en "F001-00000005"
        formatted_number = f"{doc_type.sequence_prefix}-{str(doc_type.next_sequence).zfill(8)}"

        # Incrementamos el contador para la siguiente venta
        doc_type.next_sequence += 1

        self._repo.save_changes(doc_type)
        # NOTA: No hacemos commit aquí, el commit se hace cuando la Venta se guarda
        return formatted_number



