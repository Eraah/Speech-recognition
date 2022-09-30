# -*- coding: utf-8 -*-

import requests
import time
import json

# Укажите ваш API-ключ и ссылку на аудиофайл в Object Storage.
keys_file = open('keys.txt', 'r')
keys = keys_file.readlines()
keys_file.close()
key = keys[0]
filelink = 'https://storage.yandexcloud.net/spchkt/14.opus'


POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"

body ={
    "config": {
        "specification": {
            "languageCode": "ru-RU"
        }
    },
    "audio": {
        "uri": filelink
    }
}

# Если вы хотите использовать IAM-токен для аутентификации, замените Api-Key на Bearer.
header = {'Authorization': 'Api-Key {}'.format(key)}

# Отправить запрос на распознавание.
req = requests.post(POST, headers=header, json=body)
data = req.json()
print(data)

id = data['id']

# Запрашивать на сервере статус операции, пока распознавание не будет завершено.
while True:

    time.sleep(1)

    GET = "https://operation.api.cloud.yandex.net/operations/{id}"
    req = requests.get(GET.format(id=id), headers=header)
    req = req.json()

    if req['done']: break
    print("Not ready")

# Показать полный ответ сервера в формате JSON.
#print("Response:")
#print(json.dumps(req, ensure_ascii=False, indent=2))

# Показать только текст из результатов распознавания.
print("Text chunks:")
for chunk in req['response']['chunks']:
    print(chunk['alternatives'][0]['text'])
