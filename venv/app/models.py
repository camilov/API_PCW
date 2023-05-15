from sqlalchemy import Column, Integer, String,Float,Date
from .Conexion import Base


class Clientes(Base):
    __tablename__= 'clientes'
    idCliente = Column(Integer,primary_key=True,index=True)
    nombre    = Column(String(200))


class Tarjetas(Base):
    __tablename__= 'tarjetas'
    idTarjeta       = Column(Integer,primary_key=True,index=True)
    idCliente       = Column(Integer)
    valorPrestado   = Column(Float)
    valorTotal      = Column(Float)
    fechaPrestamo   = Column(Date)
    numCuotas       = Column(Integer)
    idEstado        = Column(Integer)
    interes         = Column(Float)
    valorDefecto    = Column(Integer)
    fecActu         = Column(Date)


class Abonos(Base):
    __tablename__= 'abonos'
    idAbono      = Column(Integer,primary_key=True,index=True)
    idTarjeta    = Column(Integer)
    numCuota     = Column(Integer)
    valorAbono   = Column(Float)
    fechaAbono   = Column(Date)

class Movimientos(Base):
    __tablename__= 'movimientos'
    idMovimiento = Column(Integer,primary_key=True,index=True)
    entrada      = Column(Float)
    salida       = Column(Float)
    tipMvto      = Column(String(3))
    idTarjeta    = Column(Integer)
    idCliente    = Column(Integer)
    fecMvto      = Column(Date)
    mcaAjuste    = Column(Integer)