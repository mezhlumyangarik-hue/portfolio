from flask import Flask, render_template, request

app = Flask(__name__)

TRANSLATIONS = {
    'hy': {
        'nav_about': 'Իմ մասին',
        'nav_services': 'Ծառայություններ',
        'nav_projects': 'Պորտֆոլիո',
        'nav_contact': 'Կապ',
        'nav_cta': 'Պատվիրել',
        'hero_badge': '✨ Full-Stack Web Developer 2026',
        'hero_title_1': 'Ստեղծում եմ',
        'hero_title_2': 'Բոմբ Կայքեր',
        'hero_desc': 'Ultra-fast, modern և high-converting կայքեր բիզնեսի, հյուրատների ու օնլայն խանութների համար:',
        'hero_btn_primary': 'Կապնվել հիմա',
        'hero_btn_secondary': 'Տեսնել նախագծերը',
        'about_sub': 'Ով եմ ես',
        'about_title': 'Գարիկ Մեժլումյան | Web Developer',
        'about_text': 'Ստեղծում եմ 100% ադապտիվ, Google SEO-օպտիմալացված և ակնթարթային արագությամբ աշխատող կայքեր: Իմ նպատակն է ձեր բիզնեսին բերել ռեալ հաճախորդներ:',
        'services_sub': 'Լուծումներ',
        'services_title': 'Ինչ կարող եմ անել',
        'srv1_title': 'Հյուրատների Կայքեր',
        'srv1_desc': 'Direct Booking համակարգեր՝ 0% միջնորդավճարով:',
        'srv2_title': 'E-Commerce Խանութներ',
        'srv2_desc': 'Արագ կատալոգներ, զամբյուղ և օնլայն պատվերներ:',
        'srv3_title': 'Բիզնես Վիզիտկաներ',
        'srv3_desc': 'Էլեգանտ ներկայացուցչական կայքեր բոլոր սարքերի համար:',
        'projects_sub': 'Պորտֆոլիո',
        'projects_title': 'Իմ Նախագծերը',
        'skills_sub': 'Stack',
        'skills_title': 'Տեխնոլոգիաներ',
        'contact_sub': 'Կապ',
        'contact_title': 'Քննարկենք Ձեր Պրոյեկտը',
        'contact_desc': 'Ունե՞ք հարցեր: Գրեք կամ զանգահարեք հենց հիմա:',
        'call_now': 'Զանգահարել',
        'email_us': 'Էլ. Փոստ',
        'footer_rights': 'Բոլոր իրավունքները պաշտպանված են:'
    },

    'ru': {
        'nav_about': 'О мне',
        'nav_services': 'Услуги',
        'nav_projects': 'Портфолио',
        'nav_contact': 'Контакты',
        'nav_cta': 'Заказать',
        'hero_badge': '✨ Full-Stack Web Developer 2026',
        'hero_title_1': 'Создаю',
        'hero_title_2': 'Бомбические Сайты',
        'hero_desc': 'Ultra-fast, современные и продающие сайты для бизнеса, отелей и интернет-магазинов.',
        'hero_btn_primary': 'Связаться сейчас',
        'hero_btn_secondary': 'Смотреть работы',
        'about_sub': 'Кто я',
        'about_title': 'Гарик Межлумян | Web Developer',
        'about_text': 'Разрабатываю 100% адаптивные, SEO-оптимизированные и сверхбыстрые сайты, которые приносят реальную прибыль вашему бизнесу.',
        'services_sub': 'Услуги',
        'services_title': 'Что я предлагаю',
        'srv1_title': 'Сайты для Отелей',
        'srv1_desc': 'Прямое бронирование без комиссий третьим лицам.',
        'srv2_title': 'E-Commerce Магазины',
        'srv2_desc': 'Удобные каталоги, корзина и прием онлайн-заказов.',
        'srv3_title': 'Бизнес Визитки',
        'srv3_desc': 'Элегантные сайты для презентации вашего бренда.',
        'projects_sub': 'Портфолио',
        'projects_title': 'Мои Проекты',
        'skills_sub': 'Стек',
        'skills_title': 'Технологии',
        'contact_sub': 'Контакты',
        'contact_title': 'Обсудим Ваш Проект',
        'contact_desc': 'Есть вопросы? Свяжитесь со мной прямо сейчас!',
        'call_now': 'Позвонить',
        'email_us': 'Эл. почта',
        'footer_rights': 'Все права защищены.'
    },

    'en': {
        'nav_about': 'About',
        'nav_services': 'Services',
        'nav_projects': 'Portfolio',
        'nav_contact': 'Contact',
        'nav_cta': 'Get Started',
        'hero_badge': '✨ Full-Stack Web Developer 2026',
        'hero_title_1': 'Building High Impact',
        'hero_title_2': 'Modern Websites',
        'hero_desc': 'Ultra-fast, modern, and high-converting websites for businesses, guest houses, and e-commerce stores.',
        'hero_btn_primary': 'Contact Now',
        'hero_btn_secondary': 'View Works',
        'about_sub': 'About Me',
        'about_title': 'Garik Mezhlumyan | Web Developer',
        'about_text': 'Specialized in building fully responsive, SEO-optimized, and lightning-fast websites engineered to turn visitors into real customers.',
        'services_sub': 'Solutions',
        'services_title': 'What I Offer',
        'srv1_title': 'Hotel & Guest House Sites',
        'srv1_desc': 'Direct booking engines with 0% third-party commission.',
        'srv2_title': 'E-Commerce Stores',
        'srv2_desc': 'Sleek product catalogs and instant online orders.',
        'srv3_title': 'Business Websites',
        'srv3_desc': 'High-converting representation sites to elevate your brand.',
        'projects_sub': 'Portfolio',
        'projects_title': 'Featured Works',
        'skills_sub': 'Stack',
        'skills_title': 'Technologies',
        'contact_sub': 'Contact',
        'contact_title': "Let's Work Together",
        'contact_desc': 'Have a project in mind? Get in touch today!',
        'call_now': 'Call Now',
        'email_us': 'Send Email',
        'footer_rights': 'All rights reserved.'
    }
}


