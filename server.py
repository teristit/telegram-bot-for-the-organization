import telebot
from telebot import types
from settings import TG_TOKEN, ID_ADMIN
from menu_send import menu_send



bot = telebot.TeleBot(TG_TOKEN)
flag = ''


def file_open(name):
    f = open('data/' + name, encoding="utf-8")
    f = f.read()
    return f


@bot.message_handler(commands=["admin"])
def admin_message(message):
    if str(message.from_user.id) == ID_ADMIN:
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Рассказать об организации', callback_data='but6')
        button2 = types.InlineKeyboardButton('Предоставить расписание', callback_data='but7')
        button3 = types.InlineKeyboardButton('Предоставить информацию о преподавателях', callback_data='but8')
        button4 = types.InlineKeyboardButton('Предоставить список направлений', callback_data='but9')
        button5 = types.InlineKeyboardButton('Предоставить контактные данные', callback_data='but10')
        buttons.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, text='Какой пунк хотие редактировать?', reply_markup=buttons)
    else:
        bot.send_message(message.from_user.id, 'Вы не администратор')


@bot.message_handler(commands=["start"])
def start_message(message):
    flag = ''
    bot.send_message(ID_ADMIN,message.from_user.id)
    bot.send_message(message.chat.id, text='Здравствуйте!\nВы запустили бота')
    menu_send(message.chat.id, bot)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global flag
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'but1':
        name = 'information.txt'
        text = file_open(name)
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton('Вернутся в меню', callback_data='but11')
        buttons.add(button)
        bot.send_message(call.from_user.id, text=text, reply_markup=buttons)
    elif call.data == 'but2':
        name = 'schedule.txt'
        text = file_open(name)
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton('Вернутся в меню', callback_data='but11')
        buttons.add(button)
        bot.send_message(call.from_user.id, text=text, reply_markup=buttons)
    elif call.data == 'but3':
        name = 'teachers.txt'
        text = file_open(name)
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton('Вернутся в меню', callback_data='but11')
        buttons.add(button)
        bot.send_message(call.from_user.id, text=text, reply_markup=buttons)
    elif call.data == 'but4':
        name = 'directions.txt'
        text = file_open(name)
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton('Вернутся в меню', callback_data='but11')
        buttons.add(button)
        bot.send_message(call.from_user.id, text=text, reply_markup=buttons)
    elif call.data == 'but5':
        name = 'contacts.txt'
        text = file_open(name)
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton('Вернутся в меню', callback_data='but11')
        buttons.add(button)
        bot.send_message(call.from_user.id, text=text, reply_markup=buttons)

    elif call.data == 'but6' and str(call.from_user.id) == ID_ADMIN:
        flag = 'information.txt'
        text = 'Введите текст или отправьте файл в формате txt'
        bot.send_message(call.from_user.id, text)
    elif call.data == 'but7' and str(call.from_user.id) == ID_ADMIN:
        flag = 'schedule.txt'
        text = 'Введите текст или отправьте файл в формате txt'
        bot.send_message(call.from_user.id, text)
    elif call.data == 'but8' and str(call.from_user.id) == ID_ADMIN:
        flag = 'teachers.txt'
        text = 'Введите текст или отправьте файл в формате txt'
        bot.send_message(call.from_user.id, text)
    elif call.data == 'but9' and str(call.from_user.id) == ID_ADMIN:
        flag = 'directions.txt'
        text = 'Введите текст или отправьте файл в формате txt'
        bot.send_message(call.from_user.id, text)
    elif call.data == 'but10' and str(call.from_user.id) == ID_ADMIN:
        flag = 'contacts.txt'
        text = 'Введите текст или отправьте файл в формате txt'
        bot.send_message(call.from_user.id, text)
    elif call.data == 'but11':
        menu_send(call.from_user.id, bot)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global flag
    if flag:
        try:
            src = 'data/' + flag
            with open(src, 'w', encoding="utf-8") as new_file:
                new_file.write(message.text)

            bot.reply_to(message, "Пожалуй, я сохраню это")
        except Exception as e:
            bot.reply_to(message, 'Ошибка')
        flag = ''
    else:
        bot.reply_to(message, 'Я вас не понимаю')

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    global flag
    if flag:
        try:
            chat_id = message.chat.id

            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = 'data/' + flag
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, "Пожалуй, я сохраню это")
        except Exception as e:
            bot.reply_to(message, 'Ошибка')
        flag = ''


bot.polling(none_stop=True)
