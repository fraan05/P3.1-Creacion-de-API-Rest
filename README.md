# Práctica 3.1 – API REST con FastAPI

Alumno: Francisco Alexandru
Apellido: Babei

## Descripción
En esta práctica se ha desarrollado una API REST utilizando FastAPI.
La API permite gestionar una colección de coches mediante operaciones CRUD
(crear, leer, actualizar y eliminar).

## Ejecución del servidor FastAPI
Para lanzar el servidor FastAPI se deben seguir los siguientes pasos:

1. Instalar las dependencias del proyecto: "pip install -r requirements.txt"

2. Ejecutar el servidor: "uvicorn main:app --reload"

3. Una vez iniciado, se puede acceder a la documentación automática en: "http://127.0.0.1:8000/docs"


Desde esta URL se pueden probar todas las rutas de la API.

## Justificación del dominio de datos
El dominio elegido es la gestión de coches, ya que se trata de un
ejemplo sencillo y claro que permite trabajar con distintos tipos de datos
(texto, números y valores booleanos).
