from jwt import encode,decode
from datetime import datetime,timedelta
import os
from jwt import exceptions
from fastapi.responses import JSONResponse
from dotenv import load_dotenv,find_dotenv

SECRET = 'absc1'

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def write_token(data: dict):
    print(SECRET)
    token = encode(payload={**data,"exp": expire_date(2)}, key=SECRET,algorithm="HS256")
    return token

def validate_token(token,output=False):
    try:
        if output:
           return decode(token,key=SECRET,algorithms=["HS256"])
        decode(token,key=SECRET,algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message":"Invalid Token"},status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message":"Token Expired"},status_code=401)
    
 