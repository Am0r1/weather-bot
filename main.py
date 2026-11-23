import schedule
import python_weather
import asyncio
import time
import telebot
from telebot import types

TOKEN = "9147286976:AAGBQOXc-M7PnTqX_4sghwjrRPlIUYOLbaw"
bot = telebot.TeleBot(TOKEN)

async def job():
    client = python_weather.Client(unit=python_weather.METRIC, locale=python_weather.enums.Locale.RUSSIAN)
    weather = await client.get("Voronezh")
    result = f"Температура: {weather.temperature} °C\nСкорость ветра: {weather.wind_speed} km/h\nОписание: {weather.description}\nВлажность: {weather.humidity}%\nДавление: {round(weather.pressure*100/133.322, 2)} mmHg"
    await bot.send_message(chat_id=1704105791, text=result)
asyncio.run(job())
# schedule.every().day.at("07:00").do(job)

# while True:
#      schedule.run_pending()
#      time.sleep(1)
