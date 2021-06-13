from fastapi.encoders import jsonable_encoder
from typing import Optional


def reponses(success: bool, msg: Optional[str] = None, data=None):
    if success == False:
        return {"success": success, "msg": msg}

    if data != None:
        if type(data) != dict:
            data = jsonable_encoder(data)
        return {"success": success, "data": data}
