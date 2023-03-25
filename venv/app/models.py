from sqlalchemy import Column, Integer, String
from .Conexion import Base

class Clientes(Base):
    __tablename__= 'clientes'
    idCliente = Column(Integer,primary_key=True,index=True)
    nombre    = Column(String(200))