import telebot
from telebot import types
import os

TOKEN = "7717496084:AAGFgBlHZT8eWdtqw3WVYLSi7aSOCFx52IQ"
bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar pontuações
user_scores = {}

# ============================
# 🔧 EDITAR AQUI: Informações manuais
# ============================

# Próximo jogo (edite conforme necessário)
proximo_jogo = " FURIA 🆚 The MongolZ\n📅 10/05/2025 📅"

# Últimos 3 resultados (edite conforme necessário)
ultimos_resultados = [
    "❌ FURIA 0 x 2 The MongolZ - PGL Bucharest 2025 - 09/04/2025",
    "❌ FURIA 0 x 2 Virtus pro - PGL Bucharest 2025 - 08/04/2025",
    "❌ FURIA 1 x 2 Complexity - PGL Bucharest 2025 - 07/04/2025"
]

# Line-up atual da FURIA (edite conforme necessário)
lineup_atual = [
    "🔫🇧🇷 FalleN",
    "🔫🇧🇷 yuurih",
    "🔫🇱🇻 YEKINDAR",
    "🔫🇧🇷 KSCERATO",
    "🔫🇰🇿 molodoy",
    "🧠🇧🇷 (Coach) guerri"
]

contato_inteligente = [
    "Whatsapp: https://wa.me/5511993404466\n"
    "(Closed-Beta)"
]
# ============================

# Perguntas e respostas
quiz_questions = [
    {
        "pergunta": "🆕 Em qual ano a FURIA foi fundada?",
        "opcoes": ["2015", "2021", "2019", "2017"],
        "correta": 3
    },
    {
        "pergunta": "🪪 Qual é o nickname real do KSCERATO?",
        "opcoes": ["Kaike", "Kevin", "Kleber", "Kayo"],
        "correta": 0
    },
    {
        "pergunta": "🗺 Qual é o melhor mapa da FURIA?",
        "opcoes": ["Mirage", "Inferno", "Train", "Nuke"],
        "correta": 2
    },
    {
        "pergunta": "🧠 Quem foi o último coach da equipe principal?",
        "opcoes": ["guerri", "sidde", "BIT", "arT"],
        "correta": 0
    },
    {
        "pergunta": "🚀 Contra qual time a FURIA venceu nas quartas de finais na IEM Rio Major 2022?",
        "opcoes": ["FaZe Clan", "NAVI", "Team Liquid", "Cloud9"],
        "correta": 1
    }
]

def get_feedback(score):
    feedback = {
        5: "🐆 SUPER FÃ FURIA! Você domina tudo sobre o time!",
        4: "🔥 FÃ DE CARTEIRINHA! Quase perfeito!",
        3: "💣 ÓTIMO CONHECIMENTO! Continue acompanhando!",
        2: "🔫 BOM! Mas precisa rever alguns detalhes!",
        1: "🛑 HMM... Assista mais jogos!",
        0: "❌ NADA ACERTOU! Vamos recomeçar?"
    }
    return feedback.get(score, "🏁 Quiz completo!")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🎯 LINE-UP ATUAL", callback_data='lineup_atual'),
        types.InlineKeyboardButton("📅 PRÓXIMO JOGO", callback_data='proximo_jogo'),
        types.InlineKeyboardButton("🕹️ ÚLTIMOS RESULTADOS", callback_data='ultimos_resultados'),
        types.InlineKeyboardButton("📞 CONTATO INTELIGENTE", callback_data='contato_inteligente'),
        types.InlineKeyboardButton("✅ INICIAR QUIZ", callback_data='start_quiz'),

    )

    try:
        with open('images/furia_logo.png.png', 'rb') as logo:
            bot.send_photo(
                message.chat.id,
                logo,
                caption=" **Bem-vindo ao BOT da FURIA **\n\nEscolha uma das opções abaixo:",
                reply_markup=markup
            )
    except Exception as e:
        print(f"Erro ao carregar logo: {e}")
        bot.send_message(
            message.chat.id,
            "Erro ao carregar logo",
            reply_markup=markup
        )

@bot.callback_query_handler(func=lambda call: call.data == 'start_quiz')
def start_quiz(call):
    user_id = call.from_user.id
    user_scores[user_id] = 0
    send_question(call.message.chat.id, 0)

def send_question(chat_id, question_num):
    question = quiz_questions[question_num]
    markup = types.InlineKeyboardMarkup(row_width=2)

    buttons = []
    for idx, option in enumerate(question["opcoes"]):
        callback_data = f"ans_{question_num}_{idx}"
        buttons.append(types.InlineKeyboardButton(option, callback_data=callback_data))

    markup.add(*buttons)
    bot.send_message(chat_id, f"❓ **Pergunta {question_num + 1}:**\n\n{question['pergunta']}",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def handle_answer(call):
    user_id = call.from_user.id
    _, q_num, ans = call.data.split('_')
    q_num = int(q_num)
    ans = int(ans)

    if quiz_questions[q_num]["correta"] == ans:
        user_scores[user_id] += 1
        bot.answer_callback_query(call.id, "✅ Correto! +1 ponto!")
    else:
        correct = quiz_questions[q_num]["correta"]
        bot.answer_callback_query(call.id,
                                  f"❌ Errado! A resposta correta era: {quiz_questions[q_num]['opcoes'][correct]}")

    if q_num + 1 < len(quiz_questions):
        send_question(call.message.chat.id, q_num + 1)
    else:
        score = user_scores.get(user_id, 0)
        feedback = get_feedback(score)

        result_text = (
            f"🎉 **QUIZ COMPLETO!** 🎉\n\n"
            f"✅ **ACERTOS:** {score}/5\n"
            f"📢 **FEEDBACK:** {feedback}\n\n"
            "🐆 Continue acompanhando a FURIA nas redes sociais!\n"
            "https://www.instagram.com/furiagg/\n"
            "https://x.com/FURIA"
        )

        bot.send_message(call.message.chat.id, result_text)
        del user_scores[user_id]

@bot.callback_query_handler(func=lambda call: call.data == 'proximo_jogo')
def mostrar_proximo_jogo(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f" **PRÓXIMO JOGO DA FURIA:**\n\n{proximo_jogo}")

@bot.callback_query_handler(func=lambda call: call.data == 'ultimos_resultados')
def mostrar_resultados(call):
    bot.answer_callback_query(call.id)
    texto = "\n".join(ultimos_resultados)
    bot.send_message(call.message.chat.id, f"🕹️ **ÚLTIMOS 3 RESULTADOS:**\n\n{texto}")

@bot.callback_query_handler(func=lambda call: call.data == 'lineup_atual')
def mostrar_lineup(call):
    bot.answer_callback_query(call.id)
    texto = "\n".join(lineup_atual)
    bot.send_message(call.message.chat.id, f"🎯 **LINE-UP ATUAL DA FURIA:**\n\n{texto}")

@bot.callback_query_handler(func=lambda call: call.data == 'contato_inteligente')
def mostrar_lineup(call):
    bot.answer_callback_query(call.id)
    texto = "\n".join(contato_inteligente)
    bot.send_message(call.message.chat.id, f"📞 **CONTATO INTELIGENTE:**\n\n{texto}")

@bot.message_handler(commands=['quiz'])
def quiz_command(message):
    start_quiz(message)

if __name__ == "__main__":
    print("Bot em execução...")
    bot.polling(none_stop=True)
