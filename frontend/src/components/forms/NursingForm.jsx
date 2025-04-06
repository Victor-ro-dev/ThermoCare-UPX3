import React, { useState } from "react";
import createInViewObserver from '../../utils/functions';

const NursingForm = () => {
  const [name, setName] = useState("");
  const [cep, setCep] = useState("");
  const [logradouro, setLogradouro] = useState("");
  const [numero, setNumero] = useState("");
  const [bairro, setBairro] = useState("");
  const [cidade, setCidade] = useState("");
  const [estado, setEstado] = useState("");
  const [complemento, setComplemento] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  

  // Função para buscar o endereço pelo CEP
  const handleCepChange = async (e) => {
    const cepValue = e.target.value.replace(/\D/g, ""); // Remove caracteres não numéricos
    setCep(cepValue);

    if (cepValue.length === 8) {
      try {
        setLoading(true);
        const response = await fetch(`https://viacep.com.br/ws/${cepValue}/json/`);
        const data = await response.json();

        if (data.erro) {
          setError("CEP não encontrado.");
          setLogradouro("");
          setBairro("");
          setCidade("");
          setEstado("");
        } else {
          setError("");
          setLogradouro(data.logradouro || "");
          setBairro(data.bairro || "");
          setCidade(data.localidade || "");
          setEstado(data.uf || "");
        }
      } catch (err) {
        setError("Erro ao buscar o CEP. Tente novamente.");
      } finally {
        setLoading(false);
      }
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name.trim() || !cep.trim() || !logradouro.trim() || !numero.trim() || !bairro.trim() || !cidade.trim() || !estado.trim()) {
      setError("Todos os campos obrigatórios devem ser preenchidos.");
      return;
    }

    alert("Dados enviados com sucesso!");
  };

  return (
    <form className="nursing-form" onSubmit={handleSubmit}>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <div className="form-row">
        <div className="form-group">
          <label htmlFor="nursing-name">Nome do Asilo</label>
          <input
            type="text"
            id="nursing-name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="nursing-cep">CEP</label>
          <input
            type="text"
            id="nursing-cep"
            value={cep}
            onChange={handleCepChange}
            maxLength="9"
            required
          />
        </div>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label htmlFor="nursing-logradouro">Endereço</label>
          <input
            type="text"
            id="nursing-logradouro"
            value={logradouro}
            onChange={(e) => setLogradouro(e.target.value)}
            disabled={!cep || loading}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="nursing-numero">Número</label>
          <input
            type="text"
            id="nursing-numero"
            value={numero}
            onChange={(e) => setNumero(e.target.value)}
            required
          />
        </div>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label htmlFor="nursing-bairro">Bairro</label>
          <input
            type="text"
            id="nursing-bairro"
            value={bairro}
            onChange={(e) => setBairro(e.target.value)}
            disabled={!cep || loading}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="nursing-cidade">Cidade</label>
          <input
            type="text"
            id="nursing-cidade"
            value={cidade}
            onChange={(e) => setCidade(e.target.value)}
            disabled={!cep || loading}
            required
          />
        </div>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label htmlFor="nursing-estado">Estado</label>
          <input
            type="text"
            id="nursing-estado"
            value={estado}
            onChange={(e) => setEstado(e.target.value)}
            disabled={!cep || loading}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="nursing-complemento">Complemento</label>
          <input
            type="text"
            id="nursing-complemento"
            value={complemento}
            onChange={(e) => setComplemento(e.target.value)}
          />
        </div>
      </div>

      <button className="subimit-button" type="submit" disabled={loading}>
        {loading ? "Carregando..." : "Cadastrar"}
      </button>
    </form>
  );
};

export default NursingForm;