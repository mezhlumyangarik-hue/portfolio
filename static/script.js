/* =========================================================
   PORTFOLIO JAVASCRIPT
========================================================= */

document.addEventListener("DOMContentLoaded", () => {


    /* =====================================================
       HEADER SCROLL EFFECT
    ===================================================== */

    const header = document.getElementById("siteHeader");

    const handleHeaderScroll = () => {

        if (window.scrollY > 40) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }

    };

    window.addEventListener(
        "scroll",
        handleHeaderScroll,
        { passive: true }
    );

    handleHeaderScroll();


    /* =====================================================
       MOBILE MENU
    ===================================================== */

    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");

    if (menuBtn && navLinks) {

        menuBtn.addEventListener("click", () => {

            navLinks.classList.toggle("open");

            menuBtn.classList.toggle("active");

        });


        navLinks.querySelectorAll("a").forEach(link => {

            link.addEventListener("click", () => {

                navLinks.classList.remove("open");

                menuBtn.classList.remove("active");

            });

        });

    }


    /* =====================================================
       SCROLL REVEAL
    ===================================================== */

    const revealElements =
        document.querySelectorAll(
            ".reveal, .reveal-left, .reveal-right"
        );


    const revealObserver =
        new IntersectionObserver(
            (entries, observer) => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    entry.target.classList.add("visible");

                    observer.unobserve(entry.target);

                });

            },
            {
                threshold: 0.12,
                rootMargin: "0px 0px -50px 0px"
            }
        );


    revealElements.forEach(element => {

        revealObserver.observe(element);

    });


    /* =====================================================
       STAGGER PROJECT CARDS
    ===================================================== */

    const projectCards =
        document.querySelectorAll(".project-card");


    projectCards.forEach((card, index) => {

        card.style.transitionDelay =
            `${index * 80}ms`;

    });


    /* =====================================================
       STAGGER SERVICE CARDS
    ===================================================== */

    const serviceCards =
        document.querySelectorAll(".service-card");


    serviceCards.forEach((card, index) => {

        card.style.transitionDelay =
            `${index * 100}ms`;

    });


    /* =====================================================
       MOUSE PARALLAX
    ===================================================== */

    const heroVisual =
        document.querySelector(".hero-visual");


    if (
        heroVisual &&
        window.matchMedia("(pointer: fine)").matches
    ) {

        heroVisual.addEventListener(
            "mousemove",
            (event) => {

                const rect =
                    heroVisual.getBoundingClientRect();

                const x =
                    (event.clientX - rect.left)
                    / rect.width
                    - 0.5;

                const y =
                    (event.clientY - rect.top)
                    / rect.height
                    - 0.5;


                const laptop =
                    heroVisual.querySelector(".laptop");


                if (laptop) {

                    laptop.style.transform =
                        `perspective(1200px)
                         rotateY(${x * -7 - 5}deg)
                         rotateX(${y * 5 + 3}deg)
                         translateY(-5px)`;

                }


                const techCards =
                    heroVisual.querySelectorAll(
                        ".tech-card"
                    );


                techCards.forEach((card, index) => {

                    const strength =
                        (index % 2 === 0)
                            ? 14
                            : 9;

                    card.style.transform =
                        `translate(
                            ${x * strength}px,
                            ${y * strength}px
                        )`;

                });

            }
        );


        heroVisual.addEventListener(
            "mouseleave",
            () => {

                const laptop =
                    heroVisual.querySelector(".laptop");


                if (laptop) {

                    laptop.style.transform =
                        "";

                }


                heroVisual
                    .querySelectorAll(".tech-card")
                    .forEach(card => {

                        card.style.transform = "";

                    });

            }
        );

    }


    /* =====================================================
       CUSTOM CURSOR
    ===================================================== */

    const cursorDot =
        document.querySelector(".cursor-dot");

    const cursorRing =
        document.querySelector(".cursor-ring");


    if (
        cursorDot &&
        cursorRing &&
        window.matchMedia("(pointer: fine)").matches
    ) {

        let mouseX = 0;
        let mouseY = 0;

        let ringX = 0;
        let ringY = 0;


        document.addEventListener(
            "mousemove",
            (event) => {

                mouseX = event.clientX;
                mouseY = event.clientY;

                cursorDot.style.left =
                    `${mouseX}px`;

                cursorDot.style.top =
                    `${mouseY}px`;

            }
        );


        const animateCursor = () => {

            ringX +=
                (mouseX - ringX) * 0.13;

            ringY +=
                (mouseY - ringY) * 0.13;


            cursorRing.style.left =
                `${ringX}px`;

            cursorRing.style.top =
                `${ringY}px`;


            requestAnimationFrame(
                animateCursor
            );

        };


        animateCursor();


        const interactiveElements =
            document.querySelectorAll(
                "a, button, .service-card, .project-card, .skill-item"
            );


        interactiveElements.forEach(element => {

            element.addEventListener(
                "mouseenter",
                () => {

                    cursorRing.classList.add(
                        "cursor-hover"
                    );

                }
            );


            element.addEventListener(
                "mouseleave",
                () => {

                    cursorRing.classList.remove(
                        "cursor-hover"
                    );

                }
            );

        });

    }


    /* =====================================================
       ACTIVE NAVIGATION
    ===================================================== */

    const sections =
        document.querySelectorAll(
            "section[id]"
        );

    const navItems =
        document.querySelectorAll(
            ".nav-link"
        );


    const updateActiveNav = () => {

        let current = "";

        sections.forEach(section => {

            const sectionTop =
                section.offsetTop - 160;

            const sectionHeight =
                section.offsetHeight;


            if (
                window.scrollY >= sectionTop &&
                window.scrollY <
                sectionTop + sectionHeight
            ) {

                current =
                    section.getAttribute("id");

            }

        });


        navItems.forEach(link => {

            link.classList.remove("active");

            const href =
                link.getAttribute("href");


            if (href === `#${current}`) {

                link.classList.add("active");

            }

        });

    };


    window.addEventListener(
        "scroll",
        updateActiveNav,
        { passive: true }
    );


    updateActiveNav();


    /* =====================================================
       PROJECT CARD TILT
    ===================================================== */

    const cards =
        document.querySelectorAll(
            ".project-card"
        );


    cards.forEach(card => {

        if (
            !window.matchMedia("(pointer: fine)").matches
        ) {
            return;
        }


        card.addEventListener(
            "mousemove",
            (event) => {

                const rect =
                    card.getBoundingClientRect();


                const x =
                    event.clientX - rect.left;

                const y =
                    event.clientY - rect.top;


                const rotateY =
                    ((x / rect.width) - 0.5) * 3;

                const rotateX =
                    ((y / rect.height) - 0.5) * -3;


                card.style.transform =
                    `perspective(1000px)
                     translateY(-8px)
                     rotateX(${rotateX}deg)
                     rotateY(${rotateY}deg)`;

            }
        );


        card.addEventListener(
            "mouseleave",
            () => {

                card.style.transform = "";

            }
        );

    });


    /* =====================================================
       SMOOTH ANCHOR FALLBACK
    ===================================================== */

    document
        .querySelectorAll('a[href^="#"]')
        .forEach(anchor => {

            anchor.addEventListener(
                "click",
                function(event) {

                    const targetId =
                        this.getAttribute("href");


                    if (
                        targetId === "#" ||
                        !targetId
                    ) {
                        return;
                    }


                    const target =
                        document.querySelector(
                            targetId
                        );


                    if (!target) {
                        return;
                    }


                    event.preventDefault();


                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });

                }
            );

        });


    /* =====================================================
       PHONE / TOUCH SAFETY
    ===================================================== */

    if (
        window.matchMedia("(pointer: coarse)").matches
    ) {

        document.body.classList.add(
            "touch-device"
        );

    }


    /* =====================================================
       PAGE LOADED
    ===================================================== */

    document.body.classList.add(
        "page-loaded"
    );

});
