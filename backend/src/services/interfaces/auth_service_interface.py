from abc import ABC, abstractmethod

class AuthServiceInterface(ABC):
    @abstractmethod
    async def get_authenticated_user(self, request, response, db) -> dict:
        """Obtém o usuário autenticado pelo access token ou renova o token usando o refresh token."""
        pass

    @abstractmethod
    def authenticator(self, token_data: dict, response) -> None:
        """Gera os cookies de autenticação."""
        pass

    @abstractmethod
    def remove_cookies(self, response) -> None:
        """Remove os cookies de autenticação."""
        pass