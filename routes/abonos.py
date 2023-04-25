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


#Ruta para guardar nuevo abono de tarjeta
@abonos.post('/create_abono/',response_model=schemas.showAbonos)
def create_abonos(entrada:schemas.showAbonos,db:Session=Depends(get_db)):
    abonos = models.Abonos(idTarjeta =entrada.idTarjeta,numCuota =entrada.numCuota,valorAbono =entrada.valorAbono,fechaAbono =entrada.fechaAbono)
    #numCuota     = Column(Integer)
    #valorAbono   = Column(Float)
    #fechaAbono   = Column(Date)
    
    db.add(abonos)
    db.commit()
    db.refresh(abonos)
    return abonos

#Ruta para modificar abonos
@abonos.put('/modificar_abono/{idAbono}',response_model=schemas.showAbonos)
def modify_abonos(idAbono:int,entrada:schemas.ModificarAbonos,db:Session=Depends(get_db)):
    abono = db.query(models.Abonos).filter_by(idAbono=idAbono).first()
    abono.numCuota=entrada.numCuota
    abono.valorAbono=entrada.valorAbono
    db.commit()
    db.refresh(abono)
    return abono
