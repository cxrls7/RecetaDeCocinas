from src.features.recetas import(preparar_ensalada_cesar, preparar_wrap_cesar, preparar_sandwich_pollo)

def asistente_de_cocina():
    print("Bienvenido al asistente de cocina. ¿Qué receta te gustaría preparar?")
    print("1. Ensalada César")
    print("2. Wrap César")
    print("3. Sándwich de Pollo")

    opcion = input("Seleccione una opcion:")
    if opcion == "1":
        receta = preparar_ensalada_cesar()
    elif opcion == "2":
        receta = preparar_wrap_cesar()
    elif opcion == "3":
        receta = preparar_sandwich_pollo()
    else:
        print("Opción no válida")
        return
    
    print("\n Plato preparado con éxito! Aquí tienes los detalles de la receta:")
    print(receta)


if __name__ == "__main__":
    asistente_de_cocina()