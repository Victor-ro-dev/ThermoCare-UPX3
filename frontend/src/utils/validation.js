export const validateRegisterForm = ({ username, email, password, password_confirmation }) => {
    if (!username.trim()) return "O nome de usuário é obrigatório.";
    if (!email.includes("@")) return "O email deve ser válido.";
    if (password.length < 8) return "A senha deve ter pelo menos 8 caracteres.";
    if (password !== password_confirmation) return "As senhas não coincidem.";
    return null;
  };