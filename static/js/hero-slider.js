(function(){
  const root = document.querySelector('.hero-slider');
  if(!root) return;
  const track = root.querySelector('.hero-slides');
  const slides = [...root.querySelectorAll('.hero-slide')];
  const dots = [...root.querySelectorAll('.hero-dot')];
  const prevBtn = root.querySelector('.hero-nav.prev');
  const nextBtn = root.querySelector('.hero-nav.next');
  const autoplayMs = parseInt(track.dataset.autoplay || '0', 10);
  let i = slides.findIndex(s => s.classList.contains('is-active'));
  let timer = null;

  function go(n){
    slides[i].classList.remove('is-active');
    dots[i].classList.remove('is-active');
    i = (n + slides.length) % slides.length;
    slides[i].classList.add('is-active');
    dots[i].classList.add('is-active');
    restart();
  }
  function next(){ go(i+1); }
  function prev(){ go(i-1); }
  function restart(){
    if(!autoplayMs || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    clearInterval(timer);
    timer = setInterval(next, autoplayMs);
  }

  prevBtn.addEventListener('click', prev);
  nextBtn.addEventListener('click', next);
  dots.forEach((d,idx)=>d.addEventListener('click', ()=>go(idx)));

  // keyboard
  document.addEventListener('keydown', e=>{
    if(e.key==='ArrowRight') next();
    if(e.key==='ArrowLeft') prev();
  });

  // touch swipe
  let sx=0;
  track.addEventListener('touchstart', e=>{ sx = e.changedTouches[0].clientX; }, {passive:true});
  track.addEventListener('touchend', e=>{
    const dx = e.changedTouches[0].clientX - sx;
    if(Math.abs(dx) > 40) (dx<0?next:prev)();
  }, {passive:true});

  restart();
})();
