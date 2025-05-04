from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.schemas.bd_schema import NursingHomeSchema, NursingProfileSchema
from src.core.repositories.nursing_repository import NursingHomeRepository
from src.core.repositories.user_repository import UserRepository
from src.core.settings.db_connection_handler import db_connection_handler
from src.services.nursing_service import NursingService
from src.services.user_service import UserService
from src.utils.auth.cookie_manager import CookieManager
from src.utils.auth.token_manager import TokenManager
from src.services.auth_service import AuthService



router = APIRouter()

@router.post("/users/me/nursing-homes", response_model=NursingHomeSchema)
async def create_nursing(
    nursing: NursingHomeSchema,
    request: Request,
    db: AsyncSession = Depends(db_connection_handler.get_db),
):
    print(nursing)
    """Cria um novo asilo vinculado ao usuário autenticado."""
    access_token = request.cookies.get("access_token")
    print(access_token)
    if not access_token:
        raise HTTPException(status_code=401, detail="Token de acesso não fornecido.")
    

    try:
        # Verificar se o usuário já possui um asilo
        user_email = TokenManager.verify_token(access_token)
        user_service = UserService(UserRepository(db))
        user = await user_service.get_user_by_email(user_email.sub)
        print(user.email)
        if user.nursing_home_id:
            raise HTTPException(status_code=400, detail="Usuário já possui um asilo vinculado.")
        # Criar o asilo e associá-lo ao usuário
        nursing_service = NursingService(NursingHomeRepository(db))
        new_nursing = await nursing_service.create_nursing(nursing)
        print(new_nursing.id)
        user.nursing_home_id = new_nursing.id
        await db.commit()
        return new_nursing
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#----------------------------------------------------------------------------------------------------

@router.get("/nursing-home", response_model=NursingProfileSchema) 
async def get_nursing_by_user(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(db_connection_handler.get_db),
):
    """Obtém o asilo vinculado ao usuário autenticado."""
    get_user = await AuthService.get_authenticated_user(request, response, db)
    nursing_home_id = get_user.nursing_home_id
    try:
        nursing_service = NursingService(NursingHomeRepository(db))
        nursing = await nursing_service.get_nursing_by_id(nursing_home_id)
        return NursingProfileSchema.model_validate(nursing)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))