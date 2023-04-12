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

#Ruta para obtener todos los clientes
@clientes.get('/clientes_todo/',response_model=schemas.cl)
def show_clientes(db:Session=Depends(get_db)):
    clientes = {"status":"sucess","Lista":db.query(models.Clientes).all()}
    #print(clientes)
    return clientes

#Ruta para obtener los clientes por nombre
@clientes.get('/clientes/{nombre}',response_model=schemas.cl)
def show_clientes(nombre:str,db:Session=Depends(get_db)):
    clientes = {"status":"sucess","Lista":db.query(models.Clientes).filter(models.Clientes.nombre.ilike(f'%{nombre}%')).all()}
    #print(clientes)
    return clientes

#Ruta para guardar nuevo cliente
@clientes.post('/create_clientes/',response_model=schemas.Clientes)
def create_clientes(entrada:schemas.Clientes,db:Session=Depends(get_db)):
    cliente = models.Clientes(nombre =entrada.nombre)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

#Ruta para modificar cliente
@clientes.put('/modificar_Cliente/{idCliente}',response_model=schemas.Clientes)
def modify_cliente(idCliente:int,entrada:schemas.ModificarClientes,db:Session=Depends(get_db)):
    cliente = db.query(models.Clientes).filter_by(idCliente=idCliente).first()
    cliente.nombre=entrada.nombre
    db.commit()
    db.refresh(cliente)
    return cliente
