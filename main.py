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