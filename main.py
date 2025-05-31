from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Servidor funcionando correctamente"}

@app.get("/openapi.json")
def openapi():
    with open("openapi.json", "r") as file:
        contenido = json.load(file)
    return JSONResponse(content=contenido)
