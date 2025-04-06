class PasswordValidator:
    @staticmethod
    def validate_password(password: str, password_confirmation: str):
        """Valida a senha de acordo com as regras de negócio."""
        password_stripped = password.strip()
        
        if password != password_confirmation:
            raise ValueError("As senhas não coincidem")
        if password != password_stripped:
            raise ValueError("A senha não pode ter espaços no início ou no fim")
        
        if password == "":
            raise ValueError("A senha não pode ser vazia")
        
        if len(password) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres")
        
        if not any(char.isdigit() for char in password):
            raise ValueError("A senha deve conter pelo menos um número")
        
        if not any(char.isalpha() for char in password):
            raise ValueError("A senha deve conter pelo menos uma letra")
        

password_validator = PasswordValidator()