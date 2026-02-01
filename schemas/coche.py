from pydantic import BaseModel

class CocheBase(BaseModel):
    modelo: str
    años: int
    precio: float
    disponible: bool
    marca_id: int

class CrearCoche(CocheBase):
    pass

class MostrarCoche(CocheBase):
    id: int

    class Config:
        orm_mode = True