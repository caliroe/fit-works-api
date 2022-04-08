from fastapi import FastAPI
from api.v1.api_router import api_router


app = FastAPI()


@app.get("/")
async def heathcheck():
    return {"message": "It's working."}


app.include_router(api_router, prefix='/api/v1')
