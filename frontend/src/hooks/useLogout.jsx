import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { logoutUser } from "../services/userAuthApi";
import { useAuth } from "../contexts/AuthContext";

export const useLogout = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const { setUser } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    setLoading(true);
    setError("");

    try {
      // 1. Faz logout no backend
      await logoutUser();
      
      // 2. Limpa o estado e armazenamento
      setUser(null);
      localStorage.clear();
      sessionStorage.clear();
      
      // 3. Força recarregamento imediato
      window.location.href = "/login"; // Usamos href em vez de navigate
      
    } catch (err) {
      setError(err.message);
      // 4. Recarrega mesmo em caso de erro
      window.location.href = "/login";
    } finally {
      setLoading(false);
    }
  };

  return { loading, error, handleLogout };
};