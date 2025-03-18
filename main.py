from aiogram import Bot, Dispatcher, executor, types
from aiogram.fsm.storage.memory import MemoryStorage


API_TOKEN = "ВАШ_ТОКЕН_БОТА"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Используйте MemoryStorage
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(
        "🎥 Откройте эффект плаща невидимки в приложении!",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(
                "🔮 Запустить",
                url=f"https://t.me/{bot.username}?start=mini_app"
            )
        )
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
