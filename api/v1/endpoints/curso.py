import sys
default_path = "C:\\Users\\ct67ca\\Desktop\\Projeto - FastAPI"
sys.path.append(default_path)

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session
 
# Vou responder um CursoSchema e também receber um CursoSchema!
# API envia JSON e espera receber JSON
 
router = APIRouter()
 
#POST CURSOS
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo = curso.titulo,
                            aulas = curso.aulas,
                            horas = curso.horas,
                            instrutor = curso.instrutor)
   
    db.add(novo_curso)
    await db.commit()
    return novo_curso
 