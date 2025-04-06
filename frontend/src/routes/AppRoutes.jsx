import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from "../contexts/AuthContext";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Nursing from "../pages/Nursing";
import { RouterWithProgress } from "../components/RouterWithProgress"; // Importando o componente RouterWithProgress



const App = () => {
  return (
    <AuthProvider>
      <Router>
          <RouterWithProgress>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/nursing" element={<Nursing />} />
          </RouterWithProgress>
      </Router>
    </AuthProvider>
  );
};

export default App;
