import telebot
import time
import threading
import os
from flask import Flask

TOKEN = "8699592178:AAF7Lk0faicvdTssd9Ju4QrFNDO9tIBiVQA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот работает 24/7!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

def run_bot():
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)

app = Flask(__name__)

@app.route('/')
def health():
    return "Бот работает", 200

def run_web():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    print("🚀 Бот запущен")
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    run_web()
