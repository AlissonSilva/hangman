# Jogo da Forca 🪓

Este é um jogo da forca implementado em Python, permitindo que os jogadores adivinhem palavras de categorias diversas. O jogo suporta o carregamento de palavras a partir de um arquivo Excel ou a geração automática utilizando IA.

---

## 📋 Funcionalidades

- Escolha de categorias para o jogo.
- Palavras e dicas:
  - **Arquivo Excel:** Para palavras predefinidas.
  - **IA:** Para geração dinâmica.
- Representação visual do progresso do jogo (forca).
- Gerenciamento de entradas inválidas e erros.
- Feedback visual sobre o status do jogo (vitória ou derrota).

---

## 🛠️ Tecnologias Utilizadas

- **Python** (3.12 ou superior)
- **Bibliotecas**:
  - `os` - Para comandos de terminal.
  - `re` - Para uso de expressões regulares.
  - `pandas` - Manipulação de dados em arquivos Excel.
  - `google.generativeai` - Geração de palavras e dicas usando IA.
  - 
  - `random` - Seleção aleatória de palavras.

---

## 🔧 Pré-requisitos

1. **Python instalado (3.9 ou superior)**  
   [Download Python](https://www.python.org/downloads/)

2. **Instalar dependências**  
   Use o comando abaixo para instalar as bibliotecas necessárias:
   ```bash
   pip install pandas google-generativeai
