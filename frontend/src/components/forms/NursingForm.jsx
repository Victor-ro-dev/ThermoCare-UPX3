import React from "react";
import { useNursing } from "../../hooks/useNursing";

const NursingForm = () => {
    const {
        name,
        setName,
        cep,
        setCep,
        logradouro,
        setLogradouro,
        numero,
        setNumero,
        bairro,
        setBairro,
        cidade,
        setCidade,
        estado,
        setEstado,
        complemento,
        setComplemento,
        handleCepChange,
        handleSubmit,
        loading,
        error,
    } = useNursing();

    // Verifica se o CEP é válido (8 caracteres)
    const isCepValid = cep.length === 8;

    const handleFormSubmit = async (e) => {
        e.preventDefault();

        // Log dos dados antes de enviar
        console.log("Dados do formulário antes do envio:", {
            name,
            cep,
            logradouro,
            numero,
            bairro,
            cidade,
            estado,
            complemento,
        });

        try {
            await handleSubmit(e);
        } catch (err) {
            console.error("Erro ao enviar o formulário:", err);
        }
    };

    return (
        <form className="nursing-form" onSubmit={handleFormSubmit}>
            <h1>Cadastro do Asilo</h1>
            <div className="form-group">
                <label htmlFor="name">Nome</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="cep">CEP</label>
                <input
                    type="text"
                    id="cep"
                    value={cep}
                    onChange={handleCepChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="logradouro">Endereço</label>
                <input
                    type="text"
                    id="logradouro"
                    value={logradouro}
                    onChange={(e) => setLogradouro(e.target.value)}
                    disabled={!isCepValid} // Desabilita se o CEP não for válido
                    required
                />
            </div>
            <div className="form-group small">
                <label htmlFor="numero">Número</label>
                <input
                    type="text"
                    id="numero"
                    value={numero}
                    onChange={(e) => setNumero(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="bairro">Bairro</label>
                <input
                    type="text"
                    id="bairro"
                    value={bairro}
                    onChange={(e) => setBairro(e.target.value)}
                    disabled={!isCepValid} // Desabilita se o CEP não for válido
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="cidade">Cidade</label>
                <input
                    type="text"
                    id="cidade"
                    value={cidade}
                    onChange={(e) => setCidade(e.target.value)}
                    disabled={!isCepValid} // Desabilita se o CEP não for válido
                    required
                />
            </div>
            <div className="form-group small">
                <label htmlFor="estado">Estado</label>
                <input
                    type="text"
                    id="estado"
                    value={estado}
                    onChange={(e) => setEstado(e.target.value)}
                    disabled={!isCepValid} // Desabilita se o CEP não for válido
                    required
                />
            </div>
            <div className="form-group full-width">
                <label htmlFor="complemento">Complemento</label>
                <input
                    type="text"
                    id="complemento"
                    value={complemento}
                    onChange={(e) => setComplemento(e.target.value)}
                />
            </div>
            {error && <p className="error-message">{error}</p>}
            <button className="submit-button" type="submit" disabled={loading}>
                {loading ? "Carregando..." : "Cadastrar Asilo"}
            </button>
        </form>
    );
};

export default NursingForm;