// useLogin.js - Versão Aprimorada
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

export const useLogin = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { handleLogin } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Preencha todos os campos");
      return;
    }

    setLoading(true);
    setError("");

    try {
      
      await handleLogin({ email, password });
      navigate("/");
    } catch (err) {
      setError(err.message || "Falha no login. Tente novamente.");
    } finally {
      setLoading(false);
    }
  };

  return { email, setEmail, password, setPassword, error, loading, handleSubmit };
};