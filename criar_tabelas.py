from core.configs import settings
from core.database import engine

async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas do DB')
    # criar um bloco de contexto assincrono
    async with engine.begin() as conn:
        # trecho assincrono, enquanto ele estiver aberto ela não vai dar sequencia no resto 
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all) # excluir, caso ja exista (Alterações)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso...")

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())