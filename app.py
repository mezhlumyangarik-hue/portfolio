import threading
import time
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Ֆունկցիա, որը հետնապլանում (Background) 5 րոպեն մեկ կանչելու է այս կայքը
def self_ping():
    # Սպասում ենք 10 վայրկյան, մինչև սերվերը Render-ում լրիվ միանա
    time.sleep(10)
    while True:
        try:
            # Փոխիր սա հենց ՔՈ ԱՅՍ պորտֆոլիո կայքի իրական Render հղումով
            url = "https://garik-portfolio.onrender.com" 
            response = requests.get(url)
            print(f"--- Self-ping status: {response.status_code} ---")
        except Exception as e:
            print(f"--- Self-ping failed: {e} ---")
        
        # Սպասել 5 րոպե (300 վայրկյան)
        time.sleep(300)

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
        },
        {
            'title': 'Restaurant (Demo)',
            'description': 'Ռեստորանային համալիրի ժամանակակից դեմո կայք՝ պատրաստված Flask-ով։ Ներառում է էլեգանտ գլխավոր էջ, թվային մենյուի (Digital Menu) բաժին և սեղանների օնլայն ամրագրման հարմար համակարգ։',
            'github_url': 'https://github.com/mezhlumyangarik-hue/royal-ararati-demo', 
            'live_url': 'https://restaurant-demo-tb6k.onrender.com/', 
            'tags': ['Python', 'Flask', 'HTML/CSS', 'Responsive Design']
        }
    ]
    
    # Քո հմտությունների ցուցակը
    skills = ['HTML5', 'CSS3 / Grid / Flexbox', 'JavaScript (ES6+)', 'Python / Flask', 'Git / GitHub', 'Responsive Web Design']
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    # Միացնում ենք ավտոմատ արթնացնող ֆունկցիան առանձին thread-ով
    threading.Thread(target=self_ping, daemon=True).start()
    app.run(debug=True)
