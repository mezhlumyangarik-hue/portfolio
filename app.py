from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Քո իրական պրոյեկտների թարմացված տվյալները
    projects = [
        {
            'title': 'TechPulse Store',
            'description': 'Ժամանակակից էլեկտրոնային առևտրի հարթակ (E-commerce)՝ մաքուր, արագ և հարմարավետ ապրանքների կատալոգով:',
            'tags': ['Flask', 'HTML5/CSS3', 'JavaScript', 'Responsive'],
            'live_url': 'https://techpulse-store-333.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/techpulse-store'
        },
        {
            'title': 'Hotel Demo',
            'description': 'Ադապտիվ և սիրուն կայք՝ հատուկ տեղական հյուրատների (Guest Houses) և հյուրանոցների ամրագրումների համար:',
            'tags': ['Python', 'Flask', 'UI/UX Design', 'CSS Grid'],
            'live_url': 'https://hotel-demo-wstg.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/hotel_demo'
        },
        {
            'title': 'Kars Legacy',
            'description': 'Մշակութային և բիզնես ներկայացուցչական կայք՝ հարուստ տեղեկատվությամբ և սահուն, ժամանակակից անիմացիաներով:',
            'tags': ['HTML5', 'CSS Animation', 'JavaScript', 'Portfolio'],
            'live_url': 'https://kars-legacy.onrender.com',
            'github_url': 'https://github.com/mezhlumyangarik-hue/KARS-Legacy'
        }
    ]
    
    # Քո հմտությունների ցուցակը
    skills = ['HTML5', 'CSS3 / Grid / Flexbox', 'JavaScript (ES6+)', 'Python / Flask', 'Git / GitHub', 'Responsive Web Design']
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)