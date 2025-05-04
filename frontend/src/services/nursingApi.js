const API_URL = "http://localhost:8000/api/v1";

export async function registerNurse(userData) {
    const response = await fetch(`${API_URL}/users/me/nursing-homes`, {
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

export async function getNursingHome() {
    const response = await fetch(`${API_URL}/nursing-home`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include",
    });
    
    if (!response.ok) {
        throw new Error("Erro ao obter lares de idosos");
    }
    return response.json();
}