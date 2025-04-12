from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.entities.models import NursingHome

class NursingInterface(ABC):
    @abstractmethod
    async def create(self, obj) -> NursingHome:
        pass

    @abstractmethod
    async def get_nursing_by_id(self, obj_id: str) -> Optional[object]:
        pass

    @abstractmethod
    async def get_by_name(self, obj_name: str) -> Optional[object]:
        pass
