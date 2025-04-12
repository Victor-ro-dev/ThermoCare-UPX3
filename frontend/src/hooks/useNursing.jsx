import { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import { registerNurse } from "../services/nursingApi";

export const useNursing = () => {
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
    const { user, loading: authLoading } = useAuth(); // Verifica o usuário autenticado
    const navigate = useNavigate();

    // Redireciona para login se o usuário não estiver autenticado
    useEffect(() => {
        if (!authLoading && !user) {
            navigate("/login");
        }
    }, [authLoading, user, navigate]);

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

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!name.trim() || !cep.trim() || !logradouro.trim() || !numero.trim() || !bairro.trim() || !cidade.trim() || !estado.trim()) {
            setError("Todos os campos obrigatórios devem ser preenchidos.");
            return;
        }

        
        try {
            setLoading(true);
            const nurseData = {
                name,
                cep,
                logradouro,
                numero,
                bairro,
                cidade,
                estado,
                complemento,
            };
            console.log("Enviando dados para a API:", nurseData);
            await registerNurse(nurseData); // Chama a API para registrar os dados
            navigate("/nurses"); // Redireciona para a lista de enfermeiros após o registro
        } catch (err) {
            setError(err.message || "Erro ao registrar o asilo.");
        } finally {
            setLoading(false);
        }
    };

    return {
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
        error,
        loading,
        handleCepChange,
        handleSubmit,
    };
};