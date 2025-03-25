import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { validateRegisterForm } from "../utils/validation"; // Importa a função de validação

export const useRegister = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password_confirmation, setPasswordConfirmation] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { handleRegister } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Valida os dados do formulário
    const validationError = validateRegisterForm({
      username,
      email,
      password,
      password_confirmation: password_confirmation, // Passa os dados para validação
    });

    if (validationError) {
      setError(validationError); // Exibe o erro de validação
      return;
    }

    setLoading(true);
    setError("");

    try {
      await handleRegister({
        username,
        email,
        password,
        password_confirmation,
      });
      navigate("/");
    } catch (err) {
      setError(err.response?.data?.message || err.message || "Falha no registro");
    } finally {
      setLoading(false);
    }
  };

  return {
    username,
    setUsername,
    email,
    setEmail,
    password,
    setPassword,
    password_confirmation,
    setPasswordConfirmation,
    error,
    loading,
    handleSubmit,
  };
};