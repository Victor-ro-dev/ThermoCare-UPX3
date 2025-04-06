class UsernameValidator:
    @staticmethod
    def validate_username(username: str):
        """Valida o username de acordo com as regras de negócio."""
        username_stripped = username.strip()
        if username != username_stripped:
            raise ValueError("O username não pode ter espaços no início ou no fim")
        if len(username) < 3:
            raise ValueError("O username deve ter pelo menos 3 caracteres")
        if len(username) > 20:
            raise ValueError("O username deve ter no máximo 20 caracteres")