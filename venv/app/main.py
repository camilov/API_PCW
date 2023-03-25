from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from . import models,schemas
from .Conexion import SessionLocal,engine
from sqlalchemy.orm import Session
from typing import List
from dotenv import load_dotenv,find_dotenv
from routes.auth import auth_routes
from routes.clientes import clientes

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_routes,prefix="/api")
app.include_router(clientes,prefix="/api")
load_dotenv(find_dotenv())

"""def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/clientes/',response_model=List[schemas.Clientes])
def show_clientes(db:Session=Depends(get_db)):
    clientes = db.query(models.Clientes).all()
    return clientes"""

