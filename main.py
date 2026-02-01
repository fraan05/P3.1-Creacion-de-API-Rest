from fastapi import FastAPI
from database.database import Base, engine
from routes.rutas_marca import router as brand_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(brand_routes)
