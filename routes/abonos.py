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
def create_abonos(data: schemas.AbonoRequestData,db:Session=Depends(get_db)): 

    

    
   
    try:
        abono_data = data.abonoData
        movimiento_data = data.movimientoData
        tarjeta_data = data.tarjetaData

        abonos = models.Abonos(idTarjeta  =abono_data.idTarjeta ,
                           numCuota   =abono_data.numCuota  ,
                           valorAbono =abono_data.valorAbono,
                           fechaAbono =abono_data.fechaAbono)
    
        movimientos = models.Movimientos(idMovimiento = movimiento_data.idMovimiento,
                                         entrada      = movimiento_data.entrada     ,
                                         salida       = movimiento_data.salida      ,
                                         tipMvto      = movimiento_data.tipMvto     ,
                                         idTarjeta    = movimiento_data.idTarjeta   ,
                                         idCliente    = movimiento_data.idCliente   ,
                                         fecMvto      = movimiento_data.fecMvto     ,
                                         mcaAjuste    = movimiento_data.mcaAjuste   )
    

        tarjeta = db.query(models.Tarjetas).filter_by(idTarjeta=abono_data.idTarjeta).first()
        tarjeta.numCuotas= tarjeta_data.numCuotas
        tarjeta.valorTotal= tarjeta_data.valorTotal
        tarjeta.fecActu = tarjeta_data.fecActu

    except Exception as e:
        print(f"Error al guardar: {str(e)}")
        raise e
    
    try:
        #INSERTAR ABONO
        db.add(abonos)

        #INSERTAR MOVIMIENTO
        db.add(movimientos)

        #ACTUALIZAR TARJETA
        db.add(tarjeta)

        #COMMIT
        db.commit()
        db.refresh(abonos)
        #db.refresh(movimientos)
        


    except Exception as e:
        print(f"Error al guardar: {str(e)}")
        raise e


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

#Ruta para eliminar abonos
@abonos.delete('/eliminar_abono/{idAbono}',response_model=schemas.ResponseDeleteAbonos)
def delete_abonos(idAbono:int,db:Session=Depends(get_db)):
    abono = db.query(models.Abonos).filter_by(idAbono=idAbono).first()

    try:
        db.delete(abono)
        db.commit()
        respuesta = schemas.ResponseDeleteAbonos(response = "eliminado exitosamente")
    
    except Exception as e:
        print(f"Error al eliminar el abono: {str(e)}")
        raise e


    return respuesta