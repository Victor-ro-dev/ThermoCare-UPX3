from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.schemas.bd_schema import UserSchema, UserLoginSchema, UserCreateSchema, ProfileSchema
from src.core.settings.db_connection_handler import db_connection_handler 
from src.services.user_service import UserService
from src.services.dependencies.auth_dependence import get_current_user
from src.core.repositories.user_repository import UserRepository
from src.services.auth_service import AuthService



router = APIRouter()

@router.post("/register", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateSchema, response: Response, db: AsyncSession = Depends(db_connection_handler.get_db)):
    """Cria um novo usuário."""
    try:
        user_service = UserService(UserRepository(db))
        new_user = await user_service.create_user(user, response)
        
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
#----------------------------------------------------------------------------------------------------

    
@router.post("/login", response_model=dict, status_code=status.HTTP_200_OK)
async def login_user(
    credentials: UserLoginSchema, response: Response, db: AsyncSession = Depends(db_connection_handler.get_db)
):
    try:
        user_service = UserService(UserRepository(db))
        user_validate = await user_service.login_user(credentials, response)
        return user_validate  # Passa o objeto credentials
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    
#----------------------------------------------------------------------------------------------------

@router.get("/auth/me", response_model=UserSchema)
async def read_user_me(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(db_connection_handler.get_db)
):
    """Obtém o usuário autenticado pelo access token ou renova o token usando o refresh token."""
    try:
        return await AuthService.get_authenticated_user(request, response, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")


@router.post("/auth/logout" , response_model=dict, status_code=status.HTTP_200_OK)
async def logout_user(response: Response):
    """Realiza logout removendo os cookies de autenticação"""
    try:
        # Remove os cookies de autenticação
        AuthService.remove_cookies(response)
        print("Logout realizado com sucesso")
        
        return {"message": "Logout realizado com sucesso"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/user", response_model=ProfileSchema, status_code=status.HTTP_200_OK)
async def read_user(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(db_connection_handler.get_db),
):
    get_user = await AuthService.get_authenticated_user(request, response, db)
    email = get_user.email
    try:
        user_service = UserService(UserRepository(db))
        user = await user_service.get_user_by_email(email)
        # Converta para ProfileSchema explicitamente
        return ProfileSchema.model_validate(user)
    except HTTPException as e:
        raise e
    


@router.put("/users/{user_id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def update_user(
    user_id: int,
    user_data: dict,
    db: AsyncSession = Depends(db_connection_handler.get_db),
    current_user: dict = Depends(get_current_user),
):
    """Atualiza os dados de um usuário."""
    user_service = UserService(db)
    return await user_service.update_user(user_id, user_data)

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(db_connection_handler.get_db),
    current_user: dict = Depends(get_current_user),
):
    """Exclui um usuário."""
    user_service = UserService(db)
    await user_service.delete_user(user_id)