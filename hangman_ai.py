# from openai import OpenAI
import openai
import random
import pandas as pd
from os import system, name,getenv

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
        # Configura a chave da API
        self.client = openai.OpenAI(
            api_key = getenv('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'),
        )

    def generate_words(self, category):
        """Gera palavras e dicas baseadas na categoria."""
        prompt = f"Crie uma palavra e uma dica relacionadas à categoria: {category}."
        
        try:

            # Faz a requisição ao modelo de chat
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Ou "gpt-4"
                messages=[
                    {"role": "system", "content": "Você é um gerador de palavras e dicas."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50  # Limite de tokens na resposta
            )

            # Extrai a resposta do modelo
            text_generate = response["choices"][0]["message"]["content"].strip()

            # Separa palavra e dica com base em ":"
            words, tip = text_generate.split(":", 1)
            return words.strip(), tip.strip()

        except Exception as e:
            # Tratamento de erros
            print(f"Erro ao gerar palavras: {e}")
            return "WordGenerate", "TipGenerate"
        
class Hangman:

    def __init__(self, file_words=None):
        self.file_words = file_words
        self.df = None
        self.word_categorie = []
        self.current_word = ''
        self.current_tip = ''
        self.uncovered_letter = []
        self.wrong_letters = []
        self.chances = 6
        self.generator_ia = GeneratorWordsIA()

    def load_words(self):
        if self.file_words:
            self.df = pd.read_excel(self.file_words, sheet_name='words', usecols=['Categore', 'Name', 'Tip'])
            self.word_categorie = list(self.df['Categorie'].unique())
        else :
            self.word_categorie = ['Frutas', 'Animais','Paises','Tecnologia']

    def select_categorie(self):
        Screen.clear_screen()
        while True:
            print("Categorias: ")
            for idx, categorie in enumerate(self.word_categorie, 1):
                print(f'{idx} - {categorie}')

            try:
                select = int(input('Selecione uma categoria: ')) -1
                if 0 <= select <len(self.word_categorie):
                    return self.word_categorie[select]
                else:
                    print('Escolha inválida. Tente novamente.')
            except:
                print('Entrada inválida. Digite um número.')

    def play_game(self):
        self.load_words()
        choose_category = self.select_categorie()
        if self.df is not None:
            words = self.df[self.df['Categorie'] == choose_category]
            self.current_word, self.current_tip = random.choice(list(zip(words['Name'], words['Tip'])))
        else:
            self.current_word, self.current_tip = self.generator_ia.generate_words(choose_category)

        self.uncovered_letter = ['_' for _ in self.current_word]
        self.wrong_letters = []
        self.chances = 6

        while self.chances > 0:
            Screen.clear_screen()
            Screen.header()
            print(Force.show(self.chances))
            print(' '.join(self.uncovered_letter))
            print(f'\nChances restantes: {self.chances}')
            print(f'Letras erradas: {self.wrong_letters}')
            print(f'\nDica: {self.current_tip}')

            attempt = input('\nDigite uma letra: ').lower()
            if attempt in self.current_word.lower():
                for idx, letter in enumerate(self.current_word):
                    if letter.lower() == attempt:
                        self.uncovered_letter[idx] = letter
            else:
                self.chances -= 1
                self.wrong_letters.append(attempt)

            
            if '_' not in self.uncovered_letter:
                print(f'\n Você venceu! A palavra era: {self.current_word}')
                return
            
        Screen.clear_screen()
        Screen.header()
        print(Force.show(0))
        print(f'\nVocê perdeu. A palavra era: {self.current_word}')


if __name__ == '__main__':
    play = Hangman()
    play.play_game()

    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")