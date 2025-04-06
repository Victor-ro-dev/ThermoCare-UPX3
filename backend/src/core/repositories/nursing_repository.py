from src.core.entities.models import NursingHome
from src.core.schemas.bd_schema import NursingHomeSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from typing import List, Optional
from src.core.repositories.interfaces.nursing_interface_repository import NursingInterface

class NursingHomeRepository(NursingInterface):

    def __init__(self, db: AsyncSession) -> None:
        self.__db = db

    async def create(self, nursing_home: NursingHomeSchema) -> NursingHome:
        query = insert(NursingHome).values(
            name=nursing_home.name,
            cep=nursing_home.cep,
            logradouro=nursing_home.logradouro,
            numero=nursing_home.numero,
            bairro=nursing_home.bairro,
            cidade=nursing_home.cidade,
            estado=nursing_home.estado,
            complemento=nursing_home.complemento
        )
        await self.__db.execute(query)
        await self.__db.commit()
        
        # Retornar o objeto NursingHome criado
        return NursingHome(
            id=nursing_home.id,
            name=nursing_home.name,
            cep=nursing_home.cep,
            logradouro=nursing_home.logradouro,
            numero=nursing_home.numero,
            bairro=nursing_home.bairro,
            cidade=nursing_home.cidade,
            estado=nursing_home.estado,
            complemento=nursing_home.complemento
        )
    
    async def get_nursing_by_id(self, nursing_home_id: str) -> Optional[NursingHome]:
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