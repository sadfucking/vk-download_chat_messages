# Этот код, не программа, скачивает все сообщения из беседы ВК.
# Author: Mautoz Tech (Mikhail Kuznetsov)
#Немного переделал Артур Летов         https://vk.com/perfect.does.not.exist

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Получите ВК токен здесь https://vkhost.github.io/ и вставьте его ниже (Берете из адресной строки) в данный момент самый актуальный кейт мобайл
vk_session = vk_api.VkApi(token="Здесь токен")
session_api = vk_session.get_api()
# Вставьте ID беседы (Берете из адресной строки):
chat_id=1
# Введите ID вашего аккаунта:
user_id=693358666
#Получаем ID последнего сообщения и считаем количество запросов т.к. мы можем получить только 200 сообщений за запрос
lastMessage = session_api.messages.getHistory(count=1, peer_id=2000000000+chat_id, user_id=user_id)
pages=int(lastMessage['items'][0]['id']/200+1)
print("Сообщений: " + str(pages))

#И получаем сообщения по 200 штук за раз
file=open("text.txt", 'r+', encoding='utf-8')
content = file.read()
offset=0
for i in range(1, pages+1):
    offset+=200
    history = session_api.messages.getHistory(offset=offset, count=200, peer_id=2000000000+chat_id, user_id=user_id)['items']

    for j in reversed(history):
        if j['text'] not in content:
            file.write(str(j['text'])+'\n')
            print(j['text'])
file.close()
print("done")

#исправил дублирование текста, скрипт сохраняет только текст, если нужно всё, ущашите ['text'] везде где он есть, так же за счет того что здесь используется 'r+', файл text.txt создавать нужно вручную, или замените 'r+' на 'x', не проверял будет ли работать, но должно, лично у меня возникда проблема с исходным кодом такая: он качал в файл только 200 сообщений, я добавил смещение чтобы этого избежать, + код теперь проверяет наличие текста в файле, так что теперь он не будет дублировать, спасибо автору за помощь, код пригодился для создания базы данных для обучения модели на основе цепей маркова.
