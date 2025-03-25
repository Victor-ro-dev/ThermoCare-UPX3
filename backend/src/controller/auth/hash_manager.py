from passlib.context import CryptContext
from src.models.settings.auth_configs import auth_config

# Configuração do Passlib com o algoritmo definido no AuthConfig
pwd_context = CryptContext(schemes=[auth_config.PASSWORD_HASH_ALGORITHM], deprecated="auto")

class HashManager:
    """Serviço para hashing e verificação de senhas."""

    @staticmethod
    def hash_password(password: str) -> str:
        """Gera um hash da senha usando o algoritmo configurado."""
        if not password:
            raise ValueError("A senha não pode ser vazia ou nula")
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verifica se a senha plain corresponde ao hash."""

        if not plain_password or not hashed_password:
            raise ValueError("A senha e o hash não podem ser vazios ou nulos")
        return pwd_context.verify(plain_password, hashed_password)

# Instância do serviço de hashing
hash_manager = HashManager()