import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { useLogout } from "../hooks/useLogout";
import "../styles/Header.css";
import logo from "../assets/ThermoCare.png";

const Header = () => {
  const { user } = useAuth(); // Obtém o usuário autenticado
  const { loading, handleLogout } = useLogout(); // Usa o hook de logout

  return (
    <header className="header">
      <div className="logo">
        <Link to="/" className="logo">
          <img src={logo} alt="Logo" />
          <p>ThermoCare</p>
        </Link>
      </div>

      <nav className="navigation">
        <ul>
          <li>
            <a href="#sobre">Sobre</a>
          </li>
          <li>
            <a href="#funcionalidades">Funcionalidades</a>
          </li>
        </ul>
      </nav>

      <div className="auth-buttons">
        {user ? (
          <>
            <button className="singin">{user.username}</button>
            <button
              onClick={handleLogout}
              className="singin"
              disabled={loading} // Desabilita o botão enquanto faz logout
            >
              {loading ? "Saindo..." : "Logout"}
            </button>
          </>
        ) : (
          <>
            <Link to="/login">
              <button className="singin">Sign In</button>
            </Link>
            <Link to="/register">
              <button className="singup">Create an account</button>
            </Link>
          </>
        )}
      </div>
    </header>
  );
};

export default Header;
