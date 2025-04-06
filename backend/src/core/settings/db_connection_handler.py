from src.core.settings.db_configs import Base, engine, SessionLocal
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError

class DBConnectionHandler:
    """Classe para gerenciar a conexão com o banco de dados."""

    def __init__(self) -> None:
        """Inicializa o manipulador de conexão com o banco de dados."""
        self.__engine = engine
        self.__base = Base

    async def create_db(self) -> None:
        """Cria as tabelas no banco de dados se elas não existirem."""
        try:
            async with self.__engine.begin() as conn:
                inspector = inspect(conn)
                if not inspector.get_table_names():
                    await conn.run_sync(self.__base.metadata.create_all)
        except Exception as e:
            print(f"Erro ao criar o banco de dados: {e}")

    async def get_db(self):
        """Obtém uma sessão do banco de dados."""
        async with SessionLocal() as session:
            try:
                yield session
            except SQLAlchemyError as e:
                print(f"Erro durante a operação no banco de dados: {e}")
                raise
            finally:
                await session.close()


db_connection_handler = DBConnectionHandler()