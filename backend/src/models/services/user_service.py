from fastapi import Response
from src.models.schemas.bd_schema import UserSchema, UserLoginSchema, UserCreateSchema
from src.controller.auth.hash_manager import HashManager
from src.controller.auth.token_manager import TokenManager
from src.controller.auth.cookie_manager import CookieManager
from src.controller.auth.password_validator import PasswordValidator
from src.controller.auth.username_validator import UsernameValidator
from src.controller.auth.email_validator import EmailValidator
from src.models.repositories.user_repository import UserInterface


class UserService:
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
        access_token = TokenManager.create_access_token(data=token_data)
        refresh_token = TokenManager.create_refresh_token(data=token_data)

        # Configurar cookies
        CookieManager.set_access_token_cookie(response, access_token)
        CookieManager.set_refresh_token_cookie(response, refresh_token)


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
        access_token = TokenManager.create_access_token(data=token_data)
        refresh_token = TokenManager.create_refresh_token(data=token_data)

        print(f"Token recebido no login_user: {access_token}")

        # 4. Configurar os tokens nos cookies
        CookieManager.set_access_token_cookie(response, access_token)
        CookieManager.set_refresh_token_cookie(response, refresh_token)

        # 5. Converter o objeto SQLAlchemy para Pydantic
        user_schema = UserSchema.model_validate(user)

        # 6. Retornar o usuário e os tokens
        return {
            "user": user_schema,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    async def get_authenticated_user(self, access_token: str) -> UserSchema:
        """Obtém o usuário autenticado pelo token de acesso."""
        try:
            print(f"Token recebido no try: {access_token}")

            # Obter o usuário pelo e-mail
            user = await self.repository.get_by_email(access_token)
            if not user:
                raise ValueError("Usuário não encontrado")

            # Converter o objeto SQLAlchemy para Pydantic
            user_schema = UserSchema.model_validate(user)
            return user_schema
        except ValueError as e:
            raise ValueError(f"Erro de validação: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado ao obter usuário autenticado: {str(e)}")
    
    
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