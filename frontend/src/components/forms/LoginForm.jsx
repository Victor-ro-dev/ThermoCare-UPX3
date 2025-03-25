import React from "react";
import { motion } from "framer-motion";
import { buttonVariants } from "../../utils/functions";
import { useLogin } from "../../hooks/useLogin";

const LoginForm = () => {
  const { 
    email, 
    setEmail, 
    password, 
    setPassword, 
    handleSubmit,  // Mudei de 'login' para 'handleSubmit' para ficar consistente
    loading, 
    error 
  } = useLogin();

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      <h2>Sign In</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <div className="form-group-login">
        <label htmlFor="login-email">Enter Your Email</label>
        <motion.input
          type="email"
          id="login-email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          whileFocus={{
            scale: 1.02,
            boxShadow: "0px 0px 8px rgba(0, 0, 0, 0.2)",
          }}
        />
      </div>

      <div className="form-group-login">
        <label htmlFor="login-password">Enter Your Password</label>
        <motion.input
          type="password"
          id="login-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          autoComplete="current-password"
          whileFocus={{
            scale: 1.02,
            boxShadow: "0px 0px 8px rgba(0, 0, 0, 0.2)",
          }}
        />
      </div>

      <motion.button
        type="submit"
        className="login-button"
        variants={buttonVariants}
        whileHover="hover"
        whileTap="tap"
        disabled={loading}
      >
        {loading ? "Carregando..." : "Sign In"}
      </motion.button>

      <div className="forgot-password">
        <a href="/forgot-password">Forget Password?</a>
      </div>

      <div className="social-login">
        <div className="divider">
          <span>Or Sign In With</span>
        </div>
        <motion.button
          type="button"
          className="google-button"
          variants={buttonVariants}
          whileHover="hover"
          whileTap="tap"
        >
          <i className="fab fa-google"></i> Continue with Google
        </motion.button>
      </div>

      <div className="signup-link">
        <p>
          Don't have an account? <a href="/register">Sign Up</a>
        </p>
      </div>
    </form>
  );
};

export default LoginForm;