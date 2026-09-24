"""
Reto II Python Catálogo de colecciones
Tema: Santiago Posteguillo y su obra
"""

from catalog import (
    add_book,
    list_books,
    find_book_by_id,
    remove_book,
    get_catalog_summary,
    filter_by_status,
    get_average_price
)


INITIAL_CATALOG = [
    {"id": "SP-01", "title": "La noche en que Frankenstein leyó El Quijote", "category": "Ensayo", "price": "14.90", "status": "disponible", "description": "Edición usada, buen estado"},
    {"id": "SP-02", "title": "La sangre de los libros", "category": "Relatos", "price": "12.50", "status": "disponible", "description": "Edición usada"},
    {"id": "SP-03", "title": "Africanus: el hijo del cónsul", "category": "Trilogía de Africanus", "price": "19.95", "status": "disponible", "description": "Edición certificada"},
    {"id": "SP-04", "title": "Las legiones malditas", "category": "Trilogía de Africanus", "price": "19.95", "status": "reservada", "description": "Edición usada"},
    {"id": "SP-05", "title": "La traición de Roma", "category": "Trilogía de Africanus", "price": "19.95", "status": "disponible", "description": "Edición usada"},
    {"id": "SP-06", "title": "Los asesinos del emperador", "category": "Trilogía de Trajano", "price": "18.90", "status": "disponible", "description": "Edición certificada"},
    {"id": "SP-07", "title": "Circo Máximo", "category": "Trilogía de Trajano", "price": "18.90", "status": "vendida", "description": "Edición usada"},
    {"id": "SP-08", "title": "La legión perdida", "category": "Trilogía de Trajano", "price": "18.90", "status": "disponible", "description": "Edición usada"},
    {"id": "SP-09", "title": "Yo, Julia", "category": "Bilogía de Julia Domna", "price": "21.90", "status": "disponible", "description": "Edición certificada"},
    {"id": "SP-10", "title": "Y Julia retó a los dioses", "category": "Bilogía de Julia Domna", "price": "21.90", "status": "disponible", "description": "Edición usada"},
    {"id": "SP-11", "title": "Roma soy yo", "category": "Serie de Julio César", "price": "23.90", "status": "disponible", "description": "Edición usada"},
    {"id": "SP-12", "title": "Maldita Roma", "category": "Serie de Julio César", "price": "23.90", "status": "reservada", "description": "Edición certificada"},
    {"id": "SP-13", "title": "Los tres mundos", "category": "Serie de Julio César", "price": "24.90", "status": "disponible", "description": "Edición certificada, primera impresión"},
]


def load_initial_catalog(catalog):
    """Carga el catálogo de partida usando add_book, para que pase
    por las mismas validaciones que un alta manual desde el menú."""
    for book in INITIAL_CATALOG:
        try:
            add_book(
                catalog,
                book["id"],
                book["title"],
                book["category"],
                book["price"],
                book["status"],
                book["description"],
            )
        except ValueError as e:
            print(f"[AVISO] No se pudo cargar '{book['title']}': {e}")
        except Exception as e:
            print(f"[AVISO] Error inesperado cargando '{book['title']}': {e}")


def show_menu():
    print("\n==================================================")
    print("   BIBLIOTECA - OBRAS DE SANTIAGO POSTEGUILLO")
    print("==================================================")
    print("1. Registrar una obra (libro)")
    print("2. Mostrar títulos de todas las obras")
    print("3. Mostrar obras disponibles para la venta")
    print("4. Mostrar el precio promedio de la colección")
    print("5. Buscar obra por código/ISBN")
    print("6. Eliminar obra del catálogo")
    print("7. Ver resumen por saga/categoría")
    print("8. Salir del sistema")


def handle_register_book(catalog):
    print("\n--- Registrar Obra de Santiago Posteguillo ---")
    book_id = input("Código / ISBN (ej. SP-01): ")
    book_title = input("Título del libro (ej. Africanus: El hijo del cónsul): ")
    book_category = input("Saga / Categoría (ej. Trilogía de Africanus): ")
    book_price = input("Precio en €: ")
    book_status = input("Estado (disponible, reservada, vendida): ")
    book_description = input("Descripción (debe incluir 'usada' o 'certificada', ej. Edición usada): ")

    try:
        add_book(catalog, book_id, book_title, book_category, book_price, book_status, book_description)
        print("¡Obra registrada exitosamente en el catálogo!")
    except ValueError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def handle_list_titles(catalog):
    try:
        titles = list_books(catalog)
        if not titles:
            print("\nEl catálogo literario está vacío.")
        else:
            print("\n--- Obras Registradas ---")
            for idx, title in enumerate(titles, 1):
                print(f"{idx}. {title}")
    except Exception as e:
        print(f"Error: {e}")


def handle_show_available(catalog):
    try:
        available_books = filter_by_status(catalog, "disponible")
        if not available_books:
            print("\nNo hay obras disponibles en este momento.")
        else:
            print("\n--- Obras Disponibles ---")
            for book in available_books:
                print(f"- [{book['id']}] {book['title']} ({book['category']}) - {book['price']:.2f}€")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def handle_average_price(catalog):
    try:
        average_price = get_average_price(catalog)
        print(f"\nEl precio promedio de las obras de Santiago Posteguillo es: {average_price:.2f}€")
    except Exception as e:
        print(f"Error: {e}")


def handle_find_book(catalog):
    book_id = input("\nIngrese el código/ISBN de la obra a buscar: ").strip()
    try:
        book = find_book_by_id(catalog, book_id)
        if book:
            print("\n--- Ficha de la Obra ---")
            print(f"Código / ISBN : {book['id']}")
            print(f"Título        : {book['title']}")
            print(f"Saga          : {book['category']}")
            print(f"Precio        : {book['price']:.2f}€")
            print(f"Estado        : {book['status']}")
            print(f"Descripción   : {book['description']}")
        else:
            print("\nNo se encontró ninguna obra con ese código.")
    except Exception as e:
        print(f"Error: {e}")


def handle_remove_book(catalog):
    book_id = input("\nIngrese el código/ISBN de la obra a eliminar: ").strip()
    try:
        remove_book(catalog, book_id)
        print("¡Obra eliminada del catálogo con éxito!")
    except ValueError as e:
        print(f"[ERROR] {e}")


def handle_summary(catalog):
    try:
        summary = get_catalog_summary(catalog)
        if not summary:
            print("\nEl catálogo literario está vacío.")
        else:
            print("\n--- Resumen por Saga / Categoría ---")
            for category, count in summary.items():
                print(f"- {category}: {count} obra(s)")
    except Exception as e:
        print(f"Error: {e}")


def main():
    catalog = []
    load_initial_catalog(catalog)

    while True:
        show_menu()
        option = input("\nSeleccione una opción (1-8): ").strip()

        if option == "1":
            handle_register_book(catalog)
        elif option == "2":
            handle_list_titles(catalog)
        elif option == "3":
            handle_show_available(catalog)
        elif option == "4":
            handle_average_price(catalog)
        elif option == "5":
            handle_find_book(catalog)
        elif option == "6":
            handle_remove_book(catalog)
        elif option == "7":
            handle_summary(catalog)
        elif option == "8":
            print("\nCerrando la biblioteca de Roma. ¡Ave, César y hasta pronto!")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione un número del 1 al 8.")


if __name__ == "__main__":
    main()