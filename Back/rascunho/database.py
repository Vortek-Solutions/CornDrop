from sqlalchemy import create_engine, MetaData
from databases import Database

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)
