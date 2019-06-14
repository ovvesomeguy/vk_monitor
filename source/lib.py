import vk_api
import random
import time
import datetime
import re

from configs.config import access_token , time_for_send , build_level
from source.logger import log

def __auth_as_group():
    vk = vk_api.VkApi(token = access_token)
    return vk

def set_random_id():
    rand = random.randint(0 , 2147483647)
    return rand

def send_me_message(message):
    vk = __auth_as_group()
    vk.method('messages.send' , {'user_id': 263838377 , 'random_id': set_random_id(),  'message': message})

def need_to_send():
    now_date = time.strftime('%H:%M')
    result = []
    for user_date in time_for_send:
        if now_date == user_date:
            result.append(now_date)
    if len(result) != 0:
        return True
    else:
        return False
def send_cool_message():
    send_me_message('Наверное что-то важное сэр, просто напоминаю.')
    log('Сообщение отправвлено')