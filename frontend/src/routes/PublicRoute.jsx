import React from "react";
import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

const PublicRoute = ({ children }) => {
  const { user } = useAuth();
  const location = useLocation();

  // Se o usuário estiver autenticado e NÃO estiver na tela de registro, redireciona para o dashboard
  if (user && location.pathname !== "/register") {
    return <Navigate to="/dashboard" />;
  }
  return children;
};

export default PublicRoute;