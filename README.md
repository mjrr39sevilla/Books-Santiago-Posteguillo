# Books-Santiago-Posteguillo
Obra literaria del escritor valenciano Santiago Posteguillo.

# Santiago Posteguillo Collection

## 📌 Objetivo
Desarrollar una aplicación de consola en Python que cumpla con los requisitos académicos específicos mediante la declaración de variables, validación de datos, estructuras de objetos (diccionarios), bucles, condicionales y un manejo de errores robusto.

## 🏛️ Contexto del catálogo
Este proyecto gestiona un catálogo digital que contiene obras de novela histórica, ensayos y narraciones del reconocido autor **Santiago Posteguillo**. Cada obra se almacena como un diccionario estructurado que incluye su título, serie/categoría y año de publicación, permitiendo al usuario explorar y ampliar la colección fácilmente.

## 🚀 Funcionalidades implementadas
El programa opera a través de un menú interactivo en la consola con las siguientes opciones:
1. **Mostrar el catálogo de libros:** Muestra una lista enumerada de todos los libros almacenados actualmente en la colección con sus atributos detallados.
2. **Consultar tipos de datos de variables:** Evalúa y muestra en pantalla el tipo del sistema (`str`, `int`, `bool`, `list`) de las variables principales utilizando la función nativa `type()`.
3. **Añadir un nuevo libro (con validación de datos):**
   - Captura el texto ingresado por la terminal aplicando `.strip()` para limpiar espacios sobrantes.
   - Valida que la entrada no esté vacía.
   - Realiza una comprobación insensible a mayúsculas y minúsculas para evitar entradas duplicadas en el catálogo.
   - Añade la nueva obra como un diccionario estructurado y actualiza dinámicamente el recuento total de libros.
4. **Salir:** Finaliza de forma limpia el bucle del programa y muestra un mensaje de despedida.

## 🛠️ Tecnologías utilizadas
* **Python 3.14.7**: Lenguaje de programación principal.
* **Git y GitHub**: Control de versiones y repositorio de documentación del proyecto.

## ⚙️ Cómo ejecutar el programa
1. Asegúrate de tener Python instalado en tu equipo.
2. Clona este repositorio o descarga los archivos fuente.
3. Abre tu terminal o línea de comandos en el directorio del proyecto.
4. Ejecuta la aplicación utilizando el siguiente comando:
   ```bash
   python main.py

## 💻 Ejemplo de interacción
--- MENU ---
1. Display book catalog
2. Check variable data types
3. Add a new book (with data validation)
4. Exit
Choose an option (1-4): 3
Enter the title of the new book: El escalón 33

[SUCCESS] Book 'El escalón 33' added successfully!
Updated total books: 14
