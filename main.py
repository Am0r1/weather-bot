import schedule
import python_weather
import asyncio
import time
import telebot
from telebot import types

TOKEN = "Your token here"
USER_ID = ["Your user ID here"] # get it here >>> @userinfobot

# Temporary decision cuz it's obviously bad

# Actually I don't give a fuck

bot = telebot.TeleBot(TOKEN)

async def job():
    client = python_weather.Client(unit=python_weather.METRIC, locale=python_weather.enums.Locale.RUSSIAN)
    weather = await client.get("Voronezh")
    result = f"Температура: {weather.temperature} °C\nСкорость ветра: {weather.wind_speed} km/h\nОписание: {weather.description}\nВлажность: {weather.humidity}%\nДавление: {round(weather.pressure*100/133.322, 2)} mmHg"
    for id in USER_ID:
        bot.send_message(chat_id=id, text=result)

def start():
    asyncio.run(job())

schedule.every().day.at("07:00").do(start)


while True:
    schedule.run_pending()
    time.sleep(1)

#schedule.every(5).seconds.do(start)