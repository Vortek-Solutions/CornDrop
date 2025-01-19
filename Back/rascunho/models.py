from sqlalchemy import Table, Column, Integer, String, Float
from database import metadata

# criar tabelas
users = Table("users",metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("full_name", String),
)

items = Table("items",metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String),
    Column("price", Float, nullable=False),
    Column("tax", Float, nullable=True),
)
