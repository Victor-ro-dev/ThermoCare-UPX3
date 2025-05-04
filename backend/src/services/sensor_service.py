from src.core.schemas.bd_schema import SensorTempSchema
from src.services.interfaces.sensor_service_interface import SensorServiceInterface
from src.core.repositories.interfaces.sensor_interface import SensorInterface
from typing import List


class SensorService(SensorServiceInterface):
    def __init__(self, sensor_repository: SensorInterface) -> None:
        self.repository = sensor_repository

    async def add_sensor(self, sensor: SensorTempSchema, nursing_id: int) -> SensorTempSchema:
        """Cria um novo sensor."""
        # Criar o objeto Pydantic
        sensor_data = SensorTempSchema(
            name=sensor.name,
            location=sensor.location,
            nursing_home_id=nursing_id,
            status="Ativo",  # Assuming default status is "Ativo"
            phone=sensor.phone
        )

        # Criar o sensor no banco de dados
        new_sensor = await self.repository.add_sensor(sensor_data)

        return new_sensor
    
    async def get_all_sensor_by_nursing_id(self, nursing_id: int) -> List[SensorTempSchema]:
        """Retorna todos os sensores de um lar de idosos."""
        sensors = await self.repository.get_all_sensors_by_nursing_home(nursing_id)
        return sensors