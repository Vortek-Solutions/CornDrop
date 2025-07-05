from fastapi import FastAPI
from src.shemas import Rotina

app = FastAPI()

rotinas = []

@app.post("/corndrop/rotinas/add")
def adicionar_rotina(rotina: Rotina):
    if rotinas:
        novo_id = max(r.id_rotina for r in rotinas) + 1
    else:
        novo_id = 0
    
    rotina.id_rotina = novo_id
    rotinas.append(rotina)
    return rotina

@app.get("/corndrop/rotinas/")
def listar_rotinas():
    return rotinas