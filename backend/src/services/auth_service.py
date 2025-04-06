from fastapi import HTTPException, Response, Request, status
from src.core.schemas.bd_schema import UserSchema, UserLoginSchema, UserCreateSchema
from src.utils.auth.hash_manager import HashManager
from src.utils.auth.token_manager import TokenManager
from src.utils.auth.cookie_manager import CookieManager
from src.utils.validators.password_validator import PasswordValidator
from src.utils.validators.username_validator import UsernameValidator
from src.utils.validators.email_validator import EmailValidator
from src.core.repositories.user_repository import UserInterface, UserRepository
from src.services.interfaces.auth_service_interface import AuthServiceInterface
from sqlalchemy.ext.asyncio import AsyncSession

class AuthService(AuthServiceInterface):
    """Serviço para centralizar a lógica de autenticação."""

    @staticmethod
    async def get_authenticated_user(
        request: Request,
        response: Response,
        db: AsyncSession
    ) -> UserSchema:
        """Obtém o usuário autenticado pelo access token ou renova o token usando o refresh token."""
        # 1. Obter tokens do cookie
        access_token = request.cookies.get("access_token")
        refresh_token = request.cookies.get("refresh_token")

        if not access_token and not refresh_token:
            raise HTTPException(status_code=401, detail="Nenhum token fornecido")

        user_repository = UserRepository(db)

        # 2. Se apenas o refresh token existir
        if not access_token and refresh_token:
            try:
                # Validar o refresh token
                refresh_token_data = TokenManager.verify_token(refresh_token)
                email = refresh_token_data.sub
                if not email:
                    raise HTTPException(status_code=401, detail="Refresh token inválido")

                # Gerar um novo access token
                new_access_token = TokenManager.create_access_token({"sub": email})
                CookieManager.set_access_token_cookie(response, new_access_token)

                # Buscar o usuário pelo e-mail
                user = await user_repository.get_by_email(email)
                if not user:
                    raise HTTPException(status_code=404, detail="Usuário não encontrado")

                return UserSchema.model_validate(user)

            except Exception as refresh_error:
                raise HTTPException(status_code=401, detail=f"Erro ao validar o refresh token: {str(refresh_error)}")

        # 3. Se ambos os tokens existirem, validar apenas o access token
        if access_token:
            try:
                token_data = TokenManager.verify_token(access_token)
                email = token_data.sub
                if not email:
                    raise HTTPException(status_code=401, detail="Token de acesso inválido")

                # Buscar o usuário pelo e-mail
                user = await user_repository.get_by_email(email)
                if not user:
                    raise HTTPException(status_code=404, detail="Usuário não encontrado")

                return UserSchema.model_validate(user)

            except Exception as access_error:
                raise HTTPException(status_code=401, detail=f"Erro ao validar o access token: {str(access_error)}")

        raise HTTPException(status_code=500, detail="Erro inesperado na autenticação")
        
    @staticmethod
    def authenticator(token_data: dict, response: Response) -> None:
        """Cria os tokens de acesso e refresh"""
        print(f"Token Data: {token_data} and Response: {response}")
        access_token = TokenManager.create_access_token(data=token_data)
        refresh_token = TokenManager.create_refresh_token(data=token_data)
        CookieManager.set_access_token_cookie(response, access_token)
        CookieManager.set_refresh_token_cookie(response, refresh_token)

    @staticmethod
    def remove_cookies(response: Response) -> None:
        """Remove os cookies de autenticação."""
        CookieManager.delete_access_token_cookie(response)
        CookieManager.delete_refresh_token_cookie(response)
        CookieManager.set_no_cache_headers(response)

