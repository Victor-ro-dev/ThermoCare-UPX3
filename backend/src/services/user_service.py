from fastapi import Response
from src.core.schemas.bd_schema import UserSchema, UserLoginSchema, UserCreateSchema
from src.utils.auth.hash_manager import HashManager
from src.utils.auth.token_manager import TokenManager
from src.utils.auth.cookie_manager import CookieManager
from src.utils.validators.password_validator import PasswordValidator
from src.utils.validators.username_validator import UsernameValidator
from src.utils.validators.email_validator import EmailValidator
from src.core.repositories.user_repository import UserInterface
from src.services.interfaces.user_service_interface import UserServiceInterface
from src.services.auth_service import AuthService


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserInterface) -> None:
        self.repository = user_repository

    async def create_user(self, user: UserCreateSchema, response: Response) -> UserSchema:
        """Cria um novo usuário"""

        # Verificar se o e-mail já está cadastrado
        existing_user = await self.repository.get_by_email(user.email)
        if existing_user:
            raise ValueError("E-mail já cadastrado")
        
        # Validar o e-mail
        validate_email = EmailValidator.validate_email(user.email)
        
        # Validar o username
        UsernameValidator.validate_username(user.username)

        # Validar a senha
        PasswordValidator.validate_password(user.password, user.password_confirmation)

        # Gerar o hash da senha
        password_hash = HashManager.hash_password(user.password)

        # Criar o objeto Pydantic
        user_data = UserSchema(
            username=user.username,
            email=validate_email,
            password_hash=password_hash
        )

        # Criar o usuário no banco de dados
        new_user = await self.repository.create(user_data)

        # Gerar tokens de acesso e refresh
        token_data = {"sub": user.email}
        AuthService.authenticator(token_data, response)


        # Converter o objeto SQLAlchemy para Pydantic
        user_schema = UserSchema.model_validate(new_user)

        return user_schema

        

    async def login_user(self, credentials: UserLoginSchema, response: Response) -> dict:
        """Autentica um usuário com e-mail e senha e gera tokens de acesso e refresh."""
        
        # 1. Verificar se o e-mail existe
        user = await self.repository.get_by_email(credentials.email)
        if not user:
            raise ValueError("E-mail ou senha inválidos")

        # 2. Verificar se a senha está correta
        if not HashManager.verify_password(credentials.password, user.password_hash):
            raise ValueError("E-mail ou senha inválidos")

        # 3. Gerar tokens de acesso e refresh
        token_data = {"sub": user.email}
        AuthService.authenticator(token_data, response)

        # 5. Converter o objeto SQLAlchemy para Pydantic
        user_schema = UserSchema.model_validate(user)

        # 6. Retornar o usuário e os tokens
        return {
            "user": user_schema
        }
    
    
    
    async def update_user(self, user_id: int, user_data: dict) -> UserSchema:
        """Atualiza os dados de um usuário."""
        # Verificar se o usuário existe
        user = await self.repository.read(user_id)
        if not user:
            raise ValueError("Usuário não encontrado")

        # Atualizar apenas os campos permitidos
        if "password_hash" in user_data:
            user_data["password_hash"] = HashManager.hash_password(user_data["password_hash"])

        # Atualizar o usuário no banco de dados
        updated_user = await self.repository.update(user_id, user_data)
        return updated_user


    async def delete_user(self, user_id: int) -> None:
        """Exclui um usuário."""
        # Verificar se o usuário existe
        user = await self.repository.read(user_id)
        if not user:
            raise ValueError("Usuário não encontrado")

        # Excluir o usuário
        await self.repository.delete(user_id)

    async def get_user_by_email(self, user_email: int) -> UserSchema:
        """Busca um usuário pelo ID"""
        user = await self.repository.get_by_email(user_email)
        return user
    
