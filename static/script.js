document.addEventListener("DOMContentLoaded", () => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(pointer: fine)").matches;
  const header = document.getElementById("header");
  const progress = document.getElementById("progress");
  const nav = document.getElementById("nav");
  const menu = document.getElementById("menuToggle");

  // Scroll Progress & Sticky Header
  const onScroll = () => {
    const y = window.scrollY;
    header?.classList.toggle("scrolled", y > 24);
    const max = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.transform = `scaleX(${max > 0 ? y / max : 0})`;
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile Menu
  menu?.addEventListener("click", () => {
    nav?.classList.toggle("open");
    menu.classList.toggle("active");
  });
  nav?.querySelectorAll("a").forEach(a => a.addEventListener("click", () => {
    nav.classList.remove("open");
    menu?.classList.remove("active");
  }));

  // Reveal on Scroll
  const items = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    items.forEach(el => el.classList.add("visible"));
  } else {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("visible");
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -30px 0px" });
    items.forEach(el => observer.observe(el));
  }

  // 3D Hero Card Interaction
  const art = document.getElementById("heroArt");
  const core = document.getElementById("artCore");
  const chips = [...document.querySelectorAll("[data-float]")];
  if (art && core && fine && !reduce) {
    let targetX = 0, targetY = 0, currentX = 0, currentY = 0;
    const animate = () => {
      currentX += (targetX - currentX) * 0.08;
      currentY += (targetY - currentY) * 0.08;
      core.style.transform = `rotateX(${currentY * -10 - 6}deg) rotateY(${targetX * 12}deg) rotateZ(${-6 + currentX * 2}deg)`;
      chips.forEach((chip, i) => {
        const factor = (i + 1) * 10;
        chip.style.transform = `translate(${currentX * factor}px, ${currentY * factor}px)`;
      });
      requestAnimationFrame(animate);
    };
    animate();
    art.addEventListener("pointermove", e => {
      const r = art.getBoundingClientRect();
      targetX = ((e.clientX - r.left) / r.width - 0.5) * 2;
      targetY = ((e.clientY - r.top) / r.height - 0.5) * 2;
    });
    art.addEventListener("pointerleave", () => { targetX = 0; targetY = 0; });
  }

  // Quick Order Modal & Direct WhatsApp Integration
  const modal = document.getElementById("orderModal");
  const closeModal = document.getElementById("closeModal");
  const serviceInput = document.getElementById("clientService");
  const orderForm = document.getElementById("quickOrderForm");

  document.querySelectorAll(".open-modal-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const selectedService = btn.getAttribute("data-service") || "Կայքի պատվեր";
      if (serviceInput) serviceInput.value = selectedService;
      modal?.classList.add("open");
      modal?.setAttribute("aria-hidden", "false");
    });
  });

  const hideModal = () => {
    modal?.classList.remove("open");
    modal?.setAttribute("aria-hidden", "true");
  };
  closeModal?.addEventListener("click", hideModal);
  modal?.addEventListener("click", e => { if (e.target === modal) hideModal(); });

  orderForm?.addEventListener("submit", e => {
    e.preventDefault();
    const name = document.getElementById("clientName").value.trim();
    const phone = document.getElementById("clientPhone").value.trim();
    const service = serviceInput.value.trim();

    if (!name || !phone) return;

    const text = `Բարև Ձեզ, Mezhlumyan Web Dev!\nԱնուն / Բիզնես՝ ${name}\nՀեռախոս՝ ${phone}\nԾառայություն՝ ${service}`;
    const waUrl = `https://wa.me/37496787855?text=${encodeURIComponent(text)}`;
    window.open(waUrl, "_blank", "noopener,noreferrer");
    hideModal();
    orderForm.reset();
  });

  // Smooth Anchor Scroll
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener("click", e => {
      const target = document.querySelector(a.getAttribute("href"));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    });
  });
});
