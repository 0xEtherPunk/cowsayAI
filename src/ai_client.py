import os
import random
from dotenv import load_dotenv
import requests

load_dotenv()

DEFAULT_API_KEY = "vOoGY3RccLs6lbSAbIzQD29IyMHaB4Hb"
API_URL = "https://api.mistral.ai/v1/chat/completions"

class MistralAIClient:
    def __init__(self):
        self.api_key = os.getenv('MISTRAL_API_KEY', DEFAULT_API_KEY)
        
        # Системный промпт с акцентом на эффективные непопулярные факты
        self.system_prompts = {
            'en': """You are a collector of effective but underappreciated knowledge.
                    When given a domain, share ONE practical fact that is:
                    - Highly effective in practice
                    - Not commonly known or used
                    - Immediately applicable
                    
                    Focus on concrete utility rather than theory.
                    Share something that works surprisingly well but few people know about.
                    
                    Keep it within 3-4 lines, each up to 120 characters.
                    Make it specific and actionable.
                    Answer in English. Every fact should feel like a discovered tool.""",
            
            'ru': """Ты собиратель эффективных, но недооцененных знаний.
                    Получив область, поделись ОДНИМ практическим фактом, который:
                    - Высоко эффективен на практике
                    - Не является общеизвестным или общеиспользуемым
                    - Можно применить сразу
                    
                    Фокусируйся на конкретной пользе, а не теории.
                    Поделись чем-то, что работает удивительно хорошо, но мало кто знает.
                    
                    Уложись в 3-4 строки, каждая до 120 символов.
                    Делай это конкретным и применимым.
                    Отвечай на русском. Каждый факт должен ощущаться как найденный инструмент."""
        }
        
        # Расширенные сферы знаний
        self.domains = {
            'en': [
                # Технологии
                "Programming...",
                "AI Technology...",
                "Quantum Computing...",
                "Robotics...",
                "Biotech...",
                "Space Tech...",
                "Cybersecurity...",
                "Web3...",
                "IoT...",
                "AR/VR...",
                
                # Философия и психология
                "Philosophy...",
                "Stoicism...",
                "Psychology...",
                "Neuroscience...",
                "Meditation...",
                "Consciousness...",
                
                # Искусство
                "Modern Art...",
                "Digital Art...",
                "NFT Art...",
                "Generative Art...",
                "Music Production...",
                "Creative Coding...",
                
                # Бизнес и крипта
                "Business...",
                "Crypto...",
                "DeFi...",
                "Startups...",
                "Innovation...",
                "Market Psychology...",
                
                # Здоровье и спорт
                "Fitness...",
                "Nutrition...",
                "Mental Health...",
                "Biohacking...",
                "Sports Science...",
                "Recovery...",
                
                # Наука
                "Physics...",
                "Biology...",
                "Chemistry...",
                "Astronomy...",
                "Mathematics..."
            ],
            'ru': [
                # Технологии
                "Программирование...",
                "ИИ технологии...",
                "Квантовые вычисления...",
                "Робототехника...",
                "Биотехнологии...",
                "Космические технологии...",
                "Кибербезопасность...",
                "Web3...",
                "Интернет вещей...",
                "AR/VR...",
                
                # Философия и психология
                "Философия...",
                "Стоицизм...",
                "Психология...",
                "Нейронаука...",
                "Медитация...",
                "Сознание...",
                
                # Искусство
                "Современное искусство...",
                "Цифровое искусство...",
                "NFT искусство...",
                "Генеративное искусство...",
                "Музыкальное производство...",
                "Креативное программирование...",
                
                # Бизнес и крипта
                "Бизнес...",
                "Крипта...",
                "DeFi...",
                "Стартапы...",
                "Инновации...",
                "Психология рынка...",
                
                # Здоровье и спорт
                "Фитнес...",
                "Питание...",
                "Ментальное здоровье...",
                "Биохакинг...",
                "Спортивная наука...",
                "Восстановление...",
                
                # Наука
                "Физика...",
                "Биология...",
                "Химия...",
                "Астрономия...",
                "Мат��матика..."
            ]
        }

    def get_response(self, lang_param='en'):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        lang = 'ru' if lang_param == 'ru' else 'en'
        domain = random.choice(self.domains[lang])
        
        data = {
            "model": "mistral-small",
            "messages": [
                {"role": "system", "content": self.system_prompts[lang]},
                {"role": "user", "content": domain}
            ],
            "max_tokens": 200,
            "temperature": 1
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"{'Ошибка' if lang == 'ru' else 'Error'}: {str(e)}" 