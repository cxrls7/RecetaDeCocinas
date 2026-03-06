# 🍴 Asistente de Cocina en Python

---

## 📌 Descripción

Este proyecto consiste en un pequeño asistente de cocina desarrollado en **Python**.
El programa permite preparar distintas recetas utilizando **funciones reutilizables**, **condicionales** y **estructuras de datos** como listas y diccionarios.

El usuario puede seleccionar entre varias recetas y el sistema mostrará los **ingredientes**, **pasos de preparación** y los detalles del plato preparado.

---

## 🎯 Objetivo del Proyecto

Aplicar conceptos fundamentales de Python como:

* Funciones
* Parámetros
* Condicionales (`if`, `elif`)
* Bucles (`while`, `for`)
* Listas
* Diccionarios
* Reutilización de funciones

---

## 🍽 Recetas disponibles

El asistente puede preparar las siguientes recetas:

1. **Ensalada César con pollo**
2. **Wrap de pollo con salsa César**
3. **Sándwich clásico de pollo**

Cada receta está implementada como una función independiente dentro del proyecto.

---

## 🧩 Funciones reutilizables

El proyecto incluye funciones reutilizables que se utilizan en varias recetas:

* `preparar_pollo_a_la_plancha(presentacion)`
* `preparar_salsa_cesar(pimienta_negra_molida)`
* `emplatado()`

Estas funciones permiten organizar el código de manera modular y reutilizable.

---

## 📂 Estructura del Proyecto

```
recetas_cocina/

│
├── src
│
│   ├── features
│   │   ├── cocina.py
│   │   └── recetas.py
│
│   └── main.py
│
├── README.md
└── .gitignore
```

### Descripción de los archivos

| Archivo      | Descripción                                                    |
| ------------ | -------------------------------------------------------------- |
| `main.py`    | Punto de entrada del programa                                  |
| `cocina.py`  | Funciones reutilizables para preparar pollo, salsa y emplatado |
| `recetas.py` | Funciones que contienen la lógica de cada receta               |

---

## ▶️ Cómo ejecutar el programa

1. Clonar el repositorio o descargar el proyecto.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python src/main.py
```

---

## 🧠 Funcionamiento del programa

El flujo del programa es el siguiente:

1. El usuario selecciona una receta desde el menú.
2. El sistema ejecuta la función correspondiente.
3. Se preparan los ingredientes y los pasos de la receta.
4. Se construye un diccionario con la información del plato.
5. Se muestran los detalles de la receta al usuario.
6. El usuario puede decidir si desea preparar otra receta.

---

## ⚙️ Requisitos

Para ejecutar este proyecto solo se necesita:

* **Python 3** instalado en el sistema.

No se utilizan librerías externas.

---

## 👨‍💻 Autor

**Carlos Daniel**

Proyecto desarrollado como ejercicio práctico para aprender el uso de **funciones, estructuras de datos y control de flujo en Python**.


