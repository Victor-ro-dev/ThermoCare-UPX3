from fastapi import Response
from src.models.settings.auth_configs import auth_config

class CookieManager:
    @staticmethod
    def set_access_token_cookie(response: Response, token: str):
        """Configura o cookie do token de acesso."""
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            path="/"
        )

    @staticmethod
    def set_refresh_token_cookie(response: Response, token: str):
        """Configura o cookie do token de refresh."""
        response.set_cookie(
            key="refresh_token",
            value=token,
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=auth_config.REFRESH_TOKEN_EXPIRE_MINUTES * 60,
            path="/"
        )

    @staticmethod
    def delete_access_token_cookie(response: Response):
        """Deleta o cookie do token de acesso."""
        response.delete_cookie(
            key="access_token",
            path="/"
        )
    
    @staticmethod
    def delete_refresh_token_cookie(response: Response):
        """Deleta o cookie do token de refresh."""
        response.delete_cookie(
            key="refresh_token",
            path="/"
        )
