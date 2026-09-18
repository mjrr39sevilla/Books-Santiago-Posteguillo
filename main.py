"""
Reto Python Catálogo de colecciones
Tema: Santiago Posteguillo y su obra
"""
def main():

    # 1. Declarar variables y tipos de datos básicos

        catalog_title = "Santiago Posteguillo Collection"  # String
        total_books = 0  # Integer (se actualizará dinámicamente)
        is_running = True  # Boolean

    # 2. Estructuras de datos (Listas y Diccionarios)

        catalog = [
            {"title": "La noche en que Frankenstein leyó El Quijote", "books_series": "Ensayo", "year": 2012},
            {"title": "La sangre de los libros", "books_series": "Relatos", "year": 2014},
            {"title": "Africanus: el hijo del cónsul", "books_series": "Trilogía de Africanus", "year": 2006},
            {"title": "Las legiones malditas", "books_series": "Trilogía de Africanus", "year": 2008},
            {"title": "La traición de Roma", "books_series": "Trilogía de Africanus", "year": 2009},
            {"title": "Los asesinos del emperador", "books_series": "Trilogía de Trajano", "year": 2011},
            {"title": "Circo Máximo", "books_series": "Trilogía de Trajano", "year": 2013},
            {"title": "La legión perdida", "books_series": "Trilogía de Trajano", "year": 2016},
            {"title": "Yo, Julia", "books_series": "Bilogía de Julia Domna", "year": 2018},
            {"title": "Y Julia retó a los dioses", "books_series": "Bilogía de Julia Domna", "year": 2020},
            {"title": "Roma soy yo", "books_series": "Serie de Julio César", "year": 2022},
            {"title": "Maldita Roma", "books_series": "Serie de Julio César", "year": 2023},
            {"title": "Los tres mundos", "books_series": "Serie de Julio César", "year": 2025},
                ]


    # Actualizamos el total de libros basándonos en la longitud de la lista
        total_books = len(catalog)

        print(f"=== {catalog_title} ===")
        print(f"Initial catalog loaded with {total_books} works.")

    # 6. Repetir acciones utilizando bucles (while)
        while is_running:
            print("\n--- MENU ---")
            print("1. Display book catalog")
            print("2. Check variable data types")
            print("3. Add a new book (with data validation)")
            print("4. Exit")

    # 2 & 5. Capturar información por terminal y manipular strings con .strip()
            option = input("Choose an option (1-4): ").strip()

    # 7 & 8. Tomar decisiones con condicionales y operadores de comparación

        # Bucle for para recorrer la lista y mostrar los elementos enumerados

            if option == "1":
                print("\n[COMPLETE CATALOG LIST]")
                for index, book in enumerate(catalog, start = 1):
                    print(f"{index}. {book}")
        # Consultar el tipo de dato almacenado en una variable usando type()
            elif option == "2":
                print("\n[DATA TYPES CONSULTATION]")
                print(f"Variable 'catalog_title' type: {type(catalog_title)}")
                print(f"Variable 'total_books' type: {type(total_books)}")
                print(f"Variable 'is_running' type: {type(is_running)}")
                print(f"Variable 'catalog' type: {type(catalog)}")
        # Capturar información de texto por terminal
            elif option == "3":
                new_book_title = input("Enter the title of the new book: ").strip()

                # 1. Primero validamos que el texto no esté vacío
                if len(new_book_title) > 0:

                    # 2. Comprobamos si ya existe (usando 'new_book_title' correctamente)
                    if any(book['title'].lower() == new_book_title.lower() for book in catalog):
                        print(f"[ERROR] Book '{new_book_title}' already exists in the catalog.")
                    else:
                        # 3. Añadimos un diccionario completo para mantener la consistencia del catálogo
                        catalog.append({"title": new_book_title, "books_series": "N/A", "year": 2026})
                        total_books = len(catalog)  # Actualizar variable numérica
                        print(f"\n[SUCCESS] Book '{new_book_title}' added successfully!")
                        print(f"Updated total books: {total_books}")
                else:
                    # 4. Si el texto estaba vacío, entra aquí
                        print("\n[ERROR] The book title cannot be empty.")

            elif option == "4":
                print("\nExiting the program. Goodbye!")
                is_running = False  # Rompe el bucle while

            else:
                print("\n[ERROR] Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
