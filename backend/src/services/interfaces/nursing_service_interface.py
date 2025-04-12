from abc import ABC, abstractmethod
from src.core.schemas.bd_schema import NursingHomeSchema
from typing import List

class NursingServiceInterface(ABC):
    @abstractmethod
    async def create_nursing(self, nursing: NursingHomeSchema) -> NursingHomeSchema:
        """Cria um novo asilo."""
        pass

    @abstractmethod
    async def get_nursing_by_id(self, nursing_id: str) -> NursingHomeSchema:
        """Busca um asilo pelo ID."""
        pass
