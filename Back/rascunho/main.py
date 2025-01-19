from fastapi import FastAPI
from database import database, engine, metadata
from routers import router

# Cria as tabelas no banco
metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI()

# Inclui o router único
app.include_router(router)

# Eventos do banco de dados
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "FastAPI"}


# uvicorn main:app --reload iniciar

