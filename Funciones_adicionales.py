from Datos import *
from Recursos import * 
from Utilidades import Menuopciones_extras

def agg_recurso(Elemento, etiqueta_creador):
    seperador()
    print(f"Ingrese los datos del {Elemento}")
    seperador()
    Nombre = input(f"Ingrese el nombre del archivo tipo {Elemento}: ").strip() 
    if Verificaion_antes_de_agg(Nombre,"Nombre"):
        print(f"Ya existe este archivo")
        return None
    Genero = input("Ingrese el genero: ").strip() 
    Creador = input(f"Ingrese el nombre del {etiqueta_creador}: ").strip() 
    while True:
        try:
            Valoracion = float(input("Ingrese la valoracion (0-10): "))
            if Valoracion < 0 or Valoracion > 10:
                print("La valoracion debe estar entre 0 y 10.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido.")

    nuevo_recurso = {
        "Elemento": Elemento,
        "Nombre": Nombre,
        "Genero": Genero,
        "Creadores": Creador,
        "Valoracion": Valoracion
    }
    return nuevo_recurso

def mostrar_por_elemento(dato, tipo_elemento):
    cargar_datos(dato)
    for Recurso in Recursos:
        if Recurso['Elemento'] == tipo_elemento:
            mostrar_recurso(Recurso)

def Busqueda(dato,campo,title):
    cargar_datos(dato)
    nombre = input(f"Ingrese el nombre del {title} que desea buscar: ").strip()  

    if Verificaion_antes_de_agg(nombre, campo):
        for i in Recursos:
            if i is not None and i.get(campo) and i.get(campo).strip().lower() == nombre.lower():  
                mostrar_recurso(i)
    else:
        seperador()
        print("No existe el archivo con este criterio.")
        seperador()

def editarTitulo(dato):
    cargar_datos(dato)
    Titulo = input("Ingrese el titulo que se desee cambiar: ").strip()  
    Encontrado = False

    for i in Recursos:
        if i is not None and i.get('Nombre') and i.get('Nombre').strip().lower() == Titulo.lower():  
            Encontrado = True
            mostrar_recurso(i)
            print("\n¿Desea cambiar el titulo de este archivo? ")
            afirmacion = input("Selecione s/n : ")

            if afirmacion.lower() == "s":
                NuevoTitulo = input("Ingrese el nuevo titulo: ").strip()  
                if Verificaion_antes_de_agg(NuevoTitulo,"Nombre"): 
                    print("Ya existe un recurso con ese nombre")
                else:
                    i["Nombre"] = NuevoTitulo
                    guardar_datos(dato)
                    print("Se cambió correctamente")
            break
    if not Encontrado: 
        print("No existe ese titulo")

def EditarCreador(dato):
    cargar_datos(dato)
    Autor = input("Ingrese el nombre del autor que desea cambiar: ").strip()  
    Encontrado = False

    for i in Recursos:
        if i is not None and i.get("Creadores") and i["Creadores"].strip().lower() == Autor.lower(): 
            Encontrado = True
            mostrar_recurso(i)
            print("\n¿Desea cambiar el creador de este archivo?")
            afirmacion = input("Seleccione s/n : ")

            if afirmacion.lower() == "s":
                NuevoAutor = input("Ingrese el nuevo nombre del creador: ").strip()
                i["Creadores"] = NuevoAutor
                guardar_datos(dato)
                print("Se cambió correctamente")
            else:
                print("No se realizaron cambios")
            break  

    if not Encontrado:
        print("No existe ese autor")

def EditarGenero(dato):
    cargar_datos(dato)
    Genero = input("Ingrese el nombre del genero que desea cambiar: ").strip()  # 🔧 CAMBIO
    lista_indices = indiceGeneral(Genero, "Genero")
    if not lista_indices:
        print("No existe ese genero")
        return
    contador = 1
    for indice in lista_indices:
        mostrar_recurso_Listado(contador,Recursos[indice])
        contador += 1
    try:
        seleccion = int(input("\nSeleccione el numero que desea editar: ")) - 1
    except ValueError:
        print("Selección inválida")
        return

    if seleccion < 0 or seleccion >= len(lista_indices):
        print("Seleccion invalida")
        return

    indice_real = lista_indices[seleccion]

    print("\n¿Desea cambiar el genero de este archivo?")
    afirmacion = input("Seleccione s/n : ")

    if afirmacion.lower() == "s":
        Nuevo_Genero = input("Ingrese el nuevo nombre del genero: ").strip()  # 🔧 CAMBIO
        Recursos[indice_real]["Genero"] = Nuevo_Genero
        guardar_datos(dato)
        print("Se cambió correctamente")
    else:
        print("No se realizaron cambios")

def EditarValoracion(dato):
    cargar_datos(dato)
    try:
        ValoracionActual = float(input("Ingrese la valoracion que desee cambiar: "))
    except ValueError:
        print("Valoración inválida.")
        return

    listaValoracion = indiceFloat(ValoracionActual)

    if not listaValoracion:
        print("No existe un archivo con esta valoracion")
        return

    contador = 1
    for indice in listaValoracion:
        mostrar_recurso_Listado(contador,Recursos[indice])
        contador += 1

    try:
        seleccion = int(input("\nSeleccione el numero que desea editar: ")) - 1
    except ValueError:
        print("Selección inválida.")
        return

    if seleccion < 0 or seleccion >= len(listaValoracion):
        print("Seleccion invalida")
        return

    indice_real = listaValoracion[seleccion]

    print("\n¿Desea cambiar la valoracion de este archivo?")
    afirmacion = input("Seleccione s/n : ")

    if afirmacion.lower() == "s":
        while True:
            try:
                Nuevo_Valor = float(input("Ingrese la nueva Valoracion (0-10): "))
                if Nuevo_Valor < 0 or Nuevo_Valor > 10:  
                    print("Valor fuera del rango (0-10)")
                    continue
                break
            except ValueError:
                print("Ingrese un número válido.")

        Recursos[indice_real]["Valoracion"] = Nuevo_Valor
        guardar_datos(dato)
        print("Se cambió correctamente")
    else:
        print("No se realizaron cambios")

def eliminar_Titulo(dato):
    cargar_datos(dato)
    indice = mostrar_opciones()
    if indice != -1:
        Recursos.pop(indice)
        guardar_datos(dato)
        print("Se elimino correctamente")

def MostarLibros(dato):
    cargar_datos(dato)
    while True:
        op = Menuopciones_extras()
        if op == 1:
            Buscar_generos(dato,"Libro")
        elif op == 2:
            Buscar_Creadores(dato,"Libro")
        elif op == 3:
            Buscar_valoraciones(dato,"Libro")
        elif op == 4:
            break
        else:
            print("Opcion invalida, por favor seleccione una opcion valida.")
    
def MostrarPeliculas(dato):
    cargar_datos(dato)
    while True:
        op = Menuopciones_extras()
        if op == 1:
            Buscar_generos(dato,"Pelicula")
        elif op == 2:
            Buscar_Creadores(dato,"Pelicula")
        elif op == 3:
            Buscar_valoraciones(dato,"Pelicula")
        elif op == 4:
            break
        else:
            print("Opcion invalida, por favor seleccione una opcion valida.")

def MostrarMusica(dato):
    cargar_datos(dato)
    while True:
        op = Menuopciones_extras()
        if op == 1:
            Buscar_generos(dato,"Musica")
        elif op == 2:
            Buscar_Creadores(dato,"Musica")
        elif op == 3:
            Buscar_valoraciones(dato,"Musica")
        elif op == 4:
            break
        else:
            print("Opcion invalida, por favor seleccione una opcion valida.")
