from abc import ABC, abstractmethod
from fastapi import Response
from src.core.schemas.bd_schema import UserSchema, UserLoginSchema, UserCreateSchema
from typing import List

class UserServiceInterface(ABC):
    @abstractmethod
    async def create_user(self, user: UserCreateSchema, response: Response) -> UserSchema:
        """Cria um novo usuário."""
        pass

    @abstractmethod
    async def login_user(self, credentials: UserLoginSchema, response: Response) -> dict:
        """Autentica um usuário e gera tokens de acesso e refresh."""
        pass

    @abstractmethod
    async def update_user(self, user_id: int, user_data: dict) -> UserSchema:
        """Atualiza os dados de um usuário."""
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        """Exclui um usuário."""
        pass

    @abstractmethod
    async def get_user_by_email(self, user_email: str) -> UserSchema:
        """Busca um usuário pelo e-mail."""
        pass
