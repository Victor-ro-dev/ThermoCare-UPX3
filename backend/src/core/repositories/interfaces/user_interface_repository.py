
from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.entities.models import User

class UserInterface(ABC):
    @abstractmethod
    async def create(self, obj) -> User:
        pass

    @abstractmethod
    async def get_user_by_id(self, obj_id: str) -> Optional[object]:
        pass

    @abstractmethod
    async def get_by_email(self, obj_email: str) -> List[object]:
        pass

    @abstractmethod
    async def update(self, obj_id: int, obj_data: dict) -> Optional[object]:
        pass

    @abstractmethod
    async def delete(self, obj_id: int) -> None:
        pass