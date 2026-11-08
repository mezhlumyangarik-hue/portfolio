from flask import Flask, render_template, request

app = Flask(__name__)

COPY = {
    "hy": {
        "title": "Mezhlumyan Web Dev — Թվային փորձառություններ",
        "description": "Ժամանակակից կայքերի մշակում բիզնեսների համար։ Արագ, հարմար և մտածված թվային լուծումներ։",
        "nav": ["Մոտեցում", "Ծառայություններ", "Նախագծեր", "Կապ"],
        "eyebrow": "ԱՆԿԱԽ WEB DEVELOPMENT STUDIO",
        "headline_a": "Թվային գաղափարները",
        "headline_b": "դարձնում եմ իրականություն։",
        "lead": "Ստեղծում եմ առանձնացող կայքեր, որոնք միավորում են ուժեղ դիզայնը, հարմարավետ փորձառությունն ու վստահելի տեխնոլոգիաները։",
        "cta_work": "Դիտել նախագծերը", "cta_contact": "Քննարկել նախագիծը",
        "scroll": "ՍՔՐՈԼ ԱՐԵՔ՝ ԲԱՑԱՀԱՅՏԵԼՈՒ ՀԱՄԱՐ",
        "intro_label": "ՄՈՏԵՑՈՒՄ", "intro_title": "Կայք, որը պարզապես գեղեցիկ չէ։ Այն աշխատում է ձեր բիզնեսի համար։",
        "intro_text": "Յուրաքանչյուր նախագիծ սկսվում է նպատակից։ Հետո կառուցում ենք պարզ կառուցվածք, հիշվող տեսք և հստակ ճանապարհ՝ այցելուից դեպի հաճախորդ։",
        "stats": [["01", "Անհատական մոտեցում"], ["02", "Բոլոր էկրաններին հարմար"], ["03", "Արագ և մտածված կոդ"]],
        "services_label": "ԻՆՉ ԵՆՔ ՍՏԵՂԾՈՒՄ", "services_title": "Թվային լուծումներ՝ ձեր հաջորդ քայլին։",
        "services": [
            ["01", "fa-code", "Կայքերի մշակում", "Բրենդին համապատասխան ներկայացուցչական կայքեր՝ հստակ կառուցվածքով և ժամանակակից ինտերֆեյսով։"],
            ["02", "fa-bag-shopping", "Օնլայն խանութներ", "Ապրանքների կատալոգ, որոնում, զամբյուղ և պատվերների հարմար ընթացք։"],
            ["03", "fa-hotel", "Հյուրանոցներ և ռեստորաններ", "Մենյու, սենյակներ, պատկերասրահ և ուղիղ կապ՝ առանց ավելորդ քայլերի։"],
            ["04", "fa-wand-magic-sparkles", "UI/UX և վերաձևավորում", "Գործող կայքի դիզայնի ու օգտագործման փորձի ամբողջական բարելավում։"]
        ],
        "projects_label": "ԸՆՏՐԱՆԻ ՆԱԽԱԳԾԵՐ", "projects_title": "Աշխատանքներ, որոնք խոսում են իրենց փոխարեն։",
        "view": "Բացել նախագիծը", "process_label": "ԳՈՐԾԸՆԹԱՑ", "process_title": "Գաղափարից մինչև գործարկում։",
        "process": [["Լսել և հասկանալ", "Ուսումնասիրում ենք բիզնեսը, լսարանը և կայքի իրական նպատակը։"], ["Նախագծել", "Ստեղծում ենք կառուցվածքը, տեսողական լեզուն և ինտերակտիվության տրամաբանությունը։"], ["Կառուցել և ստուգել", "Գրում ենք կոդը, ստուգում բոլոր էկրաններին և շտկում մանրուքները։"], ["Գործարկել", "Հրապարակում ենք կայքը և օգնում հաջորդ քայլերում։"]],
        "stack_label": "ՏԵԽՆՈԼՈԳԻԱՆԵՐ", "stack_title": "Ճիշտ գործիքը՝ ճիշտ խնդրի համար։",
        "contact_label": "ՍԿՍԵՆՔ", "contact_title": "Ունե՞ք գաղափար։ Եկեք այն դարձնենք կայք։",
        "contact_text": "Պատմեք ձեր բիզնեսի և նպատակի մասին։ Կքննարկենք լավագույն լուծումը։",
        "contact_btn": "Գրել WhatsApp-ով", "email": "Ուղարկել էլ․ նամակ",
        "footer": "Ստեղծում ենք թվային փորձառություններ։ Բոլոր իրավունքները պաշտպանված են։"
    },
    "ru": {
        "title": "Mezhlumyan Web Dev — Цифровые впечатления",
        "description": "Разработка современных сайтов для бизнеса. Быстрые, удобные и продуманные цифровые решения.",
        "nav": ["Подход", "Услуги", "Проекты", "Контакты"],
        "eyebrow": "НЕЗАВИСИМАЯ WEB-СТУДИЯ",
        "headline_a": "Цифровые идеи",
        "headline_b": "становятся реальностью.",
        "lead": "Создаю выразительные сайты, объединяющие сильный дизайн, удобный пользовательский опыт и надежные технологии.",
        "cta_work": "Смотреть проекты", "cta_contact": "Обсудить проект",
        "scroll": "ПРОКРУТИТЕ, ЧТОБЫ ОТКРЫТЬ БОЛЬШЕ",
        "intro_label": "ПОДХОД", "intro_title": "Сайт — это не только красота. Он работает на ваш бизнес.",
        "intro_text": "Каждый проект начинается с цели. Затем мы создаем понятную структуру, запоминающийся стиль и простой путь от посетителя к клиенту.",
        "stats": [["01", "Индивидуальный подход"], ["02", "Адаптация под все экраны"], ["03", "Быстрый и продуманный код"]],
        "services_label": "ЧТО МЫ СОЗДАЕМ", "services_title": "Цифровые решения для вашего следующего шага.",
        "services": [
            ["01", "fa-code", "Разработка сайтов", "Имиджевые сайты в стиле бренда с понятной структурой и современным интерфейсом."],
            ["02", "fa-bag-shopping", "Интернет-магазины", "Каталог товаров, поиск, корзина и удобный процесс оформления заказов."],
            ["03", "fa-hotel", "Отели и рестораны", "Меню, номера, галерея и прямая связь без лишних шагов."],
            ["04", "fa-wand-magic-sparkles", "UI/UX и редизайн", "Комплексное улучшение дизайна и пользовательского опыта существующего сайта."]
        ],
        "projects_label": "ИЗБРАННЫЕ ПРОЕКТЫ", "projects_title": "Работы, которые говорят сами за себя.",
        "view": "Открыть проект", "process_label": "ПРОЦЕСС", "process_title": "От идеи до запуска.",
        "process": [["Понять задачу", "Изучаем бизнес, аудиторию и реальную цель сайта."], ["Спроектировать", "Создаем структуру, визуальный язык и логику взаимодействия."], ["Разработать и проверить", "Пишем код, тестируем на разных экранах и исправляем детали."], ["Запустить", "Публикуем сайт и помогаем на следующих этапах."]],
        "stack_label": "ТЕХНОЛОГИИ", "stack_title": "Правильный инструмент для каждой задачи.",
        "contact_label": "НАЧНЕМ", "contact_title": "Есть идея? Давайте превратим ее в сайт.",
        "contact_text": "Расскажите о своем бизнесе и цели. Вместе обсудим лучшее решение.",
        "contact_btn": "Написать в WhatsApp", "email": "Написать на почту",
        "footer": "Создаем цифровые впечатления. Все права защищены."
    },
    "en": {
        "title": "Mezhlumyan Web Dev — Digital experiences",
        "description": "Modern website development for businesses. Fast, useful and thoughtful digital solutions.",
        "nav": ["Approach", "Services", "Projects", "Contact"],
        "eyebrow": "INDEPENDENT WEB DEVELOPMENT STUDIO",
        "headline_a": "Digital ideas",
        "headline_b": "made tangible.",
        "lead": "I build distinctive websites combining thoughtful design, seamless experiences and reliable technology.",
        "cta_work": "Explore projects", "cta_contact": "Start a project",
        "scroll": "SCROLL TO EXPLORE",
        "intro_label": "THE APPROACH", "intro_title": "More than a beautiful website. A digital tool built for your business.",
        "intro_text": "Every project starts with a purpose. We shape a clear structure, a memorable visual language and a smooth path from visitor to customer.",
        "stats": [["01", "A tailored approach"], ["02", "Made for every screen"], ["03", "Fast, thoughtful code"]],
        "services_label": "WHAT WE CREATE", "services_title": "Digital solutions for what comes next.",
        "services": [
            ["01", "fa-code", "Website development", "Brand-led websites with clear structure and a contemporary interface."],
            ["02", "fa-bag-shopping", "E-commerce", "Product catalogs, search, shopping carts and a seamless ordering flow."],
            ["03", "fa-hotel", "Hospitality websites", "Menus, rooms, galleries and direct contact without unnecessary steps."],
            ["04", "fa-wand-magic-sparkles", "UI/UX & redesign", "A complete refresh of your website’s visual design and user experience."]
        ],
        "projects_label": "SELECTED PROJECTS", "projects_title": "Work that speaks for itself.",
        "view": "View live project", "process_label": "THE PROCESS", "process_title": "From first thought to launch.",
        "process": [["Discover", "We learn about your business, audience and the real purpose of the website."], ["Design", "We shape the structure, visual language and interaction logic."], ["Build & refine", "We write the code, test across screens and polish the details."], ["Launch", "We publish the website and support the next steps."]],
        "stack_label": "TECHNOLOGY", "stack_title": "The right tool for the right challenge.",
        "contact_label": "LET'S BEGIN", "contact_title": "Have an idea? Let's turn it into a website.",
        "contact_text": "Tell me about your business and goals. We’ll discuss the right solution.",
        "contact_btn": "Message on WhatsApp", "email": "Send an email",
        "footer": "Creating digital experiences. All rights reserved."
    }
}

