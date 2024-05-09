from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL) # criando uma função para injetar os dados no banco de dados

# sessionmaker - retorna uma classe para nós, com essas configurações
# ele que vai abrir a conexão com o nosso banco de dados

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

# Para o print funcionar tem que deixar a ultima importação assim - from configs import settings
# print(type(Session))

# Nessa pasta foi criado o "motorista" que vai buscar a carga