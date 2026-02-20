from Datos import *

def seperador():
    print("======================================================================================")

def mostrar_recurso(recurso):
    print(" | Tipo de archivo :" + recurso["Elemento"],
          " | Nombre: " + recurso["Nombre"],
          " | Genero :" + recurso["Genero"],
          " | Autor: " + recurso["Creadores"],
          " | Valoracion: " + str(recurso["Valoracion"]))  

def mostrar_recurso_Listado(Cantidad,Recurso):
    print(Cantidad, 
          "- | Tipo de archivo :" + Recurso["Elemento"],
          " | Nombre: " + Recurso["Nombre"],
          " | Genero :" + Recurso["Genero"],
          " | Autor: " + Recurso["Creadores"],
          " | Valoracion: " + str(Recurso["Valoracion"]))  

def indiceFloat(Dato):
    listado = []
    for i in range(0,len(Recursos)):
        valor = Recursos[i]["Valoracion"]
        if valor == Dato:
            listado.append(i)
    return listado

def mostrar_opciones():
    print("Ingrese el número del archivo a eliminar")
    cantidad = len(Recursos)
    for i in range(0, cantidad):
        print(i, "-", Recursos[i]["Elemento"], "-", Recursos[i]["Nombre"])
    try:
        numero_producto = int(input("Ingrese su selección: "))
    except ValueError:
        print("Entrada inválida")
        return -1
    if (numero_producto < 0 or numero_producto >= cantidad):
        print("Opción no válida")
        numero_producto = -1
    seperador()
    return numero_producto

def indiceGeneral(valor_buscar, campo):
    indices = [] 
    for i in range(len(Recursos)):
        valor = Recursos[i][campo]
        if str(valor).lower() == str(valor_buscar).lower():
            indices.append(i)  
    return indices 

def verificacion_Float(dato):
    for i in Recursos:
        datos = i.get("Valoracion")
        if datos is not None and datos == dato:
            return True
    return False

def Verificacion_Autor(nombre):
    for i in Recursos:
        autor = i.get("Creadores")
        if autor and autor.lower() == nombre.lower():
            return True
    return False

def Verficacion_Genero(Genero):
    for i in Recursos:
        genero = i.get("Genero")
        if genero and genero.lower() == Genero.lower():
            return True
    return False

def Verificaion_antes_de_agg(nombre_buscar, tipo_elemento):
    for i in Recursos:
        recurso = i.get(tipo_elemento)
        if recurso and recurso.lower() == nombre_buscar.lower():
            return True
    return False
 
def Buscar_generos(dato,campo):
    cargar_datos(dato)
    Genero = str(input("Ingrese el nombre del genero que desea buscar: ")).strip()
    if Verficacion_Genero(Genero): 
        for i in Recursos:
            if i is not None and (i.get('Elemento') == campo and i.get('Genero').lower() == Genero.lower()):
                mostrar_recurso(i) 
    else:
        print("No existe ningun archivo con este genero ")

def Buscar_Creadores(dato,campo):
    cargar_datos(dato)
    Autor = str(input("Ingrese el nombre del autor que desea buscar: ")).strip()
    if Verificacion_Autor(Autor): 
        for i in Recursos:
            if i is not None and (i.get('Elemento') == campo and i.get('Creadores').lower() == Autor.lower()):
                mostrar_recurso(i) 
    else:
        print("No existe ningun archivo con este autor ")

def Buscar_valoraciones(dato,campo):
    cargar_datos(dato)
    Valoracion = float(input("Ingrese el nombre del genero que desea buscar: "))
    if verificacion_Float(Valoracion): 
        for i in Recursos:
            if i is not None and (i.get('Elemento') == campo and i.get('Valoracion') == Valoracion):
                mostrar_recurso(i) 
    else:
        print("No existe ningun archivo con esa valoracion ")
