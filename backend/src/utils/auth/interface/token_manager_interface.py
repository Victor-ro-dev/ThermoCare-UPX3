from abc import ABC, abstractmethod
from datetime import timedelta
from src.core.schemas.auth_schema import TokenData

class TokenManagerInterface(ABC):
    @abstractmethod
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        """Cria um token de acesso JWT."""
        pass

    @abstractmethod
    def create_refresh_token(self, data: dict) -> str:
        """Cria um token de atualização JWT."""
        pass

    @abstractmethod
    def verify_token(self, token: str) -> TokenData:
        """Verifica e decodifica um token JWT."""
        pass