
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

INITIAL_TAXES = [
    {
        "code": "1000", # Código SUNAT para IGV
        "name": "IGV (18%)", # Impuesto General a las Ventas
        "rate": 18.00,
        "is_percentage": True
    },
    {
        "code": "9997", # Código SUNAT para Exonerado
        "name": "Exonerado (0%)", # Se usa para productos de la canasta básica (papas, frutas). En el XML de SUNAT se marca como "E".
        "rate": 0.00,
        "is_percentage": True
    },
    {
        "code": "9998", # Código SUNAT para Inafecto
        "name": "Inafecto (0%)", # Se usa para servicios médicos o educativos. En el XML se marca como "O".
        "rate": 0.00,
        "is_percentage": True
    },
    {
        "code": "7152", # Código SUNAT para Impuesto a la bolsa (ICBPER)
        "name": "ICBPER (Bolsas)", #Si vendes bolsas plásticas, la ley exige cobrar este monto fijo (actualmente S/ 0.50
        "rate": 0.50, # Monto fijo por unidad
        "is_percentage": False # Este es un monto fijo, no porcentaje
    }
]


INITIAL_PAYMENT_METHODS = [
    {
        "code": "008",
        "name": "EFECTIVO",
        "fee_percentage": 0.00,
        "fee_fixed": 0.00,
        "requires_reference": False,
        "allows_installments": False
    },
    {
        "code": "005",
        "name": "TARJETA DÉBITO",
        "fee_percentage": 3.15,
        "fee_fixed": 0.00,
        "requires_reference": True,
        "allows_installments": False
    },
    {
        "code": "006",
        "name": "TARJETA CRÉDITO",
        "fee_percentage": 3.45,
        "fee_fixed": 0.50,
        "requires_reference": True,
        "allows_installments": True,
        "max_installments": 36
    },
    {
        "code": "999",
        "name": "YAPE",
        "fee_percentage": 0.00,
        "fee_fixed": 0.00,
        "requires_reference": True,
        "allows_installments": False
    },
    {
        "code": "998",
        "name": "PLIN",  # <-- Agregado
        "fee_percentage": 0.00,
        "fee_fixed": 0.00,
        "requires_reference": True,
        "allows_installments": False
    },
    {
        "code": "997",
        "name": "YAPE EMPRESA",
        "fee_percentage": 2.95,
        "fee_fixed": 0.00,
        "requires_reference": True,
        "allows_installments": False
    },
    {
        "code": "996",
        "name": "PLIN EMPRESA",
        "fee_percentage": 2.95,
        "fee_fixed": 0.00,
        "requires_reference": True,
        "allows_installments": False
    },
    {
        "code": "001",
        "name": "TRANSFERENCIA BANCARIA",
        "fee_percentage": 0.00,
        "fee_fixed": 0.00,
        "requires_reference": True,
        "allows_installments": False
    }
]





