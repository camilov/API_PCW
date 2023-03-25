from fastapi import Request
from app.functions_jwt import validate_token 
from fastapi.routing import APIRoute

class VerifyTokenRoute(APIRoute):
    print("verified 1")
    def get_route_handler(self):
        original_route = super().get_route_handler()
        print("verified 2")

        async def verify_token_middleware(request:Request):
            print("verified 3")
            token = request.headers["Authorizacion"]
            validation_reponse =validate_token(token,output=False)
            print("verified 4")

            if validation_reponse == None:
                print("llega a verificar token")
                return await original_route(request)
            else:
                return validate_token
        return verify_token_middleware
             
    