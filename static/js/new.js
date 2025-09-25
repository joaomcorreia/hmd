
const ticker = document.querySelector('.news-ticker-list');
ticker.addEventListener('mouseenter', () => {
    ticker.style.animationPlayState = 'paused';
});
ticker.addEventListener('mouseleave', () => {
    ticker.style.animationPlayState = 'running';
});
