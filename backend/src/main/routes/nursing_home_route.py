from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.models.schemas.bd_schema import NursingHomeSchema
from src.models.repositories.nursinghome_repository import NursingHomeRepository
from src.models.settings.db_connection_handler import db_connection_handler


router = APIRouter()

