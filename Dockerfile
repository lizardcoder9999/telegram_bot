#Dockerfile,Image,Container

FROM python:3.8


ADD bot.py .

RUN pip install pyTelegramBotAPI

# WORKDIR /home/rootuser/Desktop/telegram_bot/telegram

CMD ["python","./bot.py"]

