"""
Reto II Python Catálogo de colecciones
Tema: Santiago Posteguillo y su obra
"""
from catalog import (
    add_piece,
    list_pieces,
    find_piece_by_id,
    remove_piece,
    get_catalog_summary,
    filter_by_status,
    get_average_price
)


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


def main():
    catalog = []

    while True:
        show_menu()
        option = input("\nSeleccione una opción (1-8): ").strip()

        if option == "1":
            print("\n--- Registrar Obra de Posteguillo ---")
            book_id = input("Código / ISBN (ej. SP-01): ")
            book_title = input("Título del libro (ej. Africanus: El hijo del consul): ")
            book_category = input("Saga / Categoría (ej. Trilogía de Escipión): ")
            book_price = input("Precio en €: ")
            book_status = input("Estado (disponible, reservada, vendida): ")
            book_description = input("Descripción (debe incluir 'usada' o 'certificada', ej. Edición usada): ")

            try:
                add_piece(catalog, book_id, book_title, book_category, book_price, book_status, book_description)
                print("¡Obra registrada exitosamente en el catálogo!")
            except ValueError as e:
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")

        elif option == "2":
            try:
                titles = list_pieces(catalog)
                if not titles:
                    print("\nEl catálogo literario está vacío.")
                else:
                    print("\n--- Obras Registradas ---")
                    for idx, title in enumerate(titles, 1):
                        print(f"{idx}. {title}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "3":
            try:
                available_books = filter_by_status(catalog, "disponible")
                if not available_books:
                    print("\nNo hay obras disponibles en este momento.")
                else:
                    print("\n--- Obras Disponibles ---")
                    for book in available_books:
                        print(f"- [{book['id']}] {book['name']} ({book['category']}) - {book['price']:.2f}€")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "4":
            try:
                average_price = get_average_price(catalog)
                print(f"\nEl precio promedio de las obras de Posteguillo es: {average_price:.2f}€")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "5":
            book_id = input("\nIngrese el código/ISBN de la obra a buscar: ").strip()
            try:
                book = find_piece_by_id(catalog, book_id)
                if book:
                    print("\n--- Ficha de la Obra ---")
                    print(f"Código / ISBN : {book['id']}")
                    print(f"Título        : {book['name']}")
                    print(f"Saga          : {book['category']}")
                    print(f"Precio        : {book['price']:.2f}€")
                    print(f"Estado        : {book['status']}")
                    print(f"Descripción   : {book['description']}")
                else:
                    print("\nNo se encontró ninguna obra con ese código.")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "6":
            book_id = input("\nIngrese el código/ISBN de la obra a eliminar: ").strip()
            try:
                remove_piece(catalog, book_id)
                print("¡Obra eliminada del catálogo con éxito!")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "7":
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

        elif option == "8":
            print("\nCerrando la biblioteca de Roma. ¡Ave, César y hasta pronto!")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione un número del 1 al 8.")


if __name__ == "__main__":
    main()
