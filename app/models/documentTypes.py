from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from .invoices import Invoice

class DocumentType(Base):
    __tablename__ = "document_types"
    # Validaciones no ve usuario final
    code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False) # "INVOICE", "RECEIPT", "CREDIT_NOTE"
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    # Prefijo o serie del comprobante.
    # Identifica la serie con la que se emiten los documentos.
    # Forma parte del número final del comprobante.
    # "F001" → F001-000123
    sequence_prefix: Mapped[str] = mapped_column(String(10), nullable=False)

    # Próximo número correlativo a emitir para esta serie.
    # Se incrementa automáticamente cada vez que se genera un comprobante.
    # Garantiza numeración ordenada y sin duplicados.
    # Ejemplo: 123 → genera F001-000123 y luego pasa a 124
    next_sequence: Mapped[int] = mapped_column(default=1)

    # Indica si este tipo de comprobante requiere obligatoriamente un cliente
    #   Factura → True (requiere cliente)
    #   Boleta → False (puede ser venta al público)
    requires_customer: Mapped[bool] = mapped_column(default=False)

    # Indica si este comprobante es una nota de crédito.
    # Se usa para devoluciones o anulación de ventas.
    # Afecta la lógica de stock y totales.
    # Ejemplo:
    #   Nota de crédito → True
    #   Factura / Boleta → False
    is_credit_note: Mapped[bool] = mapped_column(default=False)

    invoices : Mapped[List["Invoice"]] = relationship(back_populates="document_type")


    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.code}>"

