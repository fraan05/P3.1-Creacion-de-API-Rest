from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.coche import Coche
from schemas.coche import CrearCoche, MostrarCoche

router = APIRouter(prefix="/coches", tags=["Coches"])

@router.get("/", response_model=list[MostrarCoche])
def get_coches(db: Session = Depends(get_db)):
    return db.query(Coche).all()

@router.get("/{coche_id}", response_model=MostrarCoche)
def get_coche(coche_id: int, db: Session = Depends(get_db)):
    coche = db.query(Coche).filter(Coche.id == coche_id).first()
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche

@router.post("/", response_model=MostrarCoche)
def create_coche(coche: CrearCoche, db: Session = Depends(get_db)):
    nuevo_coche = Coche(**coche.dict())
    db.add(nuevo_coche)
    db.commit()
    db.refresh(nuevo_coche)
    return nuevo_coche

@router.delete("/{coche_id}")
def delete_coche(coche_id: int, db: Session = Depends(get_db)):
    coche = db.query(Coche).filter(Coche.id == coche_id).first()
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    db.delete(coche)
    db.commit()
    return {"message": "Coche eliminado correctamente"}