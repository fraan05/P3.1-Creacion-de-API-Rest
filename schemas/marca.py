from pydantic import BaseModel

class MarcaBase(BaseModel):
    nombre: str
    pais_origen: str

class CrearMarca(MarcaBase):
    pass

class MostrarMarca(MarcaBase):
    id: int

    class Config:
        orm_mode = True