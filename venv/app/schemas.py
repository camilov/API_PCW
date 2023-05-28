from pydantic import BaseModel, ValidationError, validator
from typing import Optional,List
from datetime import datetime, date

############################################## CLIENTES #####################################

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


############################################## TARJETAS #####################################

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

class modifyTarjetaAbono(BaseModel):

    valorTotal    :float
    numCuotas     :int
    fecActu       :date

    class Config:
        orm_mode = True



############################################## ABONOS #####################################

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

class ModificarAbonos(BaseModel):
    numCuota      :int
    valorAbono    :float
    
    class Config:
        orm_mode = True

class ModificarAbonosTarjeta(BaseModel):
    valorTotal : float
    numCuotas  : int
    fecActu    : date


class ResponseDeleteAbonos(BaseModel):

    response : str



class createMovimientoAbono(BaseModel):
    idMovimiento : Optional[int]
    entrada      : float
    salida       : float
    tipMvto      : str
    idTarjeta    : int
    idCliente    : int
    fecMvto      : date
    mcaAjuste    : int

    class Config:
        orm_mode = True


class AbonoRequestData(BaseModel):

    print("Entre a class abonorequestdata:")
    try:
        abonoData: showAbonos
        movimientoData: createMovimientoAbono
        tarjetaData: modifyTarjetaAbono
    
        
    except Exception as e:
        print(f"Error al guardar: {str(e)}")
        raise e
    
    print("Termina class abonorequestdata:")


class AbonoRequestModifyData(BaseModel):

    try:
        abonoData: ModificarAbonos
        tarjetaData: ModificarAbonosTarjeta
        movimientoData: createMovimientoAbono
    
        
    except Exception as e:
        print(f"Error al guardar: {str(e)}")
        raise e