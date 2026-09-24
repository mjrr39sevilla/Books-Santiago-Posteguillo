# Books-Santiago-Posteguillo
Obra literaria del escritor valenciano Santiago Posteguillo.

---

## Reto I — Santiago Posteguillo Collection

### 📌 Objetivo
Desarrollar una aplicación de consola en Python que cumpla con los requisitos académicos específicos mediante la declaración de variables, validación de datos, estructuras de objetos (diccionarios), bucles, condicionales y un manejo de errores robusto.

### 🏛️ Contexto del catálogo
Este proyecto gestiona un catálogo digital que contiene obras de novela histórica, ensayos y narraciones del reconocido autor **Santiago Posteguillo**. Cada obra se almacena como un diccionario estructurado que incluye su título, serie/categoría y año de publicación, permitiendo al usuario explorar y ampliar la colección fácilmente.

### 🚀 Funcionalidades implementadas
El programa opera a través de un menú interactivo en la consola con las siguientes opciones:
1. **Mostrar el catálogo de libros:** Muestra una lista enumerada de todos los libros almacenados actualmente en la colección con sus atributos detallados.
2. **Consultar tipos de datos de variables:** Evalúa y muestra en pantalla el tipo del sistema (`str`, `int`, `bool`, `list`) de las variables principales utilizando la función nativa `type()`.
3. **Añadir un nuevo libro (con validación de datos):**
   - Captura el texto ingresado por la terminal aplicando `.strip()` para limpiar espacios sobrantes.
   - Valida que la entrada no esté vacía.
   - Realiza una comprobación insensible a mayúsculas y minúsculas para evitar entradas duplicadas en el catálogo.
   - Añade la nueva obra como un diccionario estructurado y actualiza dinámicamente el recuento total de libros.
4. **Salir:** Finaliza de forma limpia el bucle del programa y muestra un mensaje de despedida.

### 💻 Ejemplo de interacción
```
--- MENU ---
1. Display book catalog
2. Check variable data types
3. Add a new book (with data validation)
4. Exit
Choose an option (1-4): 3
Enter the title of the new book: El escalón 33

[SUCCESS] Book 'El escalón 33' added successfully!
Updated total books: 14
```

---

## Reto II — Santiago Posteguillo Collection

### 📌 Objetivo
Refactorizar el catálogo del Reto I aplicando funciones de responsabilidad única, uso de `return`, manejo de errores con `try/except`, lanzamiento de excepciones (`raise`), validaciones tempranas y organización del código en módulos independientes.

### 🏛️ Contexto del catálogo
Cada libro se representa ahora como un diccionario con esta estructura:

```python
{
    "id": "SP-01",
    "title": "Africanus: el hijo del cónsul",
    "category": "Trilogía de Africanus",
    "price": 19.95,
    "status": "disponible",
    "description": "Edición usada, buen estado"
}
```
- `status` permitido: `disponible`, `reservada`, `vendida`.
- `description` debe contener obligatoriamente la palabra `usada` o `certificada`.

### 🗂️ Estructura del proyecto
```
Books-Santiago-Posteguillo/
├── catalog.py       -> Lógica del catálogo (agregar, listar, buscar, eliminar, filtrar, métricas)
├── validations.py   -> Validaciones de datos de una obra
├── main.py          -> Menú interactivo y flujo principal
└── README.md
```

`catalog.py` se importa desde `main.py`. `validations.py` se importa desde `catalog.py`. La lógica de validación no se repite en ningún otro archivo.

### 🚀 Funcionalidades implementadas
Menú interactivo ampliado a 8 opciones:
1. Registrar una obra
2. Mostrar títulos de todas las obras
3. Mostrar obras disponibles
4. Mostrar el precio promedio de la colección
5. Buscar obra por código/ISBN
6. Eliminar obra del catálogo
7. Ver resumen por saga/categoría
8. Salir

### ⚠️ Manejo de errores
Las funciones de `catalog.py` y `validations.py` validan los datos de entrada y lanzan `ValueError` con mensajes descriptivos cuando algo no es correcto (campo vacío, precio no numérico, estado no permitido, descripción incompleta, id inexistente, etc.). `main.py` captura esas excepciones con `try/except` en cada opción del menú, mostrando un mensaje claro sin interrumpir la ejecución del programa.

### 💻 Ejemplo de interacción
```
==================================================
BIBLIOTECA - OBRAS DE SANTIAGO POSTEGUILLO
Registrar una obra (libro)
Mostrar títulos de todas las obras
Mostrar obras disponibles para la venta
Mostrar el precio promedio de la colección
Buscar obra por código/ISBN
Eliminar obra del catálogo
Ver resumen por saga/categoría
Salir del sistema

Seleccione una opción (1-8): 6

Ingrese el código/ISBN de la obra a eliminar: SP-98
[ERROR] No se encontró ningún libro con el código 'SP-98'.
```

---

## ⚙️ Cómo ejecutar el programa
1. Asegúrate de tener Python instalado en tu equipo.
2. Clona este repositorio o descarga los archivos fuente.
3. Abre tu terminal o línea de comandos en el directorio del proyecto.
4. Ejecuta la aplicación utilizando el siguiente comando:
```bash
python main.py
```

## 🔀 Flujo de trabajo con Git
El desarrollo del Reto II se realizó en la rama `feature/posteguillo-updates`, manteniendo commits independientes por cada mejora (refactor a funciones, manejo de errores, organización en módulos, correcciones y documentación), antes de integrarse en `main`.

## 🛠️ Tecnologías utilizadas
* **Python 3.14.7**: Lenguaje de programación principal.
* **Git y GitHub**: Control de versiones y repositorio de documentación del proyecto.