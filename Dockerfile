FROM python

COPY . .

RUN pip install requests telethon

CMD [ "python", "./bot.py" ]