PROJECTS = [
    {"title":"Imperial Gold","type":"E-commerce / Luxury","desc":{"hy":"Պրեմիում զարդերի և ժամացույցների օնլայն խանութ։","ru":"Интернет-магазин премиальных украшений и часов.","en":"A premium online store for jewelry and watches."},"url":"https://imperial-gold-livid.vercel.app/","tone":"gold","number":"01"},
    {"title":"TechPulse Store","type":"E-commerce / Technology","desc":{"hy":"Տեխնիկայի խանութ՝ կատալոգով, որոնմամբ և զամբյուղով։","ru":"Магазин техники с каталогом, поиском и корзиной.","en":"An electronics store with catalog, search and cart."},"url":"https://techpulse-store-0.vercel.app/","tone":"tech","number":"02"},
    {"title":"Royal Ararat Hotel","type":"Hospitality / Booking","desc":{"hy":"Հյուրանոցի կայք՝ սենյակների ներկայացմամբ և ամրագրմամբ։","ru":"Сайт отеля с презентацией номеров и бронированием.","en":"A hotel website with room presentation and booking."},"url":"https://hotel-demo-iota-tan.vercel.app/","tone":"hotel","number":"03"},
    {"title":"Royal Ararat Restaurant","type":"Hospitality / Ordering","desc":{"hy":"Ռեստորանի կայք՝ մենյուով և օնլայն պատվերով։","ru":"Сайт ресторана с меню и онлайн-заказом.","en":"A restaurant website with menu and online ordering."},"url":"https://restaurant-demo-m.vercel.app/","tone":"food","number":"04"},
    {"title":"Tevosyan Furniture","type":"E-commerce / Furniture","desc":{"hy":"Կահույքի օնլայն կատալոգ՝ կատեգորիաներով և պատվերով։","ru":"Каталог мебели с категориями и оформлением заказа.","en":"A furniture catalog with categories and ordering."},"url":"https://tevosyan-furniture.vercel.app/","tone":"furniture","number":"05"}
]

@app.route("/")
def home():
    lang = request.args.get("lang", "hy")
    if lang not in COPY:
        lang = "hy"
    return render_template("index.html", c=COPY[lang], lang=lang, projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)
