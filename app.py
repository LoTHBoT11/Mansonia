import asyncio
from aiogram import Bot, Dispatcher, types

bot = Bot(token="6549453817:AAHJ0GUKz19fqcjbslqwbkO33MWHpRKn-lE")

dp = Dispatcher()

@dp.message()
async def start_cmd(message: types.Message):
    await message.answer('это была команда старт')


async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())