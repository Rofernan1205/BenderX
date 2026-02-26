
INITIAL_ROLES = ["Administrador", "Dueño", "Supervisor", "Cajero"]

INITIAL_BRANCH = {"name": "ApuByte SAC",
                "phone": "946566438",
                "email": "apubyte@hotmail.com"}

SUPER_USER = {
    "name": "Rodrigo",
    "last_name": "Fernandez",
    "email": "medina-1997@hotmail.com",
    "password": "Rofernan1997",
    "dni": "71114855",
    "username": "rofernan",
    "phone": "946566438"
}

DOCUMENT_TYPES = [
        {
            "code": "01",
            "name": "Factura Electrónica",
            "sequence_prefix": "F001",
            "next_sequence": 1,
            "requires_customer": True,
            "is_credit_note": False
        },
        {
            "code": "03",
            "name": "Boleta de Venta Electrónica",
            "sequence_prefix": "B001",
            "next_sequence": 1,
            "requires_customer": False,
            "is_credit_note": False
        },
        {
            "code": "07",
            "name": "Nota de Crédito",
            "sequence_prefix": "FC01",
            "next_sequence": 1,
            "requires_customer": True,
            "is_credit_note": True
        }
    ]

PAYMENT_METHODS =[]

TAXES = []



