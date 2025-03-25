from src.models.entities.models import User
from src.models.schemas.bd_schema import UserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from typing import List, Optional
from src.models.repositories.interfaces.user_interface_repository import UserInterface

class UserRepository(UserInterface):
    
        def __init__(self, db: AsyncSession) -> None:
            self.__db = db
    
        async def create(self, user: UserSchema) -> User:
            query = insert(User).values(
                username=user.username,
                email=user.email,
                password_hash=user.password_hash
            )
            await self.__db.execute(query)
            await self.__db.commit()
            
            # Retornar o objeto User criado
            return User(
                id=user.id,  # O ID será gerado automaticamente pelo banco de dados
                username=user.username,
                email=user.email,
                password_hash=user.password_hash
            )
    
        async def get_user_by_id(self, user_id: str) -> Optional[User]:
            query = select(User).where(User.id == user_id)
            result = await self.__db.execute(query)
            return result.scalar_one_or_none()
        
        async def get_by_email(self, email: str) -> Optional[User]:
            query = select(User).where(User.email == email)
            result = await self.__db.execute(query)
            return result.scalar_one_or_none()
        
        async def update(self, user_id: str, user_data: dict) -> Optional[User]:
            query = select(User).where(User.id == user_id)
            result = await self.__db.execute
            user = result.scalar_one_or_none()
            if not user:
                return None
            
            # Atualizar os campos permitidos
            for field, value in user_data.items():
                setattr(user, field, value)

            await self.__db.commit()
            return user
        
        async def delete(self, user_id: str) -> None:
            query = select(User).where(User.id == user_id)
            result = await self.__db.execute(query)
            user = result.scalar_one_or_none()
            if not user:
                return None
            
            await self.__db.delete(user)
            await self.__db.commit()