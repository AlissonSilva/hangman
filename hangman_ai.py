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