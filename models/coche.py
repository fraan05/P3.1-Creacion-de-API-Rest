from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Coche(Base):
    __tablename__ = "coches"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    año = Column(Integer)
    precio = Column(Float)
    disponible = Column(Boolean)
    marca_id = Column(Integer, ForeignKey("marcas.id"))

    marca = relationship("Marca", back_populates="coches")