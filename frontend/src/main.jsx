import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles/index.css";
import AppRoutes from "./routes/AppRoutes"; // Importa o AuthProvider
import "@fortawesome/fontawesome-free/css/all.min.css";

createRoot(document.getElementById("root")).render(
  <StrictMode>
      <AppRoutes />
  </StrictMode>
);