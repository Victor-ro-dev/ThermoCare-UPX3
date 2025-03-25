from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.models.schemas.bd_schema import UserSchema, UserLoginSchema, UserCreateSchema
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.services.user_service import UserService
from src.main.dependencies.auth_dependence import get_current_user
from src.models.repositories.user_repository import UserRepository
from src.controller.auth.cookie_manager import CookieManager
from src.controller.auth.token_manager import TokenManager



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
    credentials: UserLoginSchema,
    response: Response, 
    db: AsyncSession = Depends(db_connection_handler.get_db)
):
    try:
        user_service = UserService(UserRepository(db))
        user = await user_service.login_user(credentials, response)
        return user  # Passa o objeto credentials
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    
#----------------------------------------------------------------------------------------------------

@router.get("/auth/me", response_model=UserSchema)
async def read_user_me(
    request: Request,
    db: AsyncSession = Depends( db_connection_handler.get_db)
):
    # 1. Obter token do cookie
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token de acesso não fornecido")

    # 2. Verificar token
    try:
        token_data = TokenManager.verify_token(token)
        user_service = UserService(UserRepository(db))
        
        # 3. Buscar usuário pelo email (ou sub) do token
        user = await user_service.get_authenticated_user(token_data.sub)
        
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
            
        return user
        
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/auth/logout" , response_model=dict, status_code=status.HTTP_200_OK)
async def logout_user(response: Response):
    """Realiza logout removendo os cookies de autenticação"""
    try:
        CookieManager.delete_access_token_cookie(response)
        CookieManager.delete_refresh_token_cookie(response)
        
        # Headers adicionais para prevenir cache
        response.headers["Cache-Control"] = "no-store, max-age=0"
        response.headers["Pragma"] = "no-cache"
        print("Logout realizado com sucesso")
        
        return {"message": "Logout realizado com sucesso"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/users", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
async def read_users(
    db: AsyncSession = Depends(db_connection_handler.get_db),
    current_user: dict = Depends(get_current_user),  # Verifica o token
):
    """Obtém todos os usuários."""
    user_service = UserService(db)
    return await user_service.get_all_users()


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