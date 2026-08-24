from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Multi-language Content Data
TRANSLATIONS = {
    'hy': {
        'nav_about': 'Իմ մասին',
        'nav_services': 'Ծառայություններ',
        'nav_projects': 'Պրոյեկտներ',
        'nav_contact': 'Կապ',
        'nav_cta': 'Հարցնել գինը',
        'hero_badge': '🟢 Հասանելի է պատվերների համար 2026',
        'hero_title_1': 'Պրոֆեսիոնալ Կայքերի',
        'hero_title_2': 'Պատրաստում Գորիսում',
        'hero_desc': 'Ստեղծում եմ ultra-fast, modern և high-converting կայքեր բիզնեսների, հյուրատների ու օնլայն խանութների համար:',
        'hero_btn_primary': 'Պատվիրել Կայք',
        'hero_btn_secondary': 'Պորտֆոլիո',
        'about_sub': 'Ով եմ ես',
        'about_title': 'Կայքեր, որոնք բերում են ռեալ հաճախորդներ',
        'about_text': 'Ես Web Developer եմ՝ մասնագիտացած բիզնես կայքերի, E-commerce հարթակների և հյուրատների ամրագրման համակարգերի մշակման մեջ: Իմ ստեղծած կայքերն ունեն 100% Mobile Responsive դիզայն, Google SEO-օպտիմալացում և ակնթարթային բեռնման արագություն:',
        'services_sub': 'Ծառայություններ',
        'services_title': 'Ինչ լուծումներ եմ առաջարկում',
        'srv1_title': 'Հյուրատների Կայքեր',
        'srv1_desc': 'Ուղիղ ամրագրման համակարգեր (Direct Booking)՝ առանց Booking.com-ին միջնորդավճար տալու:',
        'srv2_title': 'E-Commerce (Օնլայն Խանութներ)',
        'srv2_desc': 'Ապրանքների ժամանակակից կատալոգներ, զամբյուղ և օնլայն պատվերների ավտոմատ ընդունում:',
        'srv3_title': 'Բիզնես Վիզիտկա Կայքեր',
        'srv3_desc': 'Էլեգանտ ներկայացուցչական կայքեր, գնացուցակներ և ակտիվ կապի կոճակներ:',
        'projects_sub': 'Պորտֆոլիո',
        'projects_title': 'Վերջին Նախագծերը',
        'skills_sub': 'Stack',
        'skills_title': 'Տեխնոլոգիական Գործիքները',
        'contact_sub': 'Կապ',
        'contact_title': 'Քննարկենք Ձեր Պրոյեկտը',
        'contact_desc': 'Ունե՞ք հարցեր կամ ցանկանում եք իմանալ ձեր ապագա կայքի մոտավոր արժեքը: Գրեք կամ զանգահարեք հիմա:',
        'call_now': 'Զանգահարել',
        'email_us': 'Էլ. Փոստ',
        'footer_rights': 'Բոլոր իրավունքները պաշտպանված են:'
    },
    'ru': {
        'nav_about': 'О обо мне',
        'nav_services': 'Услуги',
        'nav_projects': 'Проекты',
        'nav_contact': 'Контакты',
        'nav_cta': 'Узнать цену',
        'hero_badge': '🟢 Доступен для заказов 2026',
        'hero_title_1': 'Профессиональная Разработка',
        'hero_title_2': 'Сайтов в Горисе',
        'hero_desc': 'Создаю ultra-fast, современные и продающие сайты для бизнеса, гостевых домов и интернет-магазинов.',
        'hero_btn_primary': 'Заказать Сайт',
        'hero_btn_secondary': 'Портфолио',
        'about_sub': 'Кто я',
        'about_title': 'Сайты, которые приносят реальных клиентов',
        'about_text': 'Я Web-разработчик, специализирующийся на создании бизнес-сайтов, E-commerce платформ и систем бронирования для отелей. Мои сайты обладают 100% адаптивностью, SEO-оптимизацией и высокой скоростью загрузки.',
        'services_sub': 'Услуги',
        'services_title': 'Что я предлагаю',
        'srv1_title': 'Сайты для Гостевых Домов',
        'srv1_desc': 'Системы прямого бронирования (Direct Booking) без комиссии сайтам-посредникам.',
        'srv2_title': 'E-Commerce (Интернет-Магазины)',
        'srv2_desc': 'Современные каталоги товаров, корзина и автоматическое получение заказов.',
        'srv3_title': 'Бизнес Сайты-Визитки',
        'srv3_desc': 'Элегантные презентационные сайты, прайс-листы и интерактивные кнопки связи.',
        'projects_sub': 'Портфолио',
        'projects_title': 'Последние Проекты',
        'skills_sub': 'Стек',
        'skills_title': 'Технологии и Инструменты',
        'contact_sub': 'Контакты',
        'contact_title': 'Обсудим Ваш Проект',
        'contact_desc': 'Есть вопросы или хотите узнать стоимость будущего сайта? Свяжитесь со мной прямо сейчас.',
        'call_now': 'Позвонить',
        'email_us': 'Эл. почта',
        'footer_rights': 'Все права защищены.'
    },
    'en': {
        'nav_about': 'About',
        'nav_services': 'Services',
        'nav_projects': 'Projects',
        'nav_contact': 'Contact',
        'nav_cta': 'Get a Quote',
        'hero_badge': '🟢 Available for new projects 2026',
        'hero_title_1': 'Professional Web',
        'hero_title_2': 'Development in Goris',
        'hero_desc': 'Building ultra-fast, modern, and high-converting websites for businesses, guest houses, and e-commerce stores.',
        'hero_btn_primary': 'Order a Website',
        'hero_btn_secondary': 'View Portfolio',
        'about_sub': 'About Me',
        'about_title': 'Websites engineered to drive real sales',
        'about_text': 'I am a Web Developer specialized in creating modern business websites, e-commerce solutions, and custom booking engines for guest houses. Every project is optimized for speed, mobile devices, and SEO.',
        'services_sub': 'Services',
        'services_title': 'What I Offer',
        'srv1_title': 'Guest House Websites',
        'srv1_desc': 'Direct booking systems that help you accept reservations with 0% third-party commissions.',
        'srv2_title': 'E-Commerce Stores',
        'srv2_desc': 'Sleek product catalogs, shopping carts, and seamless order management.',
        'srv3_title': 'Business Websites',
        'srv3_desc': 'High-converting portfolio and representative sites designed to elevate your brand.',
        'projects_sub': 'Portfolio',
        'projects_title': 'Featured Projects',
        'skills_sub': 'Stack',
        'skills_title': 'Tech Stack & Tools',
        'contact_sub': 'Contact',
        'contact_title': "Let's Work Together",
        'contact_desc': 'Have a project in mind or need a quick price estimate? Get in touch today!',
        'call_now': 'Call Now',
        'email_us': 'Send Email',
        'footer_rights': 'All rights reserved.'
    }
}

