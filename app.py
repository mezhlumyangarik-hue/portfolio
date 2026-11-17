import os
import secrets
from flask import Flask, render_template, request, make_response

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(32))

SUPPORTED_LANGUAGES = ("hy", "ru", "en")
DEFAULT_LANGUAGE = "hy"

PROJECTS = [
    {
        "number": "01",
        "title": "Imperial Gold",
        "tone": "gold",
        "icon": "fa-gem",
        "badge": "E-COMMERCE",
        "url": "https://imperial-gold-livid.vercel.app/",
        "type": "ՕՆԼԱՅՆ ԽԱՆՈՒԹ",
        "desc": {
            "hy": "Պրեմիում զարդերի օնլայն խանութ՝ հարմար կատալոգով, արագ պատվերով և ժամանակակից դիզայնով։",
            "ru": "Премиум интернет-магазин ювелирных изделий с удобным каталогом и быстрым заказом.",
            "en": "Premium jewelry e-commerce store with a sleek catalog and instant ordering."
        }
    },
    {
        "number": "02",
        "title": "ROYAL Ararat Hotel",
        "tone": "hotel",
        "icon": "fa-hotel",
        "badge": "BOOKING",
        "url": "https://hotel-demo-iota-tan.vercel.app/",
        "type": "ՀՅՈՒՐԱՆՈՑ ԵՎ ԱՄՐԱԳՐՈՒՄ",
        "desc": {
            "hy": "Հյուրանոցային համալիրի ներկայացուցչական կայք՝ սենյակների 3D տուրով և ուղիղ ամրագրմամբ։",
            "ru": "Представительский сайт гостиничного комплекса с обзором номеров и прямым бронированием.",
            "en": "Hospitality website featuring room showcases and direct booking integration."
        }
    },
    {
        "number": "03",
        "title": "ROYAL ARARAT",
        "tone": "food",
        "icon": "fa-utensils",
        "badge": "QR MENU & DELIVERY",
        "url": "https://restaurant-demo-m.vercel.app/",
        "type": "ՌԵՍՏՈՐԱՆ ԵՎ ԱՌԱՔՈՒՄ",
        "desc": {
            "hy": "Արագ թվային մենյու և առաքման համակարգ՝ տեղական ռեստորանների ու սրճարանների համար։",
            "ru": "Быстрое цифровое меню и система доставки для местных ресторанов и кафе.",
            "en": "Fast digital menu and delivery platform tailored for local restaurants and cafes."
        }
    },
    {
        "number": "04",
        "title": "TECHPULSE ARMENIA",
        "tone": "tech",
        "icon": "fa-microchip",
        "badge": "CATALOG",
        "url": "https://techpulse-store-0.vercel.app/",
        "type": "ՏԵԽՆԻԿԱՅԻ ԽԱՆՈՒԹ",
        "desc": {
            "hy": "Էլեկտրոնիկայի խանութի հարթակ՝ ֆիլտրերով, զեղչերի համակարգով և WhatsApp պատվերով։",
            "ru": "Платформа магазина электроники с умными фильтрами, скидками и заказом в WhatsApp.",
            "en": "Electronics store platform with smart filtering, promos, and WhatsApp checkout."
        }
    },
    {
        "number": "05",
        "title": "Tevosyan Furniture",
        "tone": "furniture",
        "icon": "fa-couch",
        "badge": "SHOWROOM & CATALOG",
        "url": "#",
        "type": "ԿԱՀՈՒՅՔԻ ԱՐՏԱԴՐՈՒԹՅՈՒՆ",
        "desc": {
            "hy": "Ժամանակակից կահույքի արտադրամասի պրեմիում կայք՝ տեսականու ցուցադրությամբ և պատվերի հնարավորությամբ։",
            "ru": "Премиум-сайт мебельного производства с демонстрацией ассортимента и возможностью заказа.",
            "en": "Modern furniture manufacturing showcase website with catalog and custom order options."
        }
    }
]

