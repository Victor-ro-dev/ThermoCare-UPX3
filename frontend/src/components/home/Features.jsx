import React from 'react';
import { motion } from 'framer-motion';
import '../../styles/Features.css';
import createInViewObserver from '../../utils/functions';

const Feature = ({ title, description, image }) => {
    const [ref, inView] = createInViewObserver(0.2, false);

    return (
        <motion.div
            ref={ref}
            className="feature"
            initial={{ opacity: 0, y: 50 }} // Começa invisível e deslocado para baixo
            animate={{ opacity: inView ? 1 : 0, y: inView ? 0 : 50 }} // Aparece ao entrar, some ao sair
            transition={{ duration: 0.6 }}
        >
            <div className="feature-image">
                <img src={image} alt={title} />
            </div>
            <div className="feature-text">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </motion.div>
    );
};

const Features = () => {
    return (
        <div className="features" id="funcionalidades">
            <h2>Funcionalidades</h2>
            <Feature
                title="Monitoramento de Temperatura"
                description="Monitore a temperatura dos cômodos em tempo real."
                image="https://i.imgur.com/1Q2Q6QF.png"
            />
            <Feature
                title="Sistema de Notificações"
                description="Receba notificações em casos de temperaturas baixas e altas."
                image="https://i.imgur.com/1Q2Q6QF.png"
            />
            <Feature
                title="Análise de Dados"
                description="Analise como está a temperatura do ambiente em cada semana."
                image="https://i.imgur.com/1Q2Q6QF.png"
            />
        </div>
    );
};

export default Features;
