from src.features.cocina import (preparar_pollo_a_la_plancha, preparar_salsa_cesar, emplatado)

def preparar_ensalada_cesar():
    pollo = preparar_pollo_a_la_plancha("tiras")
    salsa = preparar_salsa_cesar(True)

    ingredientes = ["Lechuga", "Queso parmesano", "Crutones", pollo ]

    pasos = [
        "Lavar y cortar la lechuga",
        "Agregar el pollo en tiras",
        "Añadir el queso parmesano",
        "Incorporar la salsa cesar",
    ]

    return emplatado("ensalada", salsa, "tiras", ingredientes, pasos)

def preparar_sandwich_pollo():
    pollo = preparar_pollo_a_la_plancha("normal")

    ingredientes = ["Pan de sándwich", "Lechuga", "Tomate", pollo ]

    pasos = [
        "Tostar el pan de sándwich",
        "Agregar el pollo a la plancha",
        "Añadir la lechuga y el tomate",
        "Agregar queso"
    ]

    return emplatado("sandwich", None, "normal", ingredientes, pasos)


