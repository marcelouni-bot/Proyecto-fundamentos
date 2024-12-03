from enum import Enum

class Prioridad(Enum):
    BAJA = 0
    MEDIA = 1
    ALTA = 2
#Creamos la clase tarea con los atributos de descripcion, prioridad y si está completada o no
class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
#funcion para agregar tareas leyendo los atributos ingresados por el usuario
def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ")
    prioridad = int(input("Ingrese la prioridad de la tarea (0 = Baja, 1 = Media, 2 = Alta): "))
    tarea = Tarea(descripcion, Prioridad(prioridad))
    tareas.append(tarea)
#funcion que busca la tarea por el índice ingresado y cambia el atributo completada
def marcar_completada(tareas):
    indice = int(input("Ingrese el índice de la tarea a marcar como completada: "))
    if 0 <= indice < len(tareas):
        tareas[indice].completada = True
    else:
        print("Índice inválido.")
#funcion que ordena la lista de tareas por prioridad y las imprime
def mostrar_tareas(tareas):
    tareas_ordenadas = sorted(tareas, key=lambda x: x.prioridad.value, reverse=True)
    for i, tarea in enumerate(tareas_ordenadas):
        print(f"{i}. Descripción: {tarea.descripcion}, Prioridad: {tarea.prioridad.name}, Completada: {'Sí' if tarea.completada else 'No'}")
#funcion actualiza la descripción y la prioridad ingresadas por el usuario 
def editar_tarea(tareas):
    indice = int(input("Ingrese el índice de la tarea a editar: "))
    if 0 <= indice < len(tareas):
        descripcion = input("Ingrese la nueva descripción: ")
        prioridad = int(input("Ingrese la nueva prioridad (0 = Baja, 1 = Media, 2 = Alta): "))
        tareas[indice].descripcion = descripcion
        tareas[indice].prioridad = Prioridad(prioridad)
    else:
        print("Índice inválido.")
#funcion que elimina un elemento del arreglo de tareas
def eliminar_tarea(tareas):
    indice = int(input("Ingrese el índice de la tarea a eliminar: "))
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
    else:
        print("Índice inválido.")
#funcion que busca una tarea mediante el indice ingresado por el usuario
def buscar_tarea(tareas):
    keyword = input("Ingrese una palabra clave para buscar tareas: ")
    for i, tarea in enumerate(tareas):
        if keyword.lower() in tarea.descripcion.lower():
            print(f"{i}. Descripción: {tarea.descripcion}, Prioridad: {tarea.prioridad.name}, Completada: {'Sí' if tarea.completada else 'No'}")
def main():
    tareas = []  #creamos un arreglo vacío de tareas que se irán llenando
    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Ordenar y mostrar tareas por prioridad")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Buscar tarea")
        print("7. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            agregar_tarea(tareas)
        elif opcion == 2:
            marcar_completada(tareas)
        elif opcion == 3:
            mostrar_tareas(tareas)
        elif opcion == 4:
            editar_tarea(tareas)
        elif opcion == 5:
            eliminar_tarea(tareas)
        elif opcion == 6:
            buscar_tarea(tareas)
        elif opcion == 7:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
