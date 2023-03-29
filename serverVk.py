import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from settings import VK_TOKEN as token



bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def blasthack(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

       if event.to_me:


          message = event.text.lower()

          id = event.user_id



          if message == 'старт':
            blasthack(id, 'Здравствуйте!\nВы запустили бота')
            blasthack(id, 'Выберите\nВы запустили бота')

          elif message == 'как дела?':
              blasthack(id, 'Хорошо, а твои как?' )

          else:
             blasthack(id, 'Я вас не понимаю! :(')