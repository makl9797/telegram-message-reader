import requests
import base64
import hmac
import hashlib
import time
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
from signal_converter import msg_to_signal

load_dotenv()

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
client = TelegramClient('session', api_id, api_hash)


api_key = os.getenv('KC_API_KEY')
api_secret = os.getenv('KC_API_SECRET')
api_passphrase = 'signal_bot'
method = 'GET'
endpoint = '/api/v1/orders'


def get_headers(method, endpoint):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + method + endpoint
    signature = base64.b64encode(hmac.new(
        api_secret.encode(), str_to_sign.encode(), hashlib.sha256).digest()).decode()
    passphrase = base64.b64encode(hmac.new(api_secret.encode(
    ), api_passphrase.encode(), hashlib.sha256).digest()).decode()
    return {'KC-API-KEY': api_key,
            'KC-API-KEY-VERSION': '2',
            'KC-API-PASSPHRASE': passphrase,
            'KC-API-SIGN': signature,
            'KC-API-TIMESTAMP': str(now)
            }


r = requests.get('https://api.kucoin.com/api/v1/orders',
                 headers=get_headers(method, endpoint))


print(r.json())


@client.on(events.NewMessage(chats=-1001753918408, incoming=True, pattern='\[Spots]'))
async def my_event_handler(message):
    msg = message.text
    signal = msg_to_signal(msg)
    print(signal)


client.start()
client.run_until_disconnected()
