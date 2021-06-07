from fastapi import Request
from fastapi.responses import JSONResponse

import main

print(main)
print(main.app)


class CustomException(Exception):
    def __init__(self, success: bool, msg: str):
        self.success = success
        self.msg = msg


async def custom_exception(request: Request, exc=CustomException):
    print(request)
    return JSONResponse(
        status_code=400, content={"success": exc.success, "msg": exc.msg}
    )
