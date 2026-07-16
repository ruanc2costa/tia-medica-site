(() => {
    const nav = document.getElementById('nav');
    const links = document.getElementById('navLinks');
    const menuButton = document.querySelector('.hamburger');

    const setMenuState = (open, returnFocus = false) => {
        if (!links || !menuButton) return;
        links.classList.toggle('open', open);
        menuButton.setAttribute('aria-expanded', String(open));
        menuButton.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
        if (returnFocus) menuButton.focus();
    };

    if (menuButton && links) {
        menuButton.addEventListener('click', () => {
            setMenuState(!links.classList.contains('open'));
        });

        links.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', () => setMenuState(false));
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && links.classList.contains('open')) {
                setMenuState(false, true);
            }
        });
    }

    if (nav) {
        const updateNav = () => nav.classList.toggle('scrolled', window.scrollY > 50);
        window.addEventListener('scroll', updateNav, { passive: true });
        updateNav();
    }

    const faqButtons = [...document.querySelectorAll('.faq-q')];
    const closeFaq = (button) => {
        const item = button.closest('.faq-item');
        const answer = item?.querySelector('.faq-a');
        item?.classList.remove('active');
        if (answer) {
            answer.style.maxHeight = '0';
            answer.setAttribute('aria-hidden', 'true');
        }
        button.setAttribute('aria-expanded', 'false');
    };

    faqButtons.forEach((button, index) => {
        const item = button.closest('.faq-item');
        const answer = item?.querySelector('.faq-a');
        if (!item || !answer) return;

        const buttonId = `faq-pergunta-${index + 1}`;
        const answerId = `faq-resposta-${index + 1}`;
        button.id = buttonId;
        button.setAttribute('aria-controls', answerId);
        button.setAttribute('aria-expanded', 'false');
        answer.id = answerId;
        answer.setAttribute('role', 'region');
        answer.setAttribute('aria-labelledby', buttonId);
        answer.setAttribute('aria-hidden', 'true');

        button.addEventListener('click', () => {
            const shouldOpen = !item.classList.contains('active');
            faqButtons.forEach(closeFaq);
            if (!shouldOpen) return;

            item.classList.add('active');
            answer.style.maxHeight = `${answer.scrollHeight}px`;
            answer.setAttribute('aria-hidden', 'false');
            button.setAttribute('aria-expanded', 'true');
        });
    });

    const animatedCards = document.querySelectorAll(
        '.p-card,.step,.f-card,.v-card,.pe-card,.t-card,.r-card,.about-card,.plat-card'
    );
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (reduceMotion || !('IntersectionObserver' in window)) {
        animatedCards.forEach((element) => {
            element.style.opacity = '1';
            element.style.transform = 'none';
        });
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        });
    }, { threshold: .1 });

    animatedCards.forEach((element) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity .6s ease, transform .6s ease';
        observer.observe(element);
    });
})();
