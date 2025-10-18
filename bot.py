import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я базовый бот на aiogram.\n"
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/help - помощь\n"
        "/echo - эхо-ответ"
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Это помощь по боту:\n"
        "• Просто отправь мне любое сообщение\n"
        "• Используй команды из меню"
    )

# Обработчик команды /echo
@dp.message(Command("echo"))
async def cmd_echo(message: Message):
    text = message.text[6:]  # Убираем "/echo "
    if text:
        await message.answer(f"Эхо: {text}")
    else:
        await message.answer("Напиши текст после команды /echo")

# Обработчик текстовых сообщений
@dp.message(F.text)
async def handle_text(message: Message):
    await message.answer(f"Вы написали: {message.text}")

# Обработчик любых других сообщений
@dp.message()
async def handle_other(message: Message):
    await message.answer("Я понимаю только текстовые сообщения")

# Основная функция
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
