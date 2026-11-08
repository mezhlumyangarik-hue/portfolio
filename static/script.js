/* =========================================================
   mezhlumyan.dev — script.js
   (matches the new index.html and style.css)
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const fine = window.matchMedia("(pointer: fine)").matches;
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;


    /* ---------- Header background on scroll ---------- */

    const header = document.getElementById("siteHeader");

    const onScroll = () => {
        if (header) header.classList.toggle("scrolled", window.scrollY > 40);
    };

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();


    /* ---------- Mobile menu ---------- */

    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");

    if (menuBtn && navLinks) {

        const closeMenu = () => {
            navLinks.classList.remove("open");
            menuBtn.classList.remove("active");
        };

        menuBtn.addEventListener("click", () => {
            navLinks.classList.toggle("open");
            menuBtn.classList.toggle("active");
        });

        navLinks.querySelectorAll("a").forEach(a => a.addEventListener("click", closeMenu));

        document.addEventListener("keydown", e => {
            if (e.key === "Escape") closeMenu();
        });
    }


    /* ---------- Scroll reveal with a short stagger ---------- */

    const revealItems = document.querySelectorAll(".reveal, .reveal-left, .reveal-right");

    if (reduceMotion || !("IntersectionObserver" in window)) {

        revealItems.forEach(el => el.classList.add("visible"));

    } else {

        const observer = new IntersectionObserver((entries, obs) => {

            entries.forEach(entry => {

                if (!entry.isIntersecting) return;

                const el = entry.target;

                // stagger items that sit side by side in the same grid
                const siblings = el.parentElement
                    ? [...el.parentElement.children].filter(c => c.classList.contains("reveal"))
                    : [];
                const index = Math.max(0, siblings.indexOf(el));

                el.style.transitionDelay = `${(index % 4) * 90}ms`;
                el.classList.add("visible");

                // remove the delay afterwards so hover effects stay instant
                setTimeout(() => { el.style.transitionDelay = ""; }, 1200);

                obs.unobserve(el);
            });

        }, { threshold: 0.12, rootMargin: "0px 0px -50px 0px" });

        revealItems.forEach(el => observer.observe(el));
    }


    /* ---------- Hero mouse parallax (mouse devices only) ---------- */

    const heroVisual = document.querySelector(".hero-visual");

    if (heroVisual && fine && !reduceMotion) {

        const laptop = heroVisual.querySelector(".laptop");
        const techCards = heroVisual.querySelectorAll(".tech-card");

        heroVisual.addEventListener("mousemove", e => {

            const r = heroVisual.getBoundingClientRect();
            const x = (e.clientX - r.left) / r.width - 0.5;
            const y = (e.clientY - r.top) / r.height - 0.5;

            if (laptop) {
                laptop.style.transform =
                    `perspective(1200px) rotateY(${x * -7 - 5}deg) rotateX(${y * 5 + 3}deg)`;
            }

            techCards.forEach((card, i) => {
                const k = i % 2 === 0 ? 14 : 9;
                card.style.transform = `translate(${x * k}px, ${y * k}px)`;
            });
        });

        heroVisual.addEventListener("mouseleave", () => {
            if (laptop) laptop.style.transform = "";
            techCards.forEach(card => { card.style.transform = ""; });
        });
    }


    /* ---------- Custom cursor (mouse devices only) ---------- */

    const dot = document.querySelector(".cursor-dot");
    const ring = document.querySelector(".cursor-ring");

    if (dot && ring && fine && !reduceMotion) {

        let mx = 0, my = 0, rx = 0, ry = 0;

        document.addEventListener("mousemove", e => {
            mx = e.clientX;
            my = e.clientY;
            dot.style.left = `${mx}px`;
            dot.style.top = `${my}px`;
        });

        const follow = () => {
            rx += (mx - rx) * 0.13;
            ry += (my - ry) * 0.13;
            ring.style.left = `${rx}px`;
            ring.style.top = `${ry}px`;
            requestAnimationFrame(follow);
        };

        follow();

        document
            .querySelectorAll("a, button, summary, .service-card, .pj, .step, .mini-card")
            .forEach(el => {
                el.addEventListener("mouseenter", () => ring.classList.add("cursor-hover"));
                el.addEventListener("mouseleave", () => ring.classList.remove("cursor-hover"));
            });
    }


    /* ---------- Active navigation link ---------- */

    const sections = document.querySelectorAll("section[id]");
    const navItems = document.querySelectorAll(".nav-link, .dots a");

    const updateActiveNav = () => {

        let current = "";

        sections.forEach(section => {
            const top = section.offsetTop - 160;
            if (window.scrollY >= top && window.scrollY < top + section.offsetHeight) {
                current = section.id;
            }
        });

        navItems.forEach(link => {
            link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
        });
    };

    window.addEventListener("scroll", updateActiveNav, { passive: true });
    updateActiveNav();


    /* ---------- Project card tilt (mouse devices only) ---------- */

    if (fine && !reduceMotion) {

        document.querySelectorAll(".pj").forEach(card => {

            card.addEventListener("mousemove", e => {
                const r = card.getBoundingClientRect();
                const ry = ((e.clientX - r.left) / r.width - 0.5) * 3;
                const rx = ((e.clientY - r.top) / r.height - 0.5) * -3;
                card.style.transform =
                    `perspective(1000px) translateY(-8px) rotateX(${rx}deg) rotateY(${ry}deg)`;
            });

            card.addEventListener("mouseleave", () => { card.style.transform = ""; });
        });
    }


    /* ---------- Smooth anchor scrolling ---------- */

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            const id = this.getAttribute("href");
            if (!id || id === "#") return;

            const target = document.querySelector(id);
            if (!target) return;

            e.preventDefault();
            target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
        });
    });


    /* ---------- Scroll progress bar + parallax variable ---------- */

    const progress = document.getElementById("progress");
    const root = document.documentElement;
    let ticking = false;

    const frame = () => {
        const y = window.scrollY;
        const max = root.scrollHeight - window.innerHeight;
        if (progress) progress.style.transform = `scaleX(${max > 0 ? Math.min(y / max, 1) : 0})`;
        if (!reduceMotion) root.style.setProperty("--sy", y);
        ticking = false;
    };

    window.addEventListener("scroll", () => {
        if (!ticking) {
            ticking = true;
            requestAnimationFrame(frame);
        }
    }, { passive: true });

    frame();


    /* ---------- Split big headings into sliding words ---------- */

    document.querySelectorAll(".section-heading h2, .contact-content h2").forEach(h => {

        const words = h.textContent.trim().split(/\s+/);
        h.setAttribute("aria-label", h.textContent.trim());
        h.innerHTML = words
            .map((w, i) => `<span class="w" aria-hidden="true"><span style="--i:${i}">${w}</span></span>`)
            .join(" ");
    });


    /* ---------- Magnetic buttons (mouse devices only) ---------- */

    if (fine && !reduceMotion) {

        document.querySelectorAll(".main-btn, .outline-btn, .header-cta, .contact-main-btn, .contact-outline-btn").forEach(btn => {

            btn.addEventListener("mousemove", e => {
                const r = btn.getBoundingClientRect();
                const x = (e.clientX - r.left - r.width / 2) * 0.18;
                const y = (e.clientY - r.top - r.height / 2) * 0.28;
                btn.style.translate = `${x}px ${y}px`;
            });

            btn.addEventListener("mouseleave", () => { btn.style.translate = ""; });
        });


        /* ---------- Spotlight follows the cursor inside cards ---------- */

        document.querySelectorAll(".service-card, .mini-card, .step, .pj").forEach(card => {

            card.addEventListener("mousemove", e => {
                const r = card.getBoundingClientRect();
                card.style.setProperty("--mx", `${e.clientX - r.left}px`);
                card.style.setProperty("--my", `${e.clientY - r.top}px`);
            });
        });
    }


    /* ---------- Page loaded ---------- */

    document.body.classList.add("page-loaded");
});
