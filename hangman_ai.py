import re
import openai
import random
import pandas as pd
import os
import google.generativeai as genai

class Screen:
    @staticmethod
    def clear_screen():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

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
    def generate_words(self, category):
        prompt = f"Crie uma palavra e uma dica relacionadas à categoria: {category}."
        try:

            genai.configure(api_key="AIzaSyAoarCK12vcNGq6mREYvAFq_T-DTeJp3jI")
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            # Faz a chamada ao modelo
            response = model.generate_content(prompt)
            
            # Pega o texto gerado pela resposta
            generated_text = response.text.strip()

            # Regex para capturar Palavra e Dica
            pattern = r'\*\*Palavra:\*\*\s*(.*?)\n\n\*\*Dica:\*\*\s*(.*)'

            match = re.search(pattern, generated_text)
            if match:
                word = match.group(1)
                tip = match.group(2)

            return word.strip(), tip.strip()
        
        except Exception as e:
            print(f"Erro ao gerar palavras: {e}")
            return "WordGenerate", "TipGenerate"
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
            return "WordGenerate", "TipGenerate"
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
            return "WordGenerate", "TipGenerate"
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.response)
            return "WordGenerate", "TipGenerate"

        
class Hangman:

    def __init__(self, file_words=None):
        self.generated_by = ''
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
            self.df = pd.read_excel(self.file_words, sheet_name='words', usecols=['Categorie', 'Name', 'Tip'])
            self.word_categorie = list(self.df['Categorie'].unique())
            self.generated_by = 'File'
        else :
            self.word_categorie = ['Frutas', 'Animais','Paises','Tecnologia']
            self.generated_by = 'IA'

    def select_categorie(self):
        Screen.clear_screen()
        while True:
            print("Categorias: ")
            for idx, categorie in enumerate(self.word_categorie, 1):
                print(f'{idx} - {categorie}')

            try:
                select = int(input('Selecione uma categoria: ')) -1
                if 0 <= select < len(self.word_categorie):
                    return self.word_categorie[select]
                else:
                    print('Escolha inválida. Tente novamente.')
            except:
                print('Entrada inválida. Digite um número.')

    def play_game(self):
        self.load_words()
        choose_category = self.select_categorie()
        if self.df is not None:
            try:
                words = self.df[self.df['Categorie'] == choose_category]
                self.current_word, self.current_tip = random.choice(list(zip(words['Name'], words['Tip'])))
            except:
                self.current_word, self.current_tip = self.generator_ia.generate_words(choose_category)
            
        else:
            self.current_word, self.current_tip = self.generator_ia.generate_words(choose_category)

        self.uncovered_letter = ['_' for _ in self.current_word]
        self.wrong_letters = []
        self.chances = 6

        while self.chances > 0:
            Screen.clear_screen()
            Screen.header()
            print(f'Gerado via: {self.generated_by}')
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
    play.file_words = './files/words_hangman.xlsx'
    play.play_game()

    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")