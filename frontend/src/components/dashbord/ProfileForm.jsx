import React, { useState, useEffect } from "react";
import { getUserProfile } from "../../services/userAuthApi";
import "../../styles/Login.css";

const ProfileForm = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [editing, setEditing] = useState(false);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchProfile() {
      try {
        const data = await getUserProfile();
        setUsername(data.username || "");
        setEmail(data.email || "");
      } catch (err) {
        setMessage("Erro ao carregar perfil.");
      } finally {
        setLoading(false);
      }
    }
    fetchProfile();
  }, []);

  const handleUpdate = async (e) => {
    e.preventDefault();
    setMessage("Perfil atualizado (simulação).");
    setEditing(false);
  };

  const handleDelete = async () => {
    if (window.confirm("Tem certeza que deseja excluir sua conta?")) {
      setMessage("Conta excluída (simulação).");
    }
  };

  if (loading) {
    return <div className="dashboard-main-content"><p>Carregando perfil...</p></div>;
  }

  return (
    <div className="dashboard-main-content">
      <form style={{ minWidth: 350 }} onSubmit={handleUpdate}>
        <div className="logo logo-container">
          <h2>Perfil do Usuário</h2>
        </div>
        <br />
        <div className="profile-group">
          <div className="form-group-login">
            <label>Nome de usuário:</label>
            <input
              type="text"
              value={username}
              disabled={!editing}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group-login">
            <label>Email:</label>
            <input
              type="email"
              value={email}
              disabled={!editing}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div style={{ display: "flex", gap: "1rem", marginTop: "1rem" }}>
            {editing ? (
              <button className="login-button" type="submit">Salvar</button>
            ) : (
              <button className="login-button" type="button" onClick={() => setEditing(true)}>
                Editar
              </button>
            )}
            <button
              type="button"
              className="login-button"
              style={{ background: "#f44242" }}
              onClick={handleDelete}
            >
              Excluir Conta
            </button>
          </div>
          {message && <p style={{ marginTop: "1rem" }}>{message}</p>}
        </div>
      </form>
    </div>
  );
};

export default ProfileForm;