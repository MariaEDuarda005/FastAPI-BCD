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
    # não é preciso colocar o id por que ele já é gerado pelo banco 
   
    db.add(novo_curso) # adiciona no banco de dados 
    await db.commit()
    return novo_curso

#GET CURSOS
# response_model compara com o cursoShema, faz a documentação e valida os dados 
@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)): # conexão assincrona para trazer com o banco
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos

# GET CURSOS INDIVIDUAIS
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso:
            return curso
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"))
        
# PUT CURSOS para atualizar        
@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        if curso_up:
            # atualizr pelo o que enviou no json 
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas
            curso_up.instrutor = curso.instrutor
            await session.commit()
            return curso_up
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"))

# DELETE CURSO        
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()
        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado..."))