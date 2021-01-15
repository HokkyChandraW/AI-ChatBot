import requests
import json
from chatbot import bot_initialize


class telegram_bot():
    def __init__(self):
        self.token = "1553650162:AAHyiKEN5Y7W92shC8xQq0_h1SxJv-394XE"  # write your token here!
        self.url = f"https://api.telegram.org/bot{self.token}"

    def get_updates(self, offset=None):
        # In 100 seconds if user input query then process that, use it as the read timeout from the server
        url = self.url+"/getUpdates?timeout=100"
        if offset:
            url = url+f"&offset={offset+1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def send_message(self, msg, chat_id):
        url = self.url + f"/sendMessage?chat_id={chat_id}&text={msg}"
        if msg is not None:
            requests.get(url)

    def grab_token(self):
        return token


tbot = telegram_bot()
update_id = None


def make_reply(msg):     # user input will go here

    if msg is not None:
        # user input will start processing to bot_initialize function
        reply = bot_initialize(msg)
    return reply


while True:
    print("...")
    updates = tbot.get_updates(offset=update_id)
    updates = updates['result']
    print(updates)
    if updates:
        for item in updates:
            update_id = item["update_id"]
            print(update_id)
            try:
                message = item["message"]["text"]
                print(message)
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            print(from_)
            reply = make_reply(message)
            tbot.send_message(reply, from_)
