"""
Reto II Python Catálogo de colecciones
Tema: Santiago Posteguillo y su obra
"""

from validations import (
    validate_not_empty,
    validate_price,
    validate_status,
    validate_description
)


def add_book(catalog, book_id, title, category, price, status, description):
    """Agrega un libro de Santiago Posteguillo validado al catálogo."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    v_id = validate_not_empty(book_id, "id")
    v_title = validate_not_empty(title, "title")
    v_category = validate_not_empty(category, "category")
    v_price = validate_price(price)
    v_status = validate_status(status)
    v_desc = validate_description(description)

    if book_exists(catalog, v_id):
        raise ValueError(f"Ya existe un libro registrado con el código/ISBN '{v_id}'.")

        book = {
        "id": v_id,
        "title": v_title,
        "category": v_category,
        "price": v_price,
        "status": v_status,
        "description": v_desc
    }
    catalog.append(book)
    return book


def list_books(catalog):
    """Retorna una lista con los títulos de todas las obras."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return [book["title"] for book in catalog]


def find_book_by_id(catalog, book_id):
    """Busca y retorna el diccionario del libro por su código, o None si no existe."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    for book in catalog:
        if book["id"] == book_id:
            return book
    return None

def remove_book(catalog, book_id):
    """Elimina un libro del catálogo dado su código."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    book = find_book_by_id(catalog, book_id)
    if book is None:
        raise ValueError(f"No se encontró ningún libro con el código '{book_id}'.")

    catalog.remove(book)
    return True

def get_catalog_summary(catalog):
    """Retorna un diccionario con la cantidad de libros agrupados por saga/categoría."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    summary = {}
    for book in catalog:
        cat = book["category"]
        summary[cat] = summary.get(cat, 0) + 1
    return summary


def get_books_by_category(catalog, category):
    """Retorna los títulos de los libros pertenecientes a una saga específica."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return [book["title"] for book in catalog if book["category"].lower() == category.lower()]


def book_exists(catalog, book_id):
    """Retorna True si el libro existe en el catálogo, False en caso contrario."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return any(book["id"] == book_id for book in catalog)


def filter_by_status(catalog, status):
    """Filtra los libros que coincidan con un estado permitido."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    validated_status = validate_status(status)
    return [book for book in catalog if book["status"] == validated_status]


def filter_by_min_price(catalog, min_price):
    """Filtra los libros cuyo precio sea mayor al indicado."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    try:
        numeric_min = float(min_price)
    except (ValueError, TypeError):
        raise ValueError("El precio mínimo debe ser un valor numérico.")

    return [book for book in catalog if book["price"] > numeric_min]


def get_average_price(catalog):
    """Calcula el precio promedio de las obras en el catálogo."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    if not catalog:
        return 0.0

    total_price = sum(book["price"] for book in catalog)
    return total_price / len(catalog)