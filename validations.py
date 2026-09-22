"""
Reto II Python Catálogo de colecciones
Tema: Santiago Posteguillo y su obra
"""
# validations.py

VALID_STATUSES = ("disponible", "reservada", "vendida")


def validate_not_empty(value, field_name):
    """Valida que un valor no esté vacío o compuesto solo por espacios."""
    if not value or not str(value).strip():
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")
    return str(value).strip()


def validate_price(price):
    """Valida que el precio sea numérico y mayor que cero."""
    try:
        numeric_price = float(str(price).replace(",", "."))
    except (ValueError, TypeError):
        raise ValueError("El precio del libro debe ser un valor numérico válido.")

    if numeric_price <= 0:
        raise ValueError("El precio del libro debe ser estrictamente mayor que cero.")
    return numeric_price


def validate_status(status):
    """Valida que el estado se encuentre dentro de los permitidos."""
    if not isinstance(status, str):
        raise ValueError("El estado debe ser una cadena de texto.")

    normalized_status = status.strip().lower()
    if normalized_status not in VALID_STATUSES:
        allowed = ", ".join(VALID_STATUSES)
        raise ValueError(f"Estado inválido. Debe ser uno de los siguientes: {allowed}.")
    return normalized_status


def validate_description(description):
    """Valida que la descripción contenga obligatoriamente 'usada' o 'certificada'."""
    if not isinstance(description, str):
        raise ValueError("La descripción debe ser una cadena de texto.")

    desc_lower = description.lower()
    if "usada" not in desc_lower and "certificada" not in desc_lower:
        raise ValueError("La descripción del libro debe contener obligatoriamente la palabra 'usada' o 'certificada'.")
    return description.strip()