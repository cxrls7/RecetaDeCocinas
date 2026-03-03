from src.features.recetas import(preparar_ensalada_cesar, preparar_wrap_cesar, preparar_sandwich_pollo)

from src.features.recetas import (
    preparar_ensalada_cesar,
    preparar_wrap_cesar,
    preparar_sandwich_pollo
)


def asistente_cocina():
    continuar = "si"

    while continuar.lower() == "si":

        print("\n🍴 Bienvenido al Asistente de Cocina Virtual 🍴")
        print("1. Ensalada César con pollo")
        print("2. Wrap de pollo con salsa César")
        print("3. Sándwich clásico de pollo")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            receta = preparar_ensalada_cesar()
        elif opcion == "2":
            receta = preparar_wrap_cesar()
        elif opcion == "3":
            receta = preparar_sandwich_pollo()
        else:
            print("Opción no válida")
            continue  

        
        print("\n🍽 ===== DETALLE DEL PLATO ===== 🍽")
        print(f"Receta: {receta['receta']}")
        print(f"Presentación del pollo: {receta['presentacion_pollo']}")

        if receta["salsa"]:
            print("\n Salsa César:")
            for clave, valor in receta["salsa"].items():
                print(f"  - {clave}: {valor}")

        print("\n Ingredientes:")
        for ingrediente in receta["ingredientes"]:
            print(f"  - {ingrediente}")

        print("\n Pasos:")
        for i, paso in enumerate(receta["pasos"], 1):
            print(f"  {i}. {paso}")

    
        continuar = input("\n¿Deseas preparar otra receta? (si/no): ")

    print("\n Gracias por usar el asistente de cocina. ¡Hasta luego!")



if __name__ == "__main__":
    asistente_cocina()