# instanciar o elemento da classe sections 
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> AsyncGenerator:  # Gunção que vai ter como retorno um generetor
    session: AsyncSession = Session()
    # cria um objeto novo a cada nova conexão
    try:
        # é um return "sem ser return" - ele devolve a sessão mas matpem a função viva
        yield session 
    finally:
        # Após utilizar a sessão com o banco, ai sim, finalizamos ela
        await session.close() 
