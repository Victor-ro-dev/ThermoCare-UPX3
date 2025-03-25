import React, { createContext, useContext, useState, useEffect } from "react";
import { getCurrentUser, loginUser, logoutUser, registerUser } from "../services/userAuthApi";

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function checkUser() {
            try {
                const userData = await getCurrentUser();
                setUser(userData);
            } catch (error) {
                setUser(null);
            } finally {
                setLoading(false);
            }
        }
        checkUser();
    }, []);

    async function handleLogin(credentials) {
        try {
            setLoading(true);
            const userData = await loginUser(credentials);
            setUser(userData);
            window.location.assign('/')
            return userData;
        } finally {
            setLoading(false);
        }
    }

    async function handleRegister(registerData) {
        try {
            setLoading(true);
            const userData = await registerUser(registerData);
            setUser(userData);
            return userData;
        } finally {
            setLoading(false);
        }
    }

    async function handleLogout() {
        try {
            setLoading(true);
            await logoutUser();
            setUser(null);
            window.location.reload();
        } finally {
            setLoading(false);
        }
    }

    return (
        <AuthContext.Provider value={{ 
            user, 
            loading, 
            handleLogin, 
            handleRegister, 
            handleLogout 
        }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    return useContext(AuthContext);
}
