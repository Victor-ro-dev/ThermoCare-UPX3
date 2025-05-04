import React from 'react';
import { motion } from 'framer-motion';
import '../../styles/Features.css';
import createInViewObserver from '../../utils/functions';
import homeImg from '../../assets/home.png';
import alertImg from '../../assets/alerta.png';
import asiloImg from '../../assets/asilo.png';

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
    const [ref, inView] = createInViewObserver(0.2, false); 

    return (
        <div className="features" id="funcionalidades">
            {/* Título com animação */}
            <motion.h2
                ref={ref}
                initial={{ opacity: 0, y: 50 }} // Começa invisível e deslocado para baixo
                animate={{ opacity: inView ? 1 : 0, y: inView ? 0 : 50 }} // Aparece ao entrar, some ao sair
                transition={{ duration: 0.6 }}
            >
                Funcionalidades
            </motion.h2>

            {/* Lista de funcionalidades */}
            <Feature
                title="Monitoramento de Temperatura"
                description="Monitore a temperatura dos cômodos em tempo real."
                image={homeImg} 
            />
            <Feature
                title="Sistema de Notificações"
                description="Receba notificações no WhatsApp e Dashboard em casos de temperaturas baixas e altas."
                image={alertImg}
            />
            <Feature
                title="Cadastro de Asilos"
                description="Cadastre asilos e visualize sua localização no mapa."
                image={asiloImg}
            />
        </div>
    );
};

export default Features;
