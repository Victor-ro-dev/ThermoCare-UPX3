from src.core.schemas.bd_schema import NursingHomeSchema
from src.core.repositories.interfaces.nursing_interface_repository import NursingInterface
from typing import List
from src.services.interfaces.nursing_service_interface import NursingServiceInterface


class NursingService(NursingServiceInterface):
    def __init__(self, nursing_repository: NursingInterface) -> None:
        self.repository = nursing_repository

    async def create_nursing(self, nursing: NursingHomeSchema) -> NursingHomeSchema:
        """Cria um novo asilo"""
        existing_nursing = await self.repository.get_by_name(nursing.name)
        if existing_nursing:
            raise ValueError("Asilo já cadastrado")
        # Criar o objeto Pydantic
        nursing_data = NursingHomeSchema(
            name=nursing.name,
            cep=nursing.cep,
            logradouro=nursing.logradouro,
            numero=nursing.numero,
            bairro=nursing.bairro,
            cidade=nursing.cidade,
            estado=nursing.estado,
            complemento=nursing.complemento
        )

        # Criar o asilo no banco de dados
        new_nursing = await self.repository.create(nursing_data)

        return new_nursing

    async def get_nursing_by_id(self, nursing_id: str) -> NursingHomeSchema:
        """Busca um asilo pelo ID"""

        nursing = await self.repository.get_nursing_by_id(nursing_id)

        return nursing

    async def get_all_nursing(self) -> List[NursingHomeSchema]:
        """Busca todos os asilos"""

        nursing = await self.repository.get_all()

        return nursing

    async def get_nursing_by_name(self, name: str) -> NursingHomeSchema:
        """Busca um asilo pelo nome"""

        nursing = await self.repository.get_by_name(name)

        return nursing