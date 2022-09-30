#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import telebot
import requests
import urllib.request
import json

keys_file = open('keys.txt', 'r')
keys = keys_file.readlines()
keys_file.close()
token = keys[3]
bot = telebot.TeleBot(token)

FOLDER_ID = keys[1]
key = keys[2]
params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])

@bot.message_handler(content_types=['voice'])
def get_audio_messages(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        path = file_info.file_path
        fname = os.path.basename(path)
        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        with open(fname+'.ogg', 'wb') as f:
            f.write(doc.content)
        with open(fname + '.ogg', 'rb') as f:
            data = f.read()
        url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
        url.add_header("Authorization", 'Api-Key {}'.format(key))
        responseData = urllib.request.urlopen(url).read().decode('UTF-8')
        decodedData = json.loads(responseData)
        if decodedData.get("error_code") is None:
            print(decodedData.get("result"))
            bot.send_message(message.from_user.id, format(decodedData.get("result")))
        else:
            bot.send_message(message.from_user.id, "Прошу прощения, но я не разобрал сообщение, или оно поустое...")
    except Exception :
        bot.send_message(message.from_user.id,  "Прошу прощения, но я не разобрал сообщение, или оно поустое...")
    finally:
        os.remove(fname + '.ogg')

bot.polling(none_stop=True, interval=0)