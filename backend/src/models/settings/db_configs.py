from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./upx_schema.db"

# Criação do engine do SQLAlchemy
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criação da fábrica de sessões
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

class Base(DeclarativeBase):
    """Classe base para as classes do SQLAlchemy."""
    pass