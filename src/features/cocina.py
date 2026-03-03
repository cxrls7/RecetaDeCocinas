def preparar_pollo_a_la_plancha(presentacion):
    """"
    Prepara el pollo segun la presentacion
    """""
    
    if presentacion == "tiras":
        descripcion = "Pollo a la plancha cortado en tiras"
    else: 
        descripcion = "Pollo a la plancha en presentacion normal"

    return descripcion

def preparar_salsa_cesar(pimienta_negra_molida):
    """"
    Prepara la salsa cesar.
    """""
    
    salsa = { 
        "sal": "al gusto",
        "zumo de limon":"10 ml",
        "pimienta negra": "No"
    }

    if pimienta_negra_molida:
        salsa["pimienta negra"] = "Sí"
    return salsa


def emplatado(receta, salsa, presentacion_pollo, ingredientes, pasos):
    """
    Construye el diccionario al final del plato
    """

    return {
        "receta": receta,
        "salsa": salsa,
        "presentacion_pollo": presentacion_pollo,
        "ingredientes": ingredientes,
        "pasos": pasos
    }
