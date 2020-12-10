from decouple import config
import requests
import json

URL="https://api.telegram.org/bot" + config("TG_TOKEN") + "/"

def send_message(message: str, chat_id: str) -> None:
    """ Функция отпраляет сообщение пользователю """

    params = {'chat_id': chat_id, 'text': message}
    last_part_url = "sendMessage"
    if message != None:
        response = requests.get(
            "".join((URL, last_part_url)), 
            data=params)
        print("Message sent")
    
def get_update_json():
    last_part_url = "getUpdates"
    response = requests.get(
        "".join((URL, last_part_url)))
    return response.json()

def last_update():
    data = get_update_json()
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def last_update_id():
    data = get_update_json()
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]['update_id']

def get_chat_update(update):
    chat_id = update['message']['chat']['id']
    return chat_id