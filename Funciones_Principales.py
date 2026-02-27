from Datos import * 
from Utilidades import *
from Funciones_adicionales import *

def añadir(dato):
    cargar_datos(dato)
    while True:
       opc = Menu_opcion_1()
       if opc == 4:
        break
       elif opc == 1:
        Agg_Libro =  agg_recurso("Libro", "autor del libro")
        if Agg_Libro != None:
            Recursos.append(Agg_Libro)
            guardar_datos(dato)
            print("Se añadio correctamente")
       elif opc == 2:
        Agg_Pelicula = agg_recurso("Pelicula", "productor de la pelicula")
        if Agg_Pelicula != None:
            Recursos.append(Agg_Pelicula)
            guardar_datos(dato)
            print("Se añadio correctamente")
       elif opc == 3:
        Agg_Musica = agg_recurso("Musica", "artista de la musica")
        if Agg_Musica != None:
            Recursos.append(Agg_Musica)
            guardar_datos(dato)
            print("Se añadio correctamente")
       else:
        print("Error vuelvelo a intentar")

def Listado_Elemento(dato):
    cargar_datos(dato)
    while True:
        opc1 = Menu_opcion_2()
        if opc1 == 4:
            break
        elif opc1 == 1:
            mostrar_por_elemento(dato, 'Libro')
        elif opc1 == 2:
            mostrar_por_elemento(dato, 'Pelicula')
        elif opc1 == 3:
            mostrar_por_elemento(dato, 'Musica')
        else:
            print("Error vuelvalo a intentar")

def Buscar(dato):
    cargar_datos(dato)
    while True:
        opc2 = Menu_opcion_3()
        if opc2 == 4:
            break
        elif opc2 == 1:          
            Busqueda(dato,'Nombre','titulo')        
        elif opc2 == 2:
            Busqueda(dato,'Creadores','autor')
        elif opc2 == 3:
            Busqueda(dato,'Genero','genero')
        else:
            print("Opción no válida")

def Editar_Elemento(dato):
   cargar_datos(dato)
   while True:
        opc3 = Menu_opcion_4()
        if opc3 == 5:
            break
        elif opc3 == 1:
            editarTitulo(dato)
        elif opc3 == 2:
            EditarCreador(dato)
        elif opc3 == 3:
            EditarGenero(dato)
        elif opc3 == 4:
            EditarValoracion(dato)
        else:
            print("Opcion no valida vuelvelo a intentar")

def Eliminar_Elemento(dato):
   cargar_datos(dato)
   while True:
    opc4 = Menu_opcion_5()
    if opc4 == 2:
        break
    elif opc4 == 1:
        eliminar_Titulo(dato)
    else:
        print("opcion no valida") 

def Ver_Categorias(dato):
   cargar_datos(dato)
   while True:
    opc5 = Menu_opcion_6()
    if opc5 == 4:
        break
    elif opc5 == 1:
        MostarLibros(dato)
    elif opc5 == 2:
        MostrarPeliculas(dato)
    elif opc5 == 3:
        MostrarMusica(dato)
    else:
         print("opcion no valida")

def promedio_valoraciones(data,data2):
   cargar_datos(data)
   while True:
    opc6 = Menu_opcion_7()
    if opc6 == 4:
        break
    if opc6 == 1:
        Buscar_valoracion_categoria(data,"Libro",data2)
    elif opc6 == 2:
        Buscar_valoracion_categoria(data,"Pelicula",data2)
    elif opc6 == 3:
        Buscar_valoracion_categoria(data,"Musica",data2)
    else:
        print("Opcion invalida, por favor seleccione una opcion valida.")