PROJECTS_DATA = {
    'hy': [
        {
            'title': 'Imperial Gold',
            'description': 'Բարձրակարգ ոսկյա զարդերի և ադամանդյա ժամացույցների E-Commerce կայք՝ հավաքածուով, ապրանքների էջերով, զամբյուղով և պատվերի համակարգով:',
            'tags': ['E-Commerce', 'JavaScript', 'UI/UX', 'Responsive'],
            'live_url': 'https://imperial-gold-livid.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://imperial-gold-livid.vercel.app/'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Ժամանակակից տեխնիկայի E-Commerce խանութ՝ ապրանքների կատալոգով, որոնմամբ, զամբյուղով և օնլայն գնումների հնարավորությամբ:',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://techpulse-store-0.vercel.app/'
        },
        {
            'title': 'Royal Ararat Hotel',
            'description': 'Ժամանակակից հյուրանոցի կայք՝ սենյակների ներկայացմամբ, ամրագրման համակարգով և հյուրերի համար հարմարավետ ինտերֆեյսով:',
            'tags': ['Hotel', 'Booking', 'JavaScript', 'Responsive'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://hotel-demo-iota-tan.vercel.app/'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Դռների վաճառքի ժամանակակից կայք՝ ապրանքների ներկայացմամբ, գնով և կապի/պատվերի հնարավորությամբ:',
            'tags': ['Business', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://kars-legacy.onrender.com/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://kars-legacy.onrender.com/'
        },
        {
            'title': 'Royal Ararat Restaurant',
            'description': 'Պրեմիում ռեստորանի կայք՝ մենյուով, ուտեստների քարտերով, զամբյուղով և օնլայն պատվերի համակարգով:',
            'tags': ['Restaurant', 'E-Commerce', 'JavaScript', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://restaurant-demo-m.vercel.app/'
        },
        {
            'title': 'Tevosyan Furniture',
            'description': 'Ժամանակակից կահույքի E-Commerce կայք՝ կատալոգով, կատեգորիաներով, զամբյուղով և օնլայն պատվերի համակարգով:',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://tevosyan-furniture.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://tevosyan-furniture.vercel.app/'
        }
    ],

    'ru': [
        {
            'title': 'Imperial Gold',
            'description': 'Премиальный E-Commerce сайт ювелирных изделий и часов с каталогом, товарами, корзиной и системой заказа.',
            'tags': ['E-Commerce', 'JavaScript', 'UI/UX', 'Responsive'],
            'live_url': 'https://imperial-gold-livid.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://imperial-gold-livid.vercel.app/'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Современный E-Commerce магазин техники с каталогом, поиском, корзиной и системой онлайн-покупок.',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://techpulse-store-0.vercel.app/'
        },
        {
            'title': 'Royal Ararat Hotel',
            'description': 'Современный сайт отеля с презентацией номеров и системой бронирования.',
            'tags': ['Hotel', 'Booking', 'JavaScript', 'Responsive'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://hotel-demo-iota-tan.vercel.app/'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Современный сайт для продажи дверей с презентацией товаров, ценами и возможностью связи.',
            'tags': ['Business', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://kars-legacy.onrender.com/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://kars-legacy.onrender.com/'
        },
        {
            'title': 'Royal Ararat Restaurant',
            'description': 'Премиальный сайт ресторана с меню, карточками блюд, корзиной и системой онлайн-заказа.',
            'tags': ['Restaurant', 'E-Commerce', 'JavaScript', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://restaurant-demo-m.vercel.app/'
        },
        {
            'title': 'Tevosyan Furniture',
            'description': 'Современный мебельный E-Commerce сайт с каталогом, категориями, корзиной и системой онлайн-заказа.',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://tevosyan-furniture.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://tevosyan-furniture.vercel.app/'
        }
    ],

    'en': [
        {
            'title': 'Imperial Gold',
            'description': 'Premium jewelry and luxury watches E-Commerce website with collections, products, cart and ordering system.',
            'tags': ['E-Commerce', 'JavaScript', 'UI/UX', 'Responsive'],
            'live_url': 'https://imperial-gold-livid.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://imperial-gold-livid.vercel.app/'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Modern electronics E-Commerce store with product catalog, search, shopping cart and online purchasing.',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://techpulse-store-0.vercel.app/'
        },
        {
            'title': 'Royal Ararat Hotel',
            'description': 'Modern hotel website with room presentation and booking functionality.',
            'tags': ['Hotel', 'Booking', 'JavaScript', 'Responsive'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://hotel-demo-iota-tan.vercel.app/'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Modern door sales website with product presentation, pricing and contact/order functionality.',
            'tags': ['Business', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://kars-legacy.onrender.com/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://kars-legacy.onrender.com/'
        },
        {
            'title': 'Royal Ararat Restaurant',
            'description': 'Premium restaurant website with menu, food cards, shopping cart and online ordering system.',
            'tags': ['Restaurant', 'E-Commerce', 'JavaScript', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://restaurant-demo-m.vercel.app/'
        },
        {
            'title': 'Tevosyan Furniture',
            'description': 'Modern furniture E-Commerce website with catalog, categories, shopping cart and online ordering system.',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://tevosyan-furniture.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue',
            'preview_url': 'https://image.thum.io/get/width/1200/crop/800/noanimate/https://tevosyan-furniture.vercel.app/'
        }
    ]
}

    'ru': [
        {
            'title': 'Imperial Gold',
            'description': 'Электронный каталог ювелирного салона с презентацией товаров и системой заказов.',
            'tags': ['HTML5/CSS3', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://imperial-gold-livid.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/Imperial-Gold'
        },
        {
            'title': 'TechPulse Store',
            'description': 'Интернет-магазин электроники (E-commerce) с быстрым поиском, корзиной и адаптивным дизайном.',
            'tags': ['Flask', 'HTML5/CSS3', 'JavaScript', 'Responsive'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/techpulse-store'
        },
        {
            'title': 'Hotel Booking Demo',
            'description': 'Современная система бронирования для отелей и гостевых домов.',
            'tags': ['Python', 'Flask', 'UI/UX Design', 'CSS Grid'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/hotel_demo'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Презентационный веб-сайт с плавной анимацией и презентацией наследия.',
            'tags': ['HTML5', 'CSS Animation', 'JavaScript', 'Portfolio'],
            'live_url': 'https://kars-legacy.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/KARS-Legacy'
        },
        {
            'title': 'Royal Ararati Restaurant',
            'description': 'Сайт ресторанного комплекса с цифровым меню (Digital Menu) и бронированием столов.',
            'tags': ['Python', 'Flask', 'HTML/CSS', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/royal-ararati-demo'
        },
        {
            'title': 'Tevosyan Furniture',
            'description': 'Современный E-Commerce сайт мебели с каталогом, категориями, корзиной и системой онлайн-заказа.',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://tevosyan-furniture.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue'
        }
    ],

    'en': [
        {
            'title': 'Imperial Gold',
            'description': 'Luxury jewelry store e-catalog with sleek product showcases and interactive order flows.',
            'tags': ['HTML5/CSS3', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://imperial-gold-livid.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/Imperial-Gold'
        },
        {
            'title': 'TechPulse Store',
            'description': 'E-commerce platform featuring dynamic product list, custom shopping cart and responsive design.',
            'tags': ['Flask', 'HTML5/CSS3', 'JavaScript', 'Responsive'],
            'live_url': 'https://techpulse-store-0.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/techpulse-store'
        },
        {
            'title': 'Hotel Booking Demo',
            'description': 'Direct room reservation system tailored for boutique hotels and local guest houses.',
            'tags': ['Python', 'Flask', 'UI/UX Design', 'CSS Grid'],
            'live_url': 'https://hotel-demo-iota-tan.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/hotel_demo'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Showcase website featuring dynamic scrolling effects, interactive elements, and modern typography.',
            'tags': ['HTML5', 'CSS Animation', 'JavaScript', 'Portfolio'],
            'live_url': 'https://kars-legacy.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/KARS-Legacy'
        },
        {
            'title': 'Royal Ararati Restaurant',
            'description': 'Restaurant web application with Digital Menu showcase and table reservation system.',
            'tags': ['Python', 'Flask', 'HTML/CSS', 'Responsive'],
            'live_url': 'https://restaurant-demo-m.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue/royal-ararati-demo'
        },
        {
            'title': 'Tevosyan Furniture',
            'description': 'Modern furniture E-Commerce website with product catalog, categories, shopping cart and online ordering system.',
            'tags': ['E-Commerce', 'JavaScript', 'Responsive', 'UI/UX'],
            'live_url': 'https://tevosyan-furniture.vercel.app/',
            'github_url': 'https://github.com/mezhlumyangarik-hue'
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

    skills = [
        'HTML5 / CSS3',
        'JavaScript (ES6+)',
        'Python / Flask',
        'Git / GitHub',
        'Responsive Web Design',
        'UI/UX Design',
        'SEO Fundamentals'
    ]

    return render_template(
        'index.html',
        t=t,
        projects=projects,
        skills=skills,
        current_lang=lang
    )


if __name__ == '__main__':
    app.run(debug=True)
