import React from "react";
import "../../styles/Dashboard.css";
import { motion } from "framer-motion";
import logo from "../../assets/ThermoCare.png";
import { useLogout } from "../../hooks/useLogout";
import { useNavigate } from "react-router-dom";

const DashboardLeftSide = ({ activePage, setActivePage }) => {
    const { loading, handleLogout } = useLogout();
    const navigate = useNavigate();

    return (
        <div className="dashboard-left-side">
            <div
                className="logo logo-container"
                style={{ cursor: "pointer" }}
                onClick={() => navigate("/")}
            >
                <motion.img
                    src={logo}
                    alt="Logo"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 1 }}
                />
                <span style={{ marginLeft: 8, fontWeight: "bold", fontSize: 20 }}>
                    ThermoCare
                </span>
            </div>
            <div className="dashboard-menu">
                <ul>
                    <li className="dashboard-item">
                        <button
                            className={activePage === "dashboard" ? "dashboard-button active" : "dashboard-button"}
                            onClick={() => setActivePage("dashboard")}
                        >
                            <i className="fas fa-tachometer-alt"></i> Dashboard
                        </button>
                    </li>
                    <li className="dashboard-item">
                        <button
                            className={activePage === "nursing" ? "dashboard-button active" : "dashboard-button"}
                            onClick={() => setActivePage("nursing")}
                        >
                            <i className="fas fa-hospital"></i> Asilo
                        </button>
                    </li>
                    <li className="dashboard-item">
                        <button
                            className={activePage === "profile" ? "dashboard-button active" : "dashboard-button"}
                            onClick={() => setActivePage("profile")}
                        >
                            <i className="fas fa-user"></i> Perfil
                        </button>
                    </li>
                    <li className="dashboard-item">
                        <button
                            onClick={handleLogout}
                            disabled={loading}
                        >
                            <i className="fas fa-sign-out-alt"></i> Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    );
};

export default DashboardLeftSide;