FROM python:3

COPY . /tg_msg_reader

WORKDIR /tg_msg_reader

RUN pip3 install -r requirements.txt

CMD [ "python3", "./bot.py" ]