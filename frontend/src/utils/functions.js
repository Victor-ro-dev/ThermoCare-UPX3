import { useInView } from 'react-intersection-observer';

function createInViewObserver(threshold = 0.2, triggerOnce = false) {
    return useInView({
        threshold, // Quando a porcentagem especificada do elemento estiver visível, ativa a animação
        triggerOnce // Mantém o efeito de aparecer/sumir ao rolar para cima/baixo
    });
}

export const buttonVariants = {
    hover: { scale: 1.05, transition: { duration: 0.2 } },
    tap: { scale: 0.95 },
};

export default createInViewObserver;