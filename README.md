
# 🤖 Bot da FURIA — Assistente de Eng. de Software (Desafio Técnico)

Este projeto foi desenvolvido por Saymon Johnson como parte de uma aplicação para a vaga de "Assistente de Engenharia de Software" na FURIA E-sports.

---

## 📌 O que faz este bot?

Um bot interativo para Telegram com foco em fãs da FURIA, com as seguintes funcionalidades:

- 📅 Mostrar o **próximo jogo da FURIA**
- 🕹️ Exibir os **3 últimos resultados**
- 🎯 Informar o **line-up atual**
- ✅ Rodar um **quiz interativo com 5 perguntas**
- 📞 Mostrar um número de **contato inteligente** 
  
Tudo isso em um menu com botões intuitivos ao iniciar o bot com `/start`.

---

## 🚀 Como executar o bot

1. **Pré-requisitos:**
   - Python 3.7 ou superior
   - Instalar a biblioteca `pyTelegramBotAPI`:
     ```bash
     pip install pyTelegramBotAPI
     ```

2. **Editar o token do bot:**

   No início do arquivo Python (`.py`), substitua a string abaixo pela token do seu bot do Telegram:

   ```python
   TOKEN = "seu_token_aqui"
   ```

3. **Rodar o bot:**

   No terminal ou IDE, execute:

   ```bash
   python bot_furia.py
   ```

4. **Interaja com o bot no Telegram:**

   Use o comando `/start` no chat com seu bot para acessar o menu com todas as opções.

---
5. **Opção de abrir o bot pelo navegador ou mobile**

	https://t.me/furiaprojectengsoft_bot


## 🧠 Estrutura do quiz

O quiz possui 5 perguntas de múltipla escolha. Você pode adicionar, remover ou editar as perguntas diretamente na lista `quiz_questions`, seguindo o mesmo padrão:

```python
quiz_questions = [
    {
        "pergunta": "🆕 Em qual ano a FURIA foi fundada?",
        "opcoes": ["2015", "2021", "2019", "2017"],
        "correta": 3
    },
    ...
]
```

---

## 📂 Arquivos incluídos

- `bot_furia.py` — código principal do bot
- `resize_logo.py` — código para formatar a logo
- `furia_logo.png.png` — logo usada no menu inicial
- `README.md` — este arquivo com instruções

---

## 👨‍💻 Sobre o autor

Saymon Johnson 
E-mail: saymonjohnson1@gmail.com  
LinkedIn: [https://www.linkedin.com/in/saymonjohnson](https://www.linkedin.com/in/saymonjohnson)

---

> Agradeço pela oportunidade e estou à disposição para evoluir com a equipe da FURIA!!!
