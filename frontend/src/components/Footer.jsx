import React from 'react';
import '../styles/Footer.css';
import logo from '../assets/ThermoCare.png';


const Footer = () => {
    return (
        <footer className="footer">
        <div className="footer-content">
            <div className="footer-logo">
                <a href="#"><img src={logo} alt="Logo" /></a>
                <p>ThermoCare</p>
            </div>
            <div>
                Copyrigth © 2025 ThermoCare
            </div>
            <div>
                <a href="#">Termos de uso</a>
                <a href="#">Política de privacidade</a>
            </div>

        </div>
        </footer>

    );
}

export default Footer;
