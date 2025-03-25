import React from "react";
import "../../styles/MainContent.css";
import { Link } from "react-router-dom";

const MainContent = () => {
  return (
    <div className="main-content">
      <h1 className="headline">Bem-vindo ao ThermoCare</h1>
      <p className="description">
        Monitore e cuide da saúde do seu asilo com precisão e qualidade
        utilizando as tecnologias de temperatura mais novas e inovadoras do
        mercado.
      </p>
      <div className="buttons">
        <Link to="/login">
          <button className="signin">Sign In</button>
        </Link>
        <Link to="/register">
        <button className="signup">Create an Account</button>
        </Link>
      </div>
    </div>
  );
};

export default MainContent;
