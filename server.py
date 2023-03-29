import telebot
from telebot import types

from settings import TG_TOKEN, ID_ADMIN

bot = telebot.TeleBot(TG_TOKEN)
admin = False
password = '111'


@bot.message_handler(commands=["admin"])
def admin_message(message):
    global admin
    admin = True
    bot.send_message(message.from_user.id, 'Введите пароль:')


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(ID_ADMIN, message.from_user.id)
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Рассказать об организации', callback_data='but1')
    button2 = types.InlineKeyboardButton('Предоставить расписание', callback_data='but2')
    button3 = types.InlineKeyboardButton('Предоставить информацию о преподавателях', callback_data='but3')
    button4 = types.InlineKeyboardButton('Предоставить список направлений', callback_data='but4')
    buttons.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, text='Здравствуйте!\nВы запустили бота\nВыберите действие', reply_markup=buttons)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'but1':
        bot.send_message(call.from_user.id, 'все в организации работает')
    elif call.data == 'but2':
        bot.send_message(call.from_user.id, 'расписания нет')
    elif call.data == 'but3':
        bot.send_message(call.from_user.id, 'преподавтелей много')
    elif call.data == 'but4':
        bot.send_message(call.from_user.id, 'направлений много')
    elif call.data == 'but5' and admin:
        bot.send_message(call.from_user.id, 'but5')
    elif call.data == 'but6' and admin:
        bot.send_message(call.from_user.id, 'but6')
    elif call.data == 'but7' and admin:
        bot.send_message(call.from_user.id, 'but7')
    elif call.data == 'but8' and admin:
        bot.send_message(call.from_user.id, 'but8')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global admin
    if admin:
        if message.text == password:
            bot.send_message(message.from_user.id, 'Верный пароль')
            admin = False

            bot.send_message(ID_ADMIN, message.from_user.id)
            buttons = types.InlineKeyboardMarkup(row_width=1)
            button5 = types.InlineKeyboardButton('Рассказать об организации', callback_data='but5')
            button6 = types.InlineKeyboardButton('Предоставить расписание', callback_data='but6')
            button7 = types.InlineKeyboardButton('Предоставить информацию о преподавателях', callback_data='but7')
            button8 = types.InlineKeyboardButton('Предоставить список направлений', callback_data='but8')
            buttons.add(button5, button6, button7, button8)
            bot.send_message(message.chat.id, text='Какой пунк хотие редактировать?',
                             reply_markup=buttons)
        else:
            bot.send_message(message.from_user.id, 'Не верный пароль')
            admin = False
    elif message.text[:4] == 'Дима':
        bot.send_message(ID_ADMIN, message.text)
    else:
        bot.send_message(message.from_user.id, message.text)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
        bot.reply_to(message, e)

bot.polling(none_stop=True)
