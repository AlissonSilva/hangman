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
  - `random` - Seleção aleatória de palavras.

---

## 🔧 Pré-requisitos

1. **Python instalado (3.12 ou superior)**  
   [Download Python](https://www.python.org/downloads/)

2. **Instalar dependências**  
   Use o comando abaixo para instalar as bibliotecas necessárias:
   ```bash
   pip install pandas google-generativeai

3. **Arquivo Excel (opcional)**  
   Crie um arquivo Excel com os seguintes requisitos:
   - Nome da aba: words
   - Colunas:
    - Categorie: Categoria da palavra.
    - Name: Palavra.
    - Tip: Dica para a palavra.

## 🚀 Como executar
1. **Clone este repositório:**
 ```bash
   git clone https://github.com/seu-usuario/jogo-da-forca.git
   cd jogo-da-forca

2. **Configure a chave de API de IA (opcional):**
  - Adicione sua chave na linha correspondente:
   ```python
      genai.configure(api_key="sua-chave-de-api")

3. **Execute o jogo:**
  - Adicione sua chave na linha correspondente:
   ```bash
      python forca.py
