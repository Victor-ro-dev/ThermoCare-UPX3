from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.schemas.bd_schema import SensorTempSchema
from src.core.repositories.sensor_temp_repository import SensorTempRepository
from src.core.settings.db_connection_handler import db_connection_handler

router = APIRouter()



# Adicione outras rotas conforme necessário, como update e delete