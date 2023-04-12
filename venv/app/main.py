from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from . import models,schemas
from .Conexion import SessionLocal,engine
from sqlalchemy.orm import Session
from typing import List
from dotenv import load_dotenv,find_dotenv
from routes.auth import auth_routes
from routes.clientes import clientes
from routes.tarjetas import tarjetas
from routes.abonos import abonos


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_routes,prefix="/api")
app.include_router(clientes,prefix="/api")
app.include_router(tarjetas,prefix="/api")
app.include_router(abonos,prefix="/api")
load_dotenv(find_dotenv())


