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

    @abstractmethod
    async def get_all_nursing_homes(self) -> List[NursingHomeSchema]:
        """Obtém todos os asilos."""
        pass

    @abstractmethod
    async def update_nursing(self, nursing_id: int, nursing_data: dict) -> NursingHomeSchema:
        """Atualiza os dados de um asilo."""
        pass

    @abstractmethod
    async def delete_nursing(self, nursing_id: int) -> None:
        """Exclui um asilo."""
        pass