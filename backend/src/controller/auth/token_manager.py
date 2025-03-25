from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from ...models.schemas.auth_schema import TokenData
from src.models.settings.auth_configs import auth_config

class TokenManager:
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        """Cria um token de acesso JWT."""
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES))

        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, auth_config.SECRET_KEY, algorithm=auth_config.ALGORITHM)
    
    @staticmethod
    def create_refresh_token(data: dict) -> str:
        """Cria um token de atualização JWT."""
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(minutes=auth_config.REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, auth_config.SECRET_KEY, algorithm=auth_config.ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> TokenData:
        """Verifica e decodifica um token JWT."""
        try:
            # 1. Decodifica o token
            payload = jwt.decode(
                token,
                auth_config.SECRET_KEY,
                algorithms=[auth_config.ALGORITHM],
                options={"verify_exp": True}
            )
            
            # 2. Extrai o email corretamente (usando 'sub' ou 'email' conforme seu JWT)
            email = payload.get("sub") or payload.get("email")
            if not email:
                raise ValueError("Token não contém identificador do usuário (sub/email)")
            
            # 3. Retorna os dados do token no formato correto
            return TokenData(
                sub=email,
                # Adicione outros campos que seu TokenData espera
                exp=payload.get("exp"),
                # ... outros campos necessários
            )
            
        except JWTError as e:
            raise ValueError("Token inválido")

                


        