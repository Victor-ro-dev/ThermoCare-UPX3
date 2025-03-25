import React from 'react';
import { motion } from 'framer-motion';
import '../../styles/About.css';
import logo from '../../assets/ThermoCare.png';
import createInViewObserver from '../../utils/functions';

const About = () => {
    const [ref, inView] = createInViewObserver(0.2, false);

    return (
        <div ref={ref} className="about" id="sobre">
            <motion.div
                initial={{ opacity: 0, y: 50 }} // Começa invisível e deslocado para baixo
                animate={{ opacity: inView ? 1 : 0, y: inView ? 0 : 50 }} // Aparece ao entrar, some ao sair
                transition={{ duration: 0.8 }}
            >
                <h2>Quem Somos Nós ?</h2>
                <div className="about-content">
                    <div className="about-text">
                        <p>O ThermoCare foi desenvolvido por um grupo de estudantes da Facens, Faculdade de Engenharia de Sorocaba, como projeto de UPX 3. O projeto foi desenvolvido com o intuito de facilitar o monitoramento da saúde dos idosos perante aos perigos de baixas e altas temperaturas, utilizando tecnologias de ponta para garantir a precisão e qualidade do serviço.
                        </p>
                    </div>
                    <div className='about-text'>
                        <img className='about-image' src={logo} alt="" />
                    </div>
                </div>
            </motion.div>
        </div>
    );
};

export default About;
