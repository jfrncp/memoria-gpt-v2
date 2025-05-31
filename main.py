from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/")
def root():
    return {"estado": "Servidor funcionando correctamente"}

@app.get("/openapi.json")
def openapi():
    with open("openapi.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)