PROJECTS_DATA = {
    'hy': [
        {
            'title': 'imperialgold',
            'description': 'Շքեղ ոսկերչական խանութ-սրահի էլեկտրոնային կատալոգ, ապրանքների ցուցադրություն և օնլայն պատվերների ընդունման ադապտիվ համակարգ:',
            'tags': ['HTML5/CSS3', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://imperialgold.vercel.app',
            'github_url': 'https://github.com/mezhlumyangarik-hue'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Ժամանակակից էլեկտրոնային առևտրի հարթակ (E-commerce)՝ մաքուր, արագ և հարմարավետ ապրանքների կատալոգով:',
            'tags': ['Flask', 'HTML5/CSS3', 'JavaScript', 'Responsive'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/techpulse-store'
        },
        {
            'title': 'Hotel Demo',
            'description': 'Ադապտիվ և սիրուն կայք՝ հատուկ տեղական հյուրատների (Guest Houses) և հյուրանոցների ամրագրումների համար:',
            'tags': ['Python', 'Flask', 'UI/UX Design', 'CSS Grid'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/hotel_demo'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Մշակութային և բիզնես ներկայացուցչական կայք՝ հարուստ տեղեկատվությամբ և սահուն, ժամանակակից անիմացիաներով:',
            'tags': ['HTML5', 'CSS Animation', 'JavaScript', 'Portfolio'],
            'live_url': 'https://kars-legacy.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/KARS-Legacy'
        },
        {
            'title': 'Restaurant (Demo)',
            'description': 'Ռեստորանային համալիրի դեմո կայք՝ թվային մենյուով (Digital Menu) և սեղանների օնլայն ամրագրման համակարգով:',
            'tags': ['Python', 'Flask', 'HTML/CSS', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/royal-ararati-demo'
        }
    ],
    'ru': [
        {
            'title': 'imperialgold',
            'description': 'Электронный каталог ювелирного салона с презентацией товаров и адаптивной системой онлайн-заказов.',
            'tags': ['HTML5/CSS3', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://imperialgold.vercel.app',
            'github_url': 'https://github.com/mezhlumyangarik-hue'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Современная E-commerce платформа с чистым, быстрым и удобным каталогом электроники.',
            'tags': ['Flask', 'HTML5/CSS3', 'JavaScript', 'Responsive'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/techpulse-store'
        },
        {
            'title': 'Hotel Demo',
            'description': 'Адаптивный сайт с системой бронирования специально для гостевых домов и отелей.',
            'tags': ['Python', 'Flask', 'UI/UX Design', 'CSS Grid'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/hotel_demo'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Презентационный веб-сайт с плавной анимацией и богатым информационным блоком.',
            'tags': ['HTML5', 'CSS Animation', 'JavaScript', 'Portfolio'],
            'live_url': 'https://kars-legacy.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/KARS-Legacy'
        },
        {
            'title': 'Restaurant (Demo)',
            'description': 'Демо-сайт ресторана с цифровым меню (Digital Menu) и модулем бронирования столов.',
            'tags': ['Python', 'Flask', 'HTML/CSS', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/royal-ararati-demo'
        }
    ],
    'en': [
        {
            'title': 'imperialgold',
            'description': 'Luxury jewelry store e-catalog featuring elegant product showcases and an online ordering flow.',
            'tags': ['HTML5/CSS3', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://imperialgold.vercel.app',
            'github_url': 'https://github.com/mezhlumyangarik-hue'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Modern E-commerce store featuring a fast, smooth product catalog and responsive interface.',
            'tags': ['Flask', 'HTML5/CSS3', 'JavaScript', 'Responsive'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/techpulse-store'
        },
        {
            'title': 'Hotel Demo',
            'description': 'Responsive website with direct room reservation tools built for local guest houses and boutique hotels.',
            'tags': ['Python', 'Flask', 'UI/UX Design', 'CSS Grid'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/hotel_demo'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Cultural and business showcase platform featuring sleek animations and interactive layouts.',
            'tags': ['HTML5', 'CSS Animation', 'JavaScript', 'Portfolio'],
            'live_url': 'https://kars-legacy.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/KARS-Legacy'
        },
        {
            'title': 'Restaurant (Demo)',
            'description': 'Modern restaurant web platform with a Digital Menu section and online table reservation feature.',
            'tags': ['Python', 'Flask', 'HTML/CSS', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/royal-ararati-demo'
        }
    ]
}

@app.route('/')
def home():
    lang = request.args.get('lang', 'hy')
    if lang not in TRANSLATIONS:
        lang = 'hy'
        
    t = TRANSLATIONS[lang]
    projects = PROJECTS_DATA[lang]
    skills = ['HTML5 / CSS3', 'JavaScript (ES6+)', 'Python / Flask', 'Git / GitHub', 'Responsive Web Design', 'UI/UX Design', 'SEO Fundamentals']
    
    return render_template('index.html', t=t, projects=projects, skills=skills, current_lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
