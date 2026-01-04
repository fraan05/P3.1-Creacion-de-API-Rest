from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="API de Coches")

# MODELOS ---------------------

class CocheBase(BaseModel):
    marca: str = Field(..., min_length=1)
    modelo: str = Field(..., min_length=1)
    año: int = Field(..., ge=1900)
    precio: float = Field(..., gt=0)
    disponible: bool

class CocheCreate(CocheBase):
    pass

class Coche(CocheBase):
    id: int

coches_db: List[Coche] = []
contador_id = 1

# Crear coches ---------------------
@app.post("/coches", response_model=Coche, status_code=201)
def crear_coche(coche: CocheCreate):
    global contador_id

    # Evitar coches duplicados
    for c in coches_db:
        if c.marca.lower() == coche.marca.lower() and c.modelo.lower() == coche.modelo.lower():
            raise HTTPException(status_code=400, detail="El coche ya existe")

    nuevo_coche = Coche(
        id=contador_id,
        **coche.model_dump()
    )
    contador_id += 1
    coches_db.append(nuevo_coche)
    return nuevo_coche

@app.get("/coches", response_model=List[Coche])
def obtener_coches():
    return coches_db

