import schedule
import python_weather
import asyncio
import time
import telebot
from telebot import types

TOKEN = "9147286976:AAGBQOXc-M7PnTqX_4sghwjrRPlIUYOLbaw"
bot = telebot.TeleBot(TOKEN)
async def weather():
    client = python_weather.Client(unit=python_weather.METRIC, locale=python_weather.enums.Locale.RUSSIAN)
    weather = await client.get("Voronezh")
    print(weather.kind)
    print(weather.description)
asyncio.run(weather())