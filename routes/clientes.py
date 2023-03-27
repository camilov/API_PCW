from fastapi import APIRouter,Header
from pydantic import BaseModel
from app import models,schemas
from app.Conexion import SessionLocal,engine
from starlette.responses import RedirectResponse
from typing import List
from sqlalchemy.orm import Session
from fastapi.params import Depends
from middlewares.verify_token_routes import VerifyTokenRoute


models.Base.metadata.create_all(bind=engine)

clientes = APIRouter()

#route_class=VerifyTokenRoute
#Authorizacion:str=Header(None)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close

@clientes.get("/")
def main():
    return RedirectResponse(url="/docs/")


#response_model=List[schemas.Clientes]

@clientes.get('/clientes_todo/',response_model=schemas.cl)
def show_clientes(db:Session=Depends(get_db)):
    clientes = {"status":"sucess","Lista":db.query(models.Clientes).all()}
    #print(clientes)
    return clientes

@clientes.get('/clientes/{nombre}',response_model=schemas.cl)
def show_clientes(nombre:str,db:Session=Depends(get_db)):
    clientes = {"status":"sucess","Lista":db.query(models.Clientes).filter(models.Clientes.nombre.ilike(f'%{nombre}%')).all()}
    #print(clientes)
    return clientes

