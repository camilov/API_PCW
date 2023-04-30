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

tarjetas = APIRouter()

#route_class=VerifyTokenRoute
#Authorizacion:str=Header(None)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close

@tarjetas.get("/")
def main():
    return RedirectResponse(url="/docs/")


#response_model=List[schemas.Clientes]

#Ruta para obtener las tarjetas de un cliente por idCliente
@tarjetas.get('/tarjetas_id/{idCliente}',response_model=schemas.ShowTarjetasCl)
def show_tarjetas(idCliente:int,db:Session=Depends(get_db)):
    tarjetas = {"status":"sucess","Lista":db.query(models.Tarjetas).filter(models.Tarjetas.idCliente == idCliente).order_by(models.Tarjetas.idEstado.asc()).all()}
    #print(clientes)
    return tarjetas


#Ruta para crear tarjeta
@tarjetas.post('/create_tarjeta/',response_model=schemas.responseCreateTarjetas)
def create_tarjeta(entrada:schemas.ShowTarjetas,db:Session=Depends(get_db)):

    tarjeta = models.Tarjetas(idTarjeta     = entrada.idTarjeta    ,
                              idCliente     = entrada.idCliente    ,
                              valorPrestado = entrada.valorPrestado,
                              valorTotal    = entrada.valorTotal   ,
                              fechaPrestamo = entrada.fechaPrestamo,
                              numCuotas     = entrada.numCuotas    ,
                              idEstado      = entrada.idEstado     ,
                              interes       = entrada.interes      ,
                              valorDefecto  = entrada.valorDefecto ,
                              fecActu       = entrada.fecActu      )  
   
    
    try:
        db.add(tarjeta)
        db.commit()
        tarjetas = {"status":"sucesss"}
    
    except Exception as e:
        print(f"Error al refrescar la tarjeta: {str(e)}")
        raise e
    
   # try:
   #     db.refresh(tarjeta)
   # except Exception as e:
   #     # manejo de la excepción
   #     print(f"Error al refrescar la tarjeta: {str(e)}")
   #     raise e
    
    

    return tarjetas
