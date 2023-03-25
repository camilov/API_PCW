from fastapi import APIRouter,Header
from pydantic import BaseModel,EmailStr
from app.functions_jwt  import write_token,validate_token
from fastapi.responses import JSONResponse

auth_routes = APIRouter()

class User(BaseModel):
    username: str
    email: EmailStr


@auth_routes.post("/login")
def login(user:User):
    print(user.dict())
    if user.username == "cristian":
        print("entre")
        token = write_token(user.dict())
        return token
    else:
        return JSONResponse(content={"message": "User not found"},status_code=404)
        
    
@auth_routes.post("/verify/token")
def verify_token(Authorizacion:str=Header(None)):
    print(Authorizacion)
    token = Authorizacion
    return validate_token(token,output=True)