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

            if message in ['старт', '6']:
                blasthack(id, 'Здравствуйте!\nВы запустили бота')
                blasthack(id, 'Выберите действие:')
                blasthack(id, '1 Рассказать об организации')
                blasthack(id, '2 Предоставить расписание')
                blasthack(id, '3 Предоставить информацию о преподавателях')
                blasthack(id, '4 Предоставить список направлений')
                blasthack(id, '5 Предоставить контактные данные')


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
            elif message == '6':
                blasthack(id, 'Выберите действие:')
                blasthack(id, '1 Рассказать об организации')
                blasthack(id, '2 Предоставить расписание')
                blasthack(id, '3 Предоставить информацию о преподавателях')
                blasthack(id, '4 Предоставить список направлений')
                blasthack(id, '5 Предоставить контактные данные')

            else:
                blasthack(id, 'Я вас не понимаю')
