import cowsay
import random
import subprocess

class DisplayManager:
    def __init__(self):
        self.characters = cowsay.char_names

    def get_random_character(self):
        return random.choice(self.characters)

    def create_message(self, character, message):
        return cowsay.get_output_string(character, message)

    def display_colorized(self, text):
        try:
            process = subprocess.Popen(['lolcat'], stdin=subprocess.PIPE, text=True)
            process.communicate(input=text)
        except FileNotFoundError:
            print("lolcat не установлен, выводим без цвета:")
            print(text) 