COPY = {
    "hy": {
        "title": "Mezhlumyan Web Dev — Կայքերի Մշակում Գորիսում և ողջ Հայաստանում",
        "description": "Պրեմիում կայքերի և օնլայն խանութների ստեղծում բիզնեսների համար։ Արագ, ապահով և վաճառող թվային լուծումներ։",
        "nav": ["Մոտեցում", "Ծառայություններ", "Նախագծեր", "Կապ"],
        "eyebrow": "GORIS • SYUNIK • ARMENIA",
        "headline_a": "Ստեղծում ենք կայքեր,",
        "headline_b": "որոնք բերում են հաճախորդներ։",
        "lead": "Գորիսի խանութներից մինչև խոշոր բրենդներ․ մշակում ենք գերարագ, ժամանակակից և ապահով կայքեր, որոնք առանձնանում են շուկայում։",
        "cta_work": "Դիտել աշխատանքները",
        "cta_contact": "Պատվիրել կայք",
        "promo_badge": "ՀԱՏՈՒԿ ԱՌԱՋԱՐԿ ԳՈՐԻՍԻ ԵՎ ՍՅՈՒՆԻՔԻ ԲԻԶՆԵՍՆԵՐԻՆ",
        "promo_title": "Ունե՞ք խանութ, սրճարան կամ բիզնես։ Ստացեք Ձեր կայքը 5-7 օրում։",
        "promo_btn": "Անվճար խորհրդատվություն",
        "scroll": "ԻՋԵՔ ՆԵՐՔԵՎ",
        "intro_label": "ՄԵՐ ՄՈՏԵՑՈՒՄԸ",
        "intro_title": "Կայքը պարզապես էջ չէ։ Այն Ձեր 24/7 աշխատող լավագույն վաճառողն է։",
        "intro_text": "Մենք չենք օգտագործում հնացած շաբլոններ։ Յուրաքանչյուր կայք կառուցվում է զրոյից՝ հաշվի առնելով Ձեր բիզնեսի առանձնահատկությունները, արագությունը և անվտանգությունը։",
        "stats": [
            ["99%", "Արագություն և օպտիմալացում"],
            ["24/7", "Անխափան և ապահով աշխատանք"],
            ["5-7 օր", "Արագ գործարկում"],
        ],
        "services_label": "ԾԱՌԱՅՈՒԹՅՈՒՆՆԵՐ",
        "services_title": "Ամեն ինչ՝ Ձեր բիզնեսը օնլայն տեղափոխելու համար։",
        "services": [
            ["01", "fa-store", "Օնլայն Խանութներ (E-Commerce)", "Խանութների համար՝ ապրանքների ցուցադրում, գներ, զամբյուղ և 1 քլիքով պատվեր WhatsApp-ով կամ զանգով։", "Ամենապահանջվածը"],
            ["02", "fa-laptop-code", "Բիզնես և Բրենդային Կայքեր", "Ընկերությունների, ծառայությունների և մասնագետների համար՝ վստահություն ներշնչող պրեմիում դիզայնով։", "Պրեմիում"],
            ["03", "fa-utensils", "Հյուրանոցներ, Սրճարաններ, QR Մենյու", "Առանց հավելված ներբեռնելու՝ հաճախորդը սկանավորում է QR-ը, տեսնում մենյուն կամ ամրագրում սենյակ։", "Արագ լուծում"],
            ["04", "fa-shield-halved", "UI/UX Թարմացում և Անվտանգություն", "Հին կայքերի ամբողջական վերափոխում, արագացում, SSL պաշտպանություն և SEO առաջխաղացում։", "Թարմացում"],
        ],
        "projects_label": "ՊՈՐՏՖՈԼԻՈ",
        "projects_title": "Նախագծեր, որոնք ստեղծված են արդյունքի համար։",
        "process_label": "ԻՆՉՊԵՍ ԵՆՔ ԱՇԽԱՏՈՒՄ",
        "process_title": "4 պարզ քայլ՝ դեպի Ձեր նոր կայքը։",
        "process": [
            ["Քննարկում", "Ծանոթանում ենք Ձեր բիզնեսին, խանութին կամ գաղափարին և որոշում լավագույն կառուցվածքը։"],
            ["Դիզայն և Նախատիպ", "Ստեղծում ենք ժամանակակից, աչք շոյող և հարմարավետ տեսք՝ բոլոր հեռախոսների համար։"],
            ["Ծրագրավորում և Պաշտպանություն", "Գրում ենք մաքուր, գերարագ և պաշտպանված կոդ՝ ժամանակակից տեխնոլոգիաներով։"],
            ["Գործարկում և Աջակցություն", "Միացնում ենք դոմենը, սովորեցնում կառավարել կայքը և մնում ենք կապի մեջ։"],
        ],
        "stack_label": "ՏԵԽՆՈԼՈԳԻԱՆԵՐ",
        "stack_title": "Աշխատում ենք ամենաարդիական գործիքներով։",
        "contact_label": "ՍԿՍԵՆՔ ՀԻՄԱ",
        "contact_title": "Պատրա՞ստ եք ավելացնել Ձեր պատվերները։",
        "contact_text": "Գրեք մեզ հենց հիմա WhatsApp-ով կամ զանգահարեք։ Կքննարկենք Ձեր կայքի տարբերակը անվճար։",
        "contact_btn": "Գրել WhatsApp-ով",
        "call_btn": "Զանգահարել հիմա",
        "modal_title": "Արագ Պատվերի Հայտ",
        "modal_sub": "Լրացրեք տվյալները, և մենք կկապվենք Ձեզ հետ 15 րոպեում։",
        "modal_name": "Ձեր անունը կամ խանութի անվանումը",
        "modal_phone": "Հեռախոսահամար / Կոնտակտ",
        "modal_service": "Ծառայություն",
        "modal_send": "Ուղարկել WhatsApp-ով",
        "footer": "Բոլոր իրավունքները պաշտպանված են։ Ստեղծված է Գորիսում ❤️",
    },
    "ru": {
        "title": "Mezhlumyan Web Dev — Разработка современных сайтов",
        "description": "Создание быстрых, безопасных и продающих сайтов и интернет-магазинов для бизнеса.",
        "nav": ["Подход", "Услуги", "Проекты", "Контакты"],
        "eyebrow": "GORIS • SYUNIK • ARMENIA",
        "headline_a": "Создаем сайты,",
        "headline_b": "которые приводят клиентов.",
        "lead": "От локальных магазинов до крупных брендов: разрабатываем сверхбыстрые, современные и защищенные сайты.",
        "cta_work": "Смотреть работы",
        "cta_contact": "Заказать сайт",
        "promo_badge": "СПЕЦИАЛЬНОЕ ПРЕДЛОЖЕНИЕ ДЛЯ БИЗНЕСА",
        "promo_title": "Есть магазин, кафе или бизнес? Запустим ваш сайт за 5–7 дней.",
        "promo_btn": "Бесплатная консультация",
        "scroll": "ЛИСТАЙТЕ ВНИЗ",
        "intro_label": "НАШ ПОДХОД",
        "intro_title": "Сайт — это не просто страница. Это ваш лучший продавец 24/7.",
        "intro_text": "Мы не используем устаревшие шаблоны. Каждый сайт создается с нуля с упором на скорость, дизайн и безопасность.",
        "stats": [
            ["99%", "Скорость и оптимизация"],
            ["24/7", "Надежная и защищенная работа"],
            ["5-7 дней", "Быстрый запуск"],
        ],
        "services_label": "УСЛУГИ",
        "services_title": "Всё для перевода вашего бизнеса в онлайн.",
        "services": [
            ["01", "fa-store", "Интернет-магазины", "Каталог товаров, цены, корзина и быстрый заказ в 1 клик через WhatsApp или звонок.", "Хит продаж"],
            ["02", "fa-laptop-code", "Бизнес и Брендовые сайты", "Для компаний и специалистов — премиальный дизайн, вызывающий доверие клиентов.", "Премиум"],
            ["03", "fa-utensils", "Отели, Кафе и QR-меню", "Без скачивания приложений: клиент сканирует QR, смотрит меню или бронирует номер.", "Быстро"],
            ["04", "fa-shield-halved", "Редизайн и Безопасность", "Полное обновление старых сайтов, ускорение загрузки, SSL-защита и SEO.", "Апгрейд"],
        ],
        "projects_label": "ПОРТФОЛИО",
        "projects_title": "Проекты, созданные для результата.",
        "process_label": "ПРОЦЕСС",
        "process_title": "4 простых шага к вашему новому сайту.",
        "process": [
            ["Обсуждение", "Изучаем ваш бизнес, магазин или идею и подбираем лучшую структуру."],
            ["Дизайн и Прототип", "Создаем современный, стильный и удобный интерфейс для всех смартфонов."],
            ["Разработка и Защита", "Пишем чистый, сверхбыстрый и защищенный код на современных технологиях."],
            ["Запуск и Поддержка", "Подключаем домен, обучаем управлению и остаемся на связи."],
        ],
        "stack_label": "ТЕХНОЛОГИИ",
        "stack_title": "Используем самые передовые инструменты.",
        "contact_label": "НАЧНЕМ СЕЙЧАС",
        "contact_title": "Готовы увеличить количество заказов?",
        "contact_text": "Напишите нам прямо сейчас в WhatsApp или позвоните. Бесплатно обсудим ваш проект.",
        "contact_btn": "Написать в WhatsApp",
        "call_btn": "Позвонить сейчас",
        "modal_title": "Быстрая заявка",
        "modal_sub": "Заполните данные, и мы свяжемся с вами в течение 15 минут.",
        "modal_name": "Ваше имя или название магазина",
        "modal_phone": "Номер телефона / Контакт",
        "modal_service": "Услуга",
        "modal_send": "Отправить в WhatsApp",
        "footer": "Все права защищены. Создано в Горисе ❤️",
    },
    "en": {
        "title": "Mezhlumyan Web Dev — High-Converting Websites",
        "description": "Custom, ultra-fast, and secure websites and e-commerce stores built to grow your business.",
        "nav": ["Approach", "Services", "Projects", "Contact"],
        "eyebrow": "GORIS • SYUNIK • ARMENIA",
        "headline_a": "We build websites",
        "headline_b": "that bring real clients.",
        "lead": "From local retail stores to growing brands: we craft ultra-fast, modern, and secure digital experiences that stand out.",
        "cta_work": "View Projects",
        "cta_contact": "Order a Website",
        "promo_badge": "SPECIAL OFFER FOR LOCAL & REGIONAL BUSINESSES",
        "promo_title": "Own a shop, cafe, or business? Launch your website in 5–7 days.",
        "promo_btn": "Free Consultation",
        "scroll": "SCROLL TO EXPLORE",
        "intro_label": "OUR APPROACH",
        "intro_title": "A website isn't just a page. It's your best 24/7 sales representative.",
        "intro_text": "No bloated templates. Every project is engineered from scratch focusing on speed, security, and converting visitors into buyers.",
        "stats": [
            ["99%", "Speed & Optimization"],
            ["24/7", "Secure & Reliable Uptime"],
            ["5-7 Days", "Rapid Launch"],
        ],
        "services_label": "SERVICES",
        "services_title": "Everything you need to take your business online.",
        "services": [
            ["01", "fa-store", "E-Commerce & Online Stores", "Product showcase, pricing, cart, and 1-click ordering via WhatsApp or direct call.", "Most Popular"],
            ["02", "fa-laptop-code", "Business & Brand Websites", "For companies and professionals — high-trust premium design that converts.", "Premium"],
            ["03", "fa-utensils", "Hotels, Cafes & QR Menus", "No app required: guests scan a QR code to browse menus or book rooms instantly.", "Fast Setup"],
            ["04", "fa-shield-halved", "UI/UX Redesign & Security", "Complete overhaul of outdated sites, speed boost, SSL encryption, and SEO.", "Upgrade"],
        ],
        "projects_label": "PORTFOLIO",
        "projects_title": "Selected works engineered for results.",
        "process_label": "PROCESS",
        "process_title": "4 simple steps to your new website.",
        "process": [
            ["Discovery", "We learn about your business, shop, or idea and map out the best structure."],
            ["Design & Prototype", "We craft a modern, eye-catching interface tailored for mobile and desktop."],
            ["Development & Security", "We write clean, ultra-fast, and secure code using modern web technologies."],
            ["Launch & Support", "We connect your domain, guide you through management, and provide ongoing support."],
        ],
        "stack_label": "TECH STACK",
        "stack_title": "Powered by modern, reliable technologies.",
        "contact_label": "LET'S START",
        "contact_title": "Ready to multiply your orders?",
        "contact_text": "Message us on WhatsApp or call now for a free consultation on your future website.",
        "contact_btn": "Message on WhatsApp",
        "call_btn": "Call Now",
        "modal_title": "Quick Order Request",
        "modal_sub": "Fill in your details and we will reach out within 15 minutes.",
        "modal_name": "Your Name or Shop Name",
        "modal_phone": "Phone Number / Contact",
        "modal_service": "Service",
        "modal_send": "Send via WhatsApp",
        "footer": "All rights reserved. Crafted in Goris ❤️",
    }
}

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
        "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
        "img-src 'self' data: https:; "
        "connect-src 'self';"
    )
    return response

@app.route("/")
def index():
    raw_lang = request.args.get("lang", DEFAULT_LANGUAGE).lower().strip()
    lang = raw_lang if raw_lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE
    resp = make_response(render_template(
        "index.html",
        lang=lang,
        c=COPY[lang],
        projects=PROJECTS
    ))
    return resp

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
