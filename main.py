from aiogram import Bot, Dispatcher, executor, types
import logging

from tokenBOT import tokenAPI

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tokenAPI)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

