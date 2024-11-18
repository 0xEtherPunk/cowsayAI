#!/usr/bin/env python3
from .ai_client import MistralAIClient
from .display_manager import DisplayManager
from .version import VERSION
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="""CowsayAI - AI-powered wisdom generator
        
Get unique insights and perspectives from various domains:
- Programming and Technology
- Philosophy and Stoicism
- Fitness and Psychology
- Crypto and Business
- Art and Modern Tech
- Security and Hacking
and many more...

Updates: 
Run 'git pull' in the cowsayAI directory to get the latest version
Then run 'pip install -e .' if dependencies changed""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--ru', action='store_true',
                      help='Get insights in Russian')
    parser.add_argument('--version', '-v', action='version',
                      version=f'CowsayAI v{VERSION}')
    
    args = parser.parse_args()

    ai_client = MistralAIClient()
    display_manager = DisplayManager()

    # Получаем случайного персонажа для отображения
    character = display_manager.get_random_character()
    
    # Получаем сообщение от AI на выбранном языке
    ai_message = ai_client.get_response('ru' if args.ru else 'en')
    
    # Создаем и отображаем сообщение
    cow_message = display_manager.create_message(character, ai_message)
    display_manager.display_colorized(cow_message)

if __name__ == "__main__":
    main() 