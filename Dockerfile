FROM python

ADD bot.py .
ADD signal_converter.py .

RUN pip install requests telethon

CMD [ "python", "./bot.py" ]