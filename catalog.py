# catalog.py

from validations import (
    validate_not_empty,
    validate_price,
    validate_status,
    validate_description
)


def add_piece(catalog, piece_id, name, category, price, status, description):
    """Agrega un libro de Santiago Posteguillo validado al catálogo."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    v_id = validate_not_empty(piece_id, "id")
    v_name = validate_not_empty(name, "name")
    v_category = validate_not_empty(category, "category")
    v_price = validate_price(price)
    v_status = validate_status(status)
    v_desc = validate_description(description)

    if piece_exists(catalog, v_id):
        raise ValueError(f"Ya existe un libro registrado con el código/ISBN '{v_id}'.")

    piece = {
        "id": v_id,
        "name": v_name,
        "category": v_category,
        "price": v_price,
        "status": v_status,
        "description": v_desc
    }
    catalog.append(piece)
    return piece


def list_pieces(catalog):
    """Retorna una lista con los títulos de todas las obras."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog, piece_id):
    """Busca y retorna el diccionario del libro por su código, o None si no existe."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    for piece in catalog:
        if piece["id"] == piece_id:
            return piece
    return None


def remove_piece(catalog, piece_id):
    """Elimina un libro del catálogo dado su código."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    try:
        piece = find_piece_by_id(catalog, piece_id)
        if piece is None:
            raise ValueError(f"No se encontró ningún libro con el código '{piece_id}'.")
        catalog.remove(piece)
        return True
    except ValueError as e:
        print(f"[ERROR] {e}")
        return False

def get_catalog_summary(catalog):
    """Retorna un diccionario con la cantidad de libros agrupados por saga/categoría."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    summary = {}
    for piece in catalog:
        cat = piece["category"]
        summary[cat] = summary.get(cat, 0) + 1
    return summary


def get_pieces_by_category(catalog, category):
    """Retorna los títulos de los libros pertenecientes a una saga específica."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return [piece["name"] for piece in catalog if piece["category"].lower() == category.lower()]


def piece_exists(catalog, piece_id):
    """Retorna True si el libro existe en el catálogo, False en caso contrario."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return any(piece["id"] == piece_id for piece in catalog)


def filter_by_status(catalog, status):
    """Filtra los libros que coincidan con un estado permitido."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    validated_status = validate_status(status)
    return [piece for piece in catalog if piece["status"] == validated_status]


def filter_by_min_price(catalog, min_price):
    """Filtra los libros cuyo precio sea mayor al indicado."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    try:
        numeric_min = float(min_price)
    except (ValueError, TypeError):
        raise ValueError("El precio mínimo debe ser un valor numérico.")

    return [piece for piece in catalog if piece["price"] > numeric_min]


def get_average_price(catalog):
    """Calcula el precio promedio de las obras en el catálogo."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    if not catalog:
        return 0.0

    total_price = sum(piece["price"] for piece in catalog)
    return total_price / len(catalog)