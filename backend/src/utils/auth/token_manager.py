from jose import JWTError, jwt
from datetime import datetime, timedelta
from pytz import timezone
from ...core.schemas.auth_schema import TokenData
from src.core.settings.auth_configs import auth_config
from src.utils.auth.interface.token_manager_interface import TokenManagerInterface

class TokenManager(TokenManagerInterface):
    """Serviço para gerenciamento de tokens JWT."""

    # Definir o fuso horário do Brasil
    BR_TZ = timezone("America/Sao_Paulo")

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        """Cria um token de acesso JWT."""
        to_encode = data.copy()

        # Usar o horário do Brasil
        expire = datetime.now(TokenManager.BR_TZ) + (expires_delta or timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES))

        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, auth_config.SECRET_KEY, algorithm=auth_config.ALGORITHM)

    @staticmethod
    def create_refresh_token(data: dict) -> str:
        """Cria um token de atualização JWT."""
        to_encode = data.copy()

        # Usar o horário do Brasil
        expire = datetime.now(TokenManager.BR_TZ) + timedelta(minutes=auth_config.REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, auth_config.SECRET_KEY, algorithm=auth_config.ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> TokenData:
        """Verifica e decodifica um token JWT."""
        try:
            payload = jwt.decode(
                token,
                auth_config.SECRET_KEY,
                algorithms=[auth_config.ALGORITHM],
                options={"verify_exp": True}
            )

            email = payload.get("sub") or payload.get("email")
            if not email:
                raise ValueError("Token não contém identificador do usuário (sub/email)")

            return TokenData(
                sub=email,
                exp=payload.get("exp"),
            )

        except JWTError as e:
            print(f"Erro ao verificar token: {e}")
            raise ValueError("Token inválido")




