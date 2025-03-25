import React from "react";
import { motion } from "framer-motion";
import { buttonVariants } from "../../utils/functions";
import { useRegister } from "../../hooks/useRegister";

const RegisterForm = () => {
  const {
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
  } = useRegister();

  return (
    <form className="register-form" onSubmit={handleSubmit}>
      <h2>Sign Up</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <div className="form-group">
        <label htmlFor="register-username">Username</label>
        <motion.input
          type="text"
          id="register-username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          whileFocus={{ scale: 1.02, boxShadow: "0px 0px 8px rgba(0, 0, 0, 0.2)" }}
        />
      </div>

      <div className="form-group">
        <label htmlFor="register-email">Email</label>
        <motion.input
          type="email"
          id="register-email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          whileFocus={{ scale: 1.02, boxShadow: "0px 0px 8px rgba(0, 0, 0, 0.2)" }}
        />
      </div>

      <div className="form-group">
        <label htmlFor="register-password">Password</label>
        <motion.input
          type="password"
          id="register-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          whileFocus={{ scale: 1.02, boxShadow: "0px 0px 8px rgba(0, 0, 0, 0.2)" }}
        />
      </div>

      <div className="form-group">
        <label htmlFor="register-confirm-password">Confirm Password</label>
        <motion.input
          type="password"
          id="register-confirm-password"
          value={password_confirmation}
          onChange={(e) => setPasswordConfirmation(e.target.value)}
          required
          whileFocus={{ scale: 1.02, boxShadow: "0px 0px 8px rgba(0, 0, 0, 0.2)" }}
        />
      </div>

      <motion.button
        type="submit"
        className="register-button"
        variants={buttonVariants}
        whileHover="hover"
        whileTap="tap"
        disabled={loading}
      >
        {loading ? "Carregando..." : "Sign Up"}
      </motion.button>

      <div className="signin-link">
        <p>
          Have an account? <a href="/login">Sign In</a>
        </p>
      </div>
    </form>
  );
};

export default RegisterForm;


