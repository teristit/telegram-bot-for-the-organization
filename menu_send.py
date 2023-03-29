from telebot import types


def menu_send(id, bot):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Рассказать об организации', callback_data='but1')
    button2 = types.InlineKeyboardButton('Предоставить расписание', callback_data='but2')
    button3 = types.InlineKeyboardButton('Предоставить информацию о преподавателях', callback_data='but3')
    button4 = types.InlineKeyboardButton('Предоставить список направлений', callback_data='but4')
    button5 = types.InlineKeyboardButton('Предоставить контактные данные', callback_data='but5')
    buttons.add(button1, button2, button3, button4, button5)
    bot.send_message(id, text='Выберите действие', reply_markup=buttons)
