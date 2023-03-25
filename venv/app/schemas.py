from pydantic import BaseModel
from typing import Optional,List

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

