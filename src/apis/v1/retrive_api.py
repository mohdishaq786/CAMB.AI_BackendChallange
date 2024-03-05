from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from tasks import retrieve_value_from_redis, huey  # Assuming these are defined properly
from typing import Any
from pydantic import BaseModel
import traceback
from tasks import red as redis_client
# building api router 
router_v1 = APIRouter(prefix="/apis/v1", tags=["v1"], responses={404: {"description": "Not found"}})
# Define api input validator/format
class Input(BaseModel):
    key: Any

# key value retrieve function with api endpoint defination
@router_v1.get("/retrieve")
async def retrieve_value_endpoint(input: Input):
    try:
        key = input.key
        if key is None:
            out = 'Bad request'
            return JSONResponse(status_code=400, content=jsonable_encoder(out))
                # Dispatch the retrive task to Huey
        value = retrieve_value_from_redis(key)
     
    #    check key is present in redis or not
        if not redis_client.exists(key):
            return JSONResponse(status_code=404, content=jsonable_encoder("Key not found"))

        value = value.get(blocking=True, timeout=5)  # Timeout after 5 seconds
        
        out = {"key": key, "value": value}
        return JSONResponse(status_code=200, content=jsonable_encoder(out))
    except:
        out = 'Internal Server Error'
        return JSONResponse(status_code=500, content=jsonable_encoder(out))
