from abc import ABC, abstractmethod

class HashManagerInterface(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        """Gera um hash da senha."""
        pass

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verifica se a senha corresponde ao hash."""
        pass