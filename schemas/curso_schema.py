from typing import Optional
from pydantic import BaseModel as SchemaBaseModel # faz a validação dos dados 
# como o sql Alchemy tem o basemodel dele, não podemos confundir 

# Validação de dados, tipa e coloca par fazer a validação, e não inserir os dados errados
class CursoSchema(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    instrutor: str

    class Config:
        # orm_mode = True
        from_atributes = True