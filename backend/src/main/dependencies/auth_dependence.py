from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.controller.auth.token_manager import TokenManager

# Define o esquema OAuth2 para autenticação via token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Obtém o usuário atual a partir do token JWT."""
    try:
        # Verifica e decodifica o token JWT usando o AuthService
        payload = TokenManager.verify_token(token)
        return payload 
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )