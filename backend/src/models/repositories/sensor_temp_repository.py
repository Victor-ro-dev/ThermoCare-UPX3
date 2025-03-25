from src.models.entities.models import SensorTemp
from src.models.schemas.bd_schema import SensorTempSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from typing import List, Optional

class SensorTempRepository:

    def __init__(self, db: AsyncSession) -> None:
        self.__db = db

    async def create(self, sensor: SensorTempSchema) -> SensorTemp:
        query = insert(SensorTemp).values(
            name=sensor.name,
            location=sensor.location,
            nursing_home_id=sensor.nursing_home_id
        )
        await self.__db.execute(query)
        await self.__db.commit()
        
        # Retornar o objeto SensorTemp criado
        return SensorTemp(
            id=sensor.id,  # O ID será gerado automaticamente pelo banco de dados
            name=sensor.name,
            location=sensor.location,
            nursing_home_id=sensor.nursing_home_id
        )
    
    async def read(self, sensor_id: str) -> Optional[SensorTemp]:
        query = select(SensorTemp).where(SensorTemp.id == sensor_id)
        result = await self.__db.execute(query)
        return result.scalar_one_or_none()
    
    async def get_all(self) -> List[SensorTemp]:
        query = select(SensorTemp)
        result = await self.__db.execute(query)
        return result.scalars().all()
    
    async def get_by_name(self, name: str) -> Optional[SensorTemp]:
        query = select(SensorTemp).where(SensorTemp.name == name)
        result = await self.__db.execute(query)
        return result.scalar_one_or_none()
