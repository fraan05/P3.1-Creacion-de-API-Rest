from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.marca import Marca
from schemas.marca import CrearMarca, MostrarMarca

router = APIRouter(prefix="/marcas", tags=["Marcas"])

@router.get("/", response_model=list[MostrarMarca])
def get_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()

@router.get("/{marca_id}", response_model=MostrarMarca)
def get_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return marca

@router.post("/", response_model=MostrarMarca)
def create_marca(marca: CrearMarca, db: Session = Depends(get_db)):
    marca = Marca(**marca.dict())
    db.add(marca)
    db.commit()
    db.refresh(marca)
    return marca

@router.delete("/{marca_id}")
def delete_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    db.delete(marca)
    db.commit()
    return {"message": "Marca eliminada"}
