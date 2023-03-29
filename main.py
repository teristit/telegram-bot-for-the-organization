from settings import VK_TOKEN as token
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
print(help(vk.messages.send()))
