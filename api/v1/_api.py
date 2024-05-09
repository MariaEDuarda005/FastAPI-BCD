import sys
default_path = "C:\\Users\\ct67ca\\Desktop\\Projeto - FastAPI"
sys.path.append(default_path)

from fastapi import APIRouter
from api.v1.endpoints import curso

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=["cursos"])
# /api/v1/cursos -  esse será o endpoint completo junto as prefixo 