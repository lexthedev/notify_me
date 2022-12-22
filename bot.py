import time
import logging
import os

from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.environ.get('TOKEN')
MSG = "Did you program today, {}?"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    USER_ID = message.from_user.id
    USER_NAME = message.from_user.first_name
    USER_FULL_NAME = message.from_user.full_name
    logging.info(f'{USER_ID}, {USER_FULL_NAME}, {time.asctime()}')

    await message.reply(f"Hello, {USER_FULL_NAME}! Don't you think it's a good day?)")

    for i in range(7):
        # time.sleep(60*60*24)
        time.sleep(15)

        await bot.send_message(USER_ID, MSG.format(USER_NAME))

if __name__ == '__main__':
    executor.start_polling(dp)
