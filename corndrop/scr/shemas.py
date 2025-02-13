from pydantic import BaseModel
from typing import Optional

class Rotina(BaseModel):
    id_rotina: int = 0
    dispositivo: Optional[str] = None
    insumo:str
    nome_rotina:str
    quantidade:int
    horario: Optional[str] = None
    intervalo: Optional[int] = None
