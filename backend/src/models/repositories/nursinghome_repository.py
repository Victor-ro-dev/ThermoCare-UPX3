from src.models.entities.models import NursingHome
from src.models.schemas.bd_schema import NursingHomeSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from typing import List, Optional

class NursingHomeRepository:

    def __init__(self, db: AsyncSession) -> None:
        self.__db = db

    async def create(self, nursing_home: NursingHomeSchema) -> NursingHome:
        query = insert(NursingHome).values(
            name=nursing_home.name,
            address=nursing_home.address
        )
        await self.__db.execute(query)
        await self.__db.commit()
        
        # Retornar o objeto NursingHome criado
        return NursingHome(
            id=nursing_home.id,  # O ID será gerado automaticamente pelo banco de dados
            name=nursing_home.name,
            address=nursing_home.address
        )
    
    async def read(self, nursing_home_id: str) -> Optional[NursingHome]:
        query = select(NursingHome).where(NursingHome.id == nursing_home_id)
        result = await self.__db.execute(query)
        return result.scalar_one_or_none()
    
    async def get_all(self) -> List[NursingHome]:
        query = select(NursingHome)
        result = await self.__db.execute(query)
        return result.scalars().all()
    
    async def get_by_name(self, name: str) -> Optional[NursingHome]:
        query = select(NursingHome).where(NursingHome.name == name)
        result = await self.__db.execute(query)
        return result.scalar_one_or_none()