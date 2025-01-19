from fastapi import APIRouter, HTTPException
from database import database
from models import users, items
from pydantic import BaseModel

router = APIRouter()

# --- MODELOS ---
class User(BaseModel):
    username: str
    email: str
    full_name: str = None

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# --- ROTAS DE USUÁRIOS ---
@router.get("/users/", tags=["Users"])
async def list_users():
    query = users.select()
    return await database.fetch_all(query)

@router.post("/users/", tags=["Users"])
async def create_user(user: User):
    query = users.insert().values(username=user.username, email=user.email, full_name=user.full_name)
    try:
        await database.execute(query)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# --- ROTAS DE ITENS ---
@router.get("/items/", tags=["Items"])
async def list_items():
    query = items.select()
    return await database.fetch_all(query)

@router.post("/items/", tags=["Items"])
async def create_item(item: Item):
    query = items.insert().values(name=item.name, description=item.description, price=item.price, tax=item.tax)
    try:
        await database.execute(query)
        return {"message": "Item created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/items/{item_id}", tags=["Items"])
async def get_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    item = await database.fetch_one(query)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
