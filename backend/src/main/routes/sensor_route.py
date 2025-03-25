from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.models.schemas.bd_schema import SensorTempSchema
from src.models.repositories.sensor_temp_repository import SensorTempRepository
from src.models.settings.db_connection_handler import db_connection_handler

router = APIRouter()



# Adicione outras rotas conforme necessário, como update e delete