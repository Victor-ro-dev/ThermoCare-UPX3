from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.schemas.bd_schema import SensorTempSchema, SensorWithLastDataSchema, LastSensorDataSchema
from src.core.entities.models import SensorData
from src.services.sensor_service import SensorService
from src.services.auth_service import AuthService
from src.core.repositories.sensor_temp_repository import SensorTempRepository
from src.core.settings.db_connection_handler import db_connection_handler
from sqlalchemy.future import select

router = APIRouter()



# Adicione outras rotas conforme necessário, como update e delete


@router.post("/sensor", response_model=SensorTempSchema)
async def create_sensor(
    new_sensor: SensorTempSchema,
    request: Request,
    response: Response,
    db: AsyncSession = Depends(db_connection_handler.get_db),
):
    print(new_sensor)
    get_user = await AuthService.get_authenticated_user(request,response, db)
    nursing_home_id = get_user.nursing_home_id
    try:
        sensor_service = SensorService(SensorTempRepository(db))
        added_sensor = await sensor_service.add_sensor(new_sensor,nursing_home_id)
        return added_sensor
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))    
    
@router.get("/sensor", response_model=List[SensorWithLastDataSchema])
async def get_all_sensors_by_nursing_id(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(db_connection_handler.get_db),
):
    print("Iniciando rota GET /sensor")
    get_user = await AuthService.get_authenticated_user(request, response, db)
    print(f"Usuário autenticado: {get_user}")
    nursing_home_id = get_user.nursing_home_id
    print(f"nursing_home_id: {nursing_home_id}")
    try:
        sensor_service = SensorService(SensorTempRepository(db))
        sensors = await sensor_service.get_all_sensor_by_nursing_id(nursing_home_id)
        print(f"Sensores encontrados: {sensors}")

        result = []
        for sensor in sensors:
            print(f"Processando sensor: {sensor.id} - {sensor.name}")
            # Busca o último dado do sensor
            last_data_query = (
                select(SensorData)
                .where(SensorData.sensor_id == sensor.id)
                .order_by(SensorData.created_at.desc())
                .limit(1)
            )
            last_data_result = await db.execute(last_data_query)
            last_data = last_data_result.scalar_one_or_none()
            print(f"Último dado do sensor {sensor.id}: {last_data}")

            result.append(
                SensorWithLastDataSchema(
                    id=sensor.id,
                    name=sensor.name,
                    location=sensor.location,
                    status=sensor.status,
                    phone=sensor.phone,
                    last_data=LastSensorDataSchema.model_validate(last_data) if last_data else None
                )
            )
        print(f"Resultado final enviado para o frontend: {result}")
        return result

    except ValueError as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=400, detail=str(e))