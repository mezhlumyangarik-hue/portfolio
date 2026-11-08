document.addEventListener("DOMContentLoaded", () => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(pointer: fine)").matches;
  const header = document.getElementById("header");
  const progress = document.getElementById("progress");
  const nav = document.getElementById("nav");
  const menu = document.getElementById("menuToggle");

  const onScroll = () => {
    const y = window.scrollY;
    header?.classList.toggle("scrolled", y > 24);
    const max = document.documentElement.scrollHeight - innerHeight;
    if (progress) progress.style.transform = `scaleX(${max > 0 ? y / max : 0})`;
  };
  addEventListener("scroll", onScroll, {passive:true});
  onScroll();

  menu?.addEventListener("click", () => {
    nav?.classList.toggle("open");
    menu.classList.toggle("active");
  });
  nav?.querySelectorAll("a").forEach(a => a.addEventListener("click", () => {
    nav.classList.remove("open"); menu?.classList.remove("active");
  }));

  const items = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) items.forEach(el => el.classList.add("visible"));
  else {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("visible");
        obs.unobserve(entry.target);
      });
    }, {threshold:.12, rootMargin:"0px 0px -35px 0px"});
    items.forEach(el => observer.observe(el));
  }

  // Soft spring-like 3D card movement. Disabled for touch and reduced-motion users.
  const art = document.getElementById("heroArt");
  const core = document.getElementById("artCore");
  const chips = [...document.querySelectorAll("[data-float]")];
  if (art && core && fine && !reduce) {
    let frame = 0;
    let targetX = 0, targetY = 0, currentX = 0, currentY = 0;
    const animate = () => {
      currentX += (targetX - currentX) * .075;
      currentY += (targetY - currentY) * .075;
      core.style.transform = `rotateX(${currentY * -9 - 7}deg) rotateY(${targetX * 11}deg) rotateZ(${-7 + targetX * 2}deg)`;
      chips.forEach((chip, i) => {
        const factor = (i + 1) * 9;
        chip.style.translate = `${currentX * factor}px ${currentY * factor}px`;
      });
      frame = requestAnimationFrame(animate);
    };
    art.addEventListener("pointermove", e => {
      const r = art.getBoundingClientRect();
      targetX = ((e.clientX - r.left) / r.width - .5) * 2;
      targetY = ((e.clientY - r.top) / r.height - .5) * 2;
      if (!frame) animate();
    });
    art.addEventListener("pointerleave", () => { targetX = 0; targetY = 0; });
  }

  if (fine && !reduce) {
    document.querySelectorAll(".magnetic").forEach(el => {
      el.addEventListener("pointermove", e => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width/2) * .08;
        const y = (e.clientY - r.top - r.height/2) * .12;
        el.style.transform = `translate(${x}px,${y}px)`;
      });
      el.addEventListener("pointerleave", () => el.style.transform = "");
    });
  }

  // Smooth anchor navigation with native fallback.
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener("click", e => {
      const target = document.querySelector(a.getAttribute("href"));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({behavior: reduce ? "auto" : "smooth", block:"start"});
    });
  });
});
