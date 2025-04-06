import React from "react";
import { motion } from "framer-motion";
import "../../styles/Nursing.css";
import NursingForm from "./NursingForm";

const NursingLayout = () => {
  return (
    <div className="nursing-container">
      <motion.div
        className="nursing-form-wrapper"
        initial={{ opacity: 0, y: 100 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
      >
        <h1>Cadastro do Asilo</h1>
        <p>Preencha as informações abaixo para cadastrar o asilo.</p>
        <NursingForm />
      </motion.div>
    </div>
  );
};

export default NursingLayout;