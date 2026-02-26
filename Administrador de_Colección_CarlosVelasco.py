from Utilidades import Menu_Principal,Salida
from Funciones_Principales import *

Name_Archivo = "Recurso.json"
Name_Archivo2 = "promedio_valoraciones.json"
while True:
    opc = Menu_Principal()
    if opc == 8:
        Salida()
        break
    elif opc == 1:
        añadir(Name_Archivo)
    elif opc == 2:
        Listado_Elemento(Name_Archivo)
    elif opc == 3:
        Buscar(Name_Archivo)
    elif opc == 4:
        Editar_Elemento(Name_Archivo)
    elif opc == 5:
        Eliminar_Elemento(Name_Archivo)
    elif opc == 6:
        Ver_Categorias(Name_Archivo)
    elif opc == 7:
        promedio_valoraciones(Name_Archivo)
    else:
        print("opcion no valida, Vuelvelo a intentar")
