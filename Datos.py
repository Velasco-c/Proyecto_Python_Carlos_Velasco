from json import load,dumps
Recursos = []

def leer_Json(nombre_archivo):
    try:
        Respaldo = []
        with open(nombre_archivo, "r") as file:
            Respaldo = load(file)
            return Respaldo
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
    with open(nombre_archivo, "w") as file:
        file.write("[]")
    return []
   
def escribir_json(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w") as file:
            contenido_a_guardar = dumps(contenido, indent=2)
            file.write(contenido_a_guardar)
    except TypeError:
        print("Error: Los datos no se pueden convertir a JSON.")
         
def cargar_datos(nombre_archivo):
    Recursos.clear()
    Recursos.extend(leer_Json(nombre_archivo))
    
def guardar_datos(nombre_archivo):
    escribir_json(nombre_archivo, Recursos)

