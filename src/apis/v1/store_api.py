from tasks import store_key_value_to_redis, delete_key_from_redis, huey
from pydantic import BaseModel
from typing import Any
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from tasks import red as redis_client

router_v1 = APIRouter(prefix="/apis/v1", tags=["v1"], responses={404: {"description": "Not found"}})

class Input(BaseModel):
    key:Any
    value:Any

@router_v1.post("/store")
async def store_key_value_endpoint(input: Input):
    try:
        key = input.key
        value = input.value
        if key == None or value == None:
            out = 'Bad request'
            return JSONResponse(status_code=400, content=jsonable_encoder(out))
        # Properly dispatch the task to Huey
        store_key_value_to_redis(key, value)  # Notice the .delay() here
        out = {key : value}
        return JSONResponse(status_code=201, content=jsonable_encoder(out))
    except:
        out = 'Internal Server Error'
        return JSONResponse(status_code=500, content=jsonable_encoder(out)) 
    
class KeyInput(BaseModel):
    key: Any

@router_v1.delete("/store")
async def delete_key_endpoint(input: KeyInput):
    try:
        key = input.key
        
        if not redis_client.exists(key):
            return JSONResponse(status_code=404, content=jsonable_encoder("Key not found"))

        if key is None:
            return JSONResponse(status_code=400, content=jsonable_encoder('Bad request'))
        # Dispatch the delete task to Huey
        delete_key_from_redis(key)
        return JSONResponse(status_code=200, content=jsonable_encoder(f'Key {key} scheduled for deletion'))
    except Exception as e:
        return JSONResponse(status_code=500, content=jsonable_encoder('Internal Server Error'))
