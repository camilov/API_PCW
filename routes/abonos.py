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

abonos = APIRouter()

#route_class=VerifyTokenRoute
#Authorizacion:str=Header(None)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close

@abonos.get("/")
def main():
    return RedirectResponse(url="/docs/")


#response_model=List[schemas.Clientes]

#Ruta para obtener las tarjetas de un cliente por idCliente
@abonos.get('/abonos/{idTarjeta}',response_model=schemas.ShowAbonosCl)
def show_abonos(idTarjeta:int,db:Session=Depends(get_db)):
    abonos = {"status":"sucess","Lista":db.query(models.Abonos).filter(models.Abonos.idTarjeta == idTarjeta).order_by(models.Abonos.idAbono.asc()).all()}
    #print(clientes)
    return abonos
