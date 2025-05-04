const API_URL = "http://localhost:8000/api/v1"; // Ajuste conforme necessário

// Função para registrar um usuário
export async function registerUser(userData) {
    const response = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
        credentials: "include",
    });

    
    
    if (!response.ok) {
        throw new Error("Erro ao registrar usuário");
    }
    return response.json();
}

// Função para fazer login
export async function loginUser(credentials) {
    const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
        credentials: "include",
    });

    if (!response.ok) {
        throw new Error("Credenciais inválidas");
    }
    return response.json();
}

// Função para verificar usuário autenticado
export const getCurrentUser = async () => {
    try {
        const response = await fetch(`${API_URL}/auth/me`, {
            method: "GET",
            credentials: "include",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        });

        if (response.status === 401) {
            console.log("Token inválido/expirado - redirecionando para login");
            return null;
        }

        if (!response.ok) {
            throw new Error("Erro ao verificar autenticação");
        }

        return await response.json();
    } catch (error) {
        console.error("Erro no getCurrentUser:", error);
        return null;
    }
};

// Função para fazer logout
export async function logoutUser() {
    const response = await fetch(`${API_URL}/auth/logout`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
    });
    
    if (!response.ok) {
        throw new Error("Falha ao fazer logout");
    }
}

export async function getUserProfile() {
    const response = await fetch(`${API_URL}/user`, {
        method: "GET",
        credentials: "include",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    });
    if (!response.ok) {
        throw new Error("Erro ao buscar perfil do usuário");
    }
    return response.json();
}
