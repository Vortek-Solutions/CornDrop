from fastapi import FastAPI
from models import Rotina

app = FastAPI()

rotinas = []

@app.post("/rotinas/add")
def adicionar_rotina(rotina: Rotina):
    rotinas.append(rotina)
    return rotina

@app.get("/rotinas/")
def listar_rotinas():
    return rotinas