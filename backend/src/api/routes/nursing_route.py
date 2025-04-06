from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.schemas.bd_schema import NursingHomeSchema
from src.core.repositories.nursing_repository import NursingHomeRepository
from src.core.repositories.user_repository import UserRepository
from src.core.settings.db_connection_handler import db_connection_handler
from src.services.nursing_service import NursingService
from src.services.user_service import UserService
from src.services.dependencies.auth_dependence import get_current_user



router = APIRouter()

@router.post("/users/me/nursing-homes", response_model=NursingHomeSchema)
async def create_nursing(
    nursing: NursingHomeSchema,
    db: AsyncSession = Depends(db_connection_handler.get_db),
    current_user: dict = Depends(get_current_user),  # Obtém o usuário autenticado
):
    """Cria um novo asilo vinculado ao usuário autenticado."""
    try:
        # Verificar se o usuário já possui um asilo
        user_service = UserService(UserRepository(db))
        user = await user_service.get_user_by_email(current_user.sub)
        if user.nursing_home_id:
            raise HTTPException(status_code=400, detail="Usuário já possui um asilo associado.")

        # Criar o asilo e associá-lo ao usuário
        nursing_service = NursingService(NursingHomeRepository(db))
        new_nursing = await nursing_service.create_nursing(nursing)
        user.nursing_home_id = new_nursing.id
        await db.commit()
        return new_nursing
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#----------------------------------------------------------------------------------------------------

@router.get("/nursing/{nursing_id}", response_model=NursingHomeSchema)
async def get_nursing_by_id(nursing_id: str, db: AsyncSession = Depends(db_connection_handler.get_db)):
    """Busca um asilo pelo ID."""
    try:
        nursing_service = NursingService(NursingHomeRepository(db))
        nursing = await nursing_service.get_nursing_by_id(nursing_id)
        
        return nursing
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))