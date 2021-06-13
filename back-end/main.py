from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from routers.users import users


app = FastAPI(
    title="Soccer Project",
    description="This is a very fancy project, with auto docs for the API and everything⚽️",
)

# Customized the Httpexception(Response json format)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse((exc.detail), status_code=exc.status_code)


app.include_router(users.router)
