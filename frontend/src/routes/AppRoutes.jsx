import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from "../contexts/AuthContext";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Nursing from "../pages/Nursing";
import Dashboard from "../pages/Dashboard";
import { RouterWithProgress } from "../components/RouterWithProgress"; // Importando o componente RouterWithProgress
import PublicRoute from "./PublicRoute";

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <RouterWithProgress>
          <Route path="/" element={<Home />} />
          <Route
            path="/login"
            element={
              <PublicRoute>
                <Login />
              </PublicRoute>
            }
          />
          <Route
            path="/register"
            element={
              <PublicRoute>
                <Register />
              </PublicRoute>
            }
          />
          <Route path="/nursing" element={<Nursing />}
          />
          <Route path="/dashboard" element={<Dashboard />} />
        </RouterWithProgress>
      </Router>
    </AuthProvider>
  );
};

export default App;
