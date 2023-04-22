from pydantic import BaseModel, ValidationError, validator
from typing import Optional,List
from datetime import datetime, date


class Clientes(BaseModel):
    idCliente:Optional[int]
    nombre:str
    
    class Config:
        orm_mode = True



class cl(BaseModel):
    status:str
    Lista:List[Clientes]

    class Config:
        orm_mode = True


class ModificarClientes(BaseModel):
    nombre:str
    
    class Config:
        orm_mode = True

class ShowTarjetas(BaseModel):

    idTarjeta     :Optional[int]
    idCliente     :int
    valorPrestado :float
    valorTotal    :float
    fechaPrestamo :date
    numCuotas     :int
    idEstado      :int
    interes       :float|None
    valorDefecto  :int
    fecActu       :date

    

    class Config:
        orm_mode = True


class ShowTarjetasCl(BaseModel):
    status:str
    Lista:List[ShowTarjetas]

    class Config:
        orm_mode = True

class responseCreateTarjetas(BaseModel):
    status:str

    class Config:
        orm_mode = True

class showAbonos(BaseModel):

    idAbono       :Optional[int]
    idTarjeta     :int
    numCuota      :int
    valorAbono    :float
    fechaAbono    :date

    class Config:
        orm_mode = True

class ShowAbonosCl(BaseModel):
    status:str
    Lista:List[showAbonos]

    class Config:
        orm_mode = True

