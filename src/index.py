import requests
from tg_side import send_message, get_chat_update, get_update_json, last_update, last_update_id
from time import sleep

if __name__ == "__main__":
    update_id = last_update_id()
    while True:
        try:
            last_update()['text'] == "пост"
            if update_id == last_update_id():
                send_message(
                    "Сейчас",
                    get_chat_update(last_update())
                )
                update_id += 1
        except KeyError:
            print("Несовпадение!")
        finally:
            sleep(2)