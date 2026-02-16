from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from sqlalchemy import String, Numeric, ForeignKey
from typing import TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from.documentTypes import DocumentType
    from .sales import Sale


class Invoice(Base):
    __tablename__ = 'invoices'
    document_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False) # F001-000123
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False) # Monto sin comisiones
    fee_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal('0.00')) #Comisiones credit card 4.5%
    total_paid: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False) # Monto total

    sale_id: Mapped[int] = mapped_column(ForeignKey('sales.id', ondelete="RESTRICT"), nullable=False)
    document_type_id: Mapped[int] = mapped_column(ForeignKey("document_types.id", ondelete="RESTRICT"),nullable=False )

    sale :Mapped["Sale"] = Relationship("Sale", back_populates="invoices")
    document_type:Mapped["DocumentType"] = Relationship("DocumentType", back_populates="invoices")

    def __repr__(self) -> str:
        return f"Invoice(document_number={self.document_number}, amount={self.total_paid})"



