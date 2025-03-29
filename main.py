import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin
from telebot.types import BotCommand

    
bot = telebot.TeleBot("7941249751:AAFB7ktTvPZOlg-nVBw0U7pjxNWM0TrzMZQ")

bot.set_my_commands([
    BotCommand("start", "Запуск бота"),
    BotCommand("hello", "Здоровается с вами"),
    BotCommand("bye", "Прощается с вами"),
    BotCommand("pass", "Cгенерирует пароль длиной от 1 до 15"),
    BotCommand("emodji", "Отправит любой эмоджи"),
    BotCommand("coin", "Игра в монетку"),
    BotCommand("heh", "Смеется заданное количество раз")
])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.У меня есть такие команды как:/hello, /bye, /pass, /emodji и /coin")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def ask_password_length(message):
    msg = bot.reply_to(message, "Укажите длину пароля (число от 1 до 15):")
    bot.register_next_step_handler(msg, process_password_length)
def process_password_length(message):
    try:
        length = int(message.text)
        if length < 1:
            length = 1
        elif length > 15:
            length = 15
        password = gen_pass(length)
        bot.reply_to(message, f"Вот твой сгенерированный пароль длиной {length} символов: {password}")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число от 1 до 15. Попробуйте снова командой /pass")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
bot.polling()
