import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from settings import VK_TOKEN as token

bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def blasthack(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


def file_open(name):
    f = open('data/' + name, encoding="utf-8")
    f = f.read()
    return f


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            message = event.text.lower()

            id = event.user_id
            if message == 'старт':
                blasthack(id, 'Здравствуйте!\nВы запустили бота')
            if message in ['старт', '6']:
                blasthack(id,
                          'Выберите действие:\n1 Рассказать об организации\n2 Предоставить расписание\n3 Предоставить информацию о преподавателях\n4 Предоставить список направлений\n5 Предоставить контактные данные')


            elif message == '1':
                name = 'information.txt'
                text = file_open(name)
                blasthack(id, text)
            elif message == '2':
                name = 'schedule.txt'
                text = file_open(name)
                blasthack(id, text)
            elif message == '3':
                name = 'teachers.txt'
                text = file_open(name)
                blasthack(id, text)
            elif message == '4':
                name = 'directions.txt'
                text = file_open(name)
                blasthack(id, text)
            elif message == '5':
                name = 'contacts.txt'
                text = file_open(name)
                blasthack(id, text)

            else:
                blasthack(id, 'Я вас не понимаю')
            if message not in ['старт', '6']:
                blasthack(id, '6 Вернутся в меню')
