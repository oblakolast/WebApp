
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor

API_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID', '0'))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentType.PHOTO)
async def handle_photo(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ У вас нет прав для загрузки.")
    photo = message.photo[-1]
    await bot.download_file_by_id(photo.file_id, destination_file='latest.jpg')
    await message.reply("✅ Фото обновлено!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
