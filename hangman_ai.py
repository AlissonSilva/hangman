from transformers import pipeline
import random
import pandas as pd
from os import system, name

class Screen:
    @staticmethod
    def clear_screen():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    @staticmethod
    def header():
        print('\nBem-vindo(a) ao jogo da forca!')
        print('Adivinha a palavra abaixo: \n')

class Force:
    step = [
        '''
            ------
            |     |
            |     O
            |    \\|/
            |     |
            |    / \\
''',
        '''
            ------
            |     |
            |     O
            |    \\|/
            |     |
            |    / 
''',
        '''
            ------
            |     |
            |     O
            |    \\|/
            |     |
            |     
''',
        '''
            ------
            |     |
            |     O
            |    \\|
            |     |
            |      
''',
        '''
            ------
            |     |
            |     O
            |     |
            |     |
            |      
''',
        '''
            ------
            |     |
            |     O
            |
            |
            |
''',
        '''
            ------
            |     |
            |
            |
            |
            |
''',
    ]

    @staticmethod
    def show(chances):
        return Force.step[chances]

class GeneratorWordsIA:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt-2')

    def generate_words(self,categorie ):
        """Gera palavras e dicas baseadas na categoria."""
        prompt = f"Crie uma palavra e uma dica relacionadas à categoria: {categorie}."
        answers = self.generator(prompt, max_length=50, num_return_sequences=1)
        text_generate = answers[0]['generated_text']

        try:
            words, tip = text_generate.split(':',1)
            return words.strip(), tip.strip()
        except:
            return 'WordGenerate', 'TipGenerate'