import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from signal_converter import msg_to_signal

api_id = int(os.getenv('TG_API_ID'))
api_hash = os.getenv('TG_API_HASH')
session_string = os.getenv('TG_SESSION_STRING')
client = TelegramClient(StringSession(session_string), api_id, api_hash)


@client.on(events.NewMessage(chats=-1001753918408, incoming=True, pattern='\[Spots]'))
async def my_event_handler(message):
    msg = message.text
    signal = msg_to_signal(msg)
    print(signal, flush=True)

with client:
    print(f'listening on {api_id}', flush=True)
    client.run_until_disconnected()
