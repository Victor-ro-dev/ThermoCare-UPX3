import secrets
from pydantic import field_validator
from pydantic_settings import BaseSettings

class AuthConfig(BaseSettings):
    """
    Configurações de autenticação e segurança.
    """
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 1440
    PASSWORD_HASH_ALGORITHM: str = "bcrypt"

    @field_validator('SECRET_KEY')
    def validate_secret_key(cls, v):
        """Valida se a SECRET_KEY tem comprimento suficiente."""
        if len(v) < 32:
            raise ValueError("SECRET_KEY deve ter pelo menos 32 caracteres")
        return v

    @field_validator('ACCESS_TOKEN_EXPIRE_MINUTES', 'REFRESH_TOKEN_EXPIRE_MINUTES')
    def validate_expiration_times(cls, v):
        """Valida se os tempos de expiração são positivos."""
        if v <= 0:
            raise ValueError("Tempos de expiração devem ser positivos")
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignora variáveis de ambiente não definidas na classe

# Instância da configuração de autenticação
auth_config = AuthConfig()