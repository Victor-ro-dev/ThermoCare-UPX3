class EmailValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Verifica se o email está em minúsculo."""
        email_lower = email.lower()
        return email_lower