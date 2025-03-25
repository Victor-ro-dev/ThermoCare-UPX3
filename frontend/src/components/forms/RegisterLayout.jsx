import React from "react";
import { motion } from "framer-motion";
import "../../styles/Register.css";
import logo from "../../assets/ThermoCare.png";
import { Link } from "react-router-dom";
import RegisterForm from "./RegisterForm";

const RegisterLayout = () => {
  return (
    <div className="register-container">
      <motion.div
        className="register-left-side"
        initial={{ opacity: 0, x: 50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8 }}
      >
        <div className="logo">
          <Link to={"/"}>
            <motion.img
              src={logo}
              alt="Logo"
              whileHover={{ scale: 1.1, rotate: 5 }}
              transition={{ duration: 0.3 }}
            />
          </Link>
          <h1>Bem-vindo ao ThermoCare!</h1>
          <p>Abra uma conta no nosso site e aproveite os nossos recursos.</p>
        </div>
      </motion.div>

      <motion.div
        className="register-right-side"
        initial={{ opacity: 0, x: -50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8 }}
      >
        <RegisterForm />
      </motion.div>
    </div>
  );
};

export default RegisterLayout;
