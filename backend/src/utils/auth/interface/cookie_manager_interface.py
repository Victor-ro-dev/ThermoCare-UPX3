from abc import ABC, abstractmethod
from fastapi import Response

class CookieManagerInterface(ABC):
    @abstractmethod
    def set_access_token_cookie(self, response: Response, token: str) -> None:
        """Configura o cookie do token de acesso."""
        pass

    @abstractmethod
    def set_refresh_token_cookie(self, response: Response, token: str) -> None:
        """Configura o cookie do token de refresh."""
        pass

    @abstractmethod
    def delete_access_token_cookie(self, response: Response) -> None:
        """Deleta o cookie do token de acesso."""
        pass

    @abstractmethod
    def delete_refresh_token_cookie(self, response: Response) -> None:
        """Deleta o cookie do token de refresh."""
        pass

    @abstractmethod
    def set_no_cache_headers(self, response: Response) -> None:
        """Configura os cabeçalhos para evitar cache."""
        pass