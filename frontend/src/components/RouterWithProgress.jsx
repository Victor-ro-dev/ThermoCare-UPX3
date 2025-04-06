import { useEffect } from "react";
import { useLocation, useNavigationType, Routes } from "react-router-dom";
import nProgress from "nprogress";

export const RouterWithProgress = ({ children }) => {
  const location = useLocation();
  const navigationType = useNavigationType();

  useEffect(() => {
    nProgress.configure({ showSpinner: false }); // Configuração opcional
    nProgress.start();

    const timer = setTimeout(() => {
      nProgress.done();
    }, 300);

    return () => clearTimeout(timer);
  }, [location.pathname, navigationType]);

  return <Routes>{children}</Routes>;
};