import React from "react";
import { motion } from "framer-motion";
import "../../styles/Login.css";
import logo from "../../assets/ThermoCare.png";
import { Link } from "react-router-dom";
import LoginForm from "./LoginForm";

const LoginLayout = () => {
  return (
    <div className="login-container">
      <motion.div
        className="login-left-side"
        initial={{ opacity: 0, x: -50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8 }}
      >
        <div className="logo">
          <Link to={"/"}>
            <motion.img
              src={logo}
              alt="Logo"
              whileHover={{
                scale: 1.1,
                rotate: 5,
              }}
              transition={{ duration: 0.3 }}
            />
          </Link>
          <h1>Bem-vindo de volta ao ThermoCare!</h1>
          <p>Faça login para aproveitar os nossos recursos.</p>
        </div>
      </motion.div>

      <motion.div
        className="login-right-side"
        initial={{ opacity: 0, x: 50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8 }}
      >
        <LoginForm />
      </motion.div>
    </div>
  );
};

export default LoginLayout;
