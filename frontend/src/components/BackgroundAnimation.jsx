import React from 'react';
import { motion } from 'framer-motion';
import '../styles/BackgroundAnimation.css';

// número de partículas aqui
const particles = Array.from({ length: 150 });

const BackgroundAnimation = () => {
  return (
    <div className="background-animation">
      {particles.map((_, index) => {
        const top = Math.random() * 100;
        const left = Math.random() * 100;
        return (
          <motion.div
            key={index}
            className="particle"
            style={{ top: `${top}%`, left: `${left}%` }}
            initial={{ opacity: 0, y: 0 }}
            animate={{ opacity: 1, y: [0, -20, 0] }}
            transition={{
              duration: 4,
              repeat: Infinity,
              repeatType: 'mirror',
              delay: index * 0.2,
            }}
          />
        );
      })}
    </div>
  );
};

export default BackgroundAnimation;