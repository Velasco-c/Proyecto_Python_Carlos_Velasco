def pedir_opcion(mensaje):
    while True:
        try:
            op = int(input(mensaje))
            return op
        except ValueError:
            print("Error: Solo se permiten números.")

def Menu_Principal():
    Menu = """
===========================================
        Administrador de Colección
===========================================
1. Añadir un Nuevo Elemento
2. Ver Todos los Elementos
3. Buscar un Elemento
4. Editar un Elemento
5. Eliminar un Elemento
6. Ver Elementos por Categoría
7. Salir
===========================================
Selecciona una opción (1-7):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menu_opcion_1():
    Menu = """
===========================================
        Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menu_opcion_2():
    Menu = """
===========================================
        Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda la Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menu_opcion_3():
    Menu = """
===========================================
        Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por Título
2. Buscar por Autor/Director/Artista
3. Buscar por Género
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menu_opcion_4():
    Menu = """
===========================================
        Editar un Elemento
===========================================
¿Qué tipo de cambio deseas realizar?
1. Editar Título
2. Editar Autor/Director/Artista
3. Editar Género
4. Editar Valoración
5. Regresar al Menú Principal
===========================================
Selecciona una opción (1-5):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menu_opcion_5():
    Menu = """
===========================================
        Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Regresar al Menú Principal
===========================================
Selecciona una opción (1-2):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menu_opcion_6():
    Menu = """
===========================================
        Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Menuopciones_extras():
    Menu = """
===========================================
        Ver por las Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Genero
2. Ver Autor
3. Ver Valoracion
4. Regresar al Menú ver elementos por categoria
===========================================
Selecciona una opción (1-4):
"""
    print(Menu)
    return pedir_opcion("Ingrese una de las opciones: ")

def Salida():
    exit = """ 
===========================================
                   Salida
===========================================
          Que tenga un feliz dia
===========================================
"""
    print(exit)
