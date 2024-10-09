from fastapi import FastAPI
from api.config.database import *
from api.models.products import *
from api.routes.products import router as products_router 


app = FastAPI()
# para iniciar el servidor uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Servidor con FastAPI"}

# Incluir el router de products
app.include_router(products_router)