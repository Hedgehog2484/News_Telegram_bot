import asyncio
import aiosqlite

from aiogram import Bot, Dispatcher

from load_config import TOKEN, DATABASE_PATH
from services import background_parsing, parse_kremlin, parse_rbc
from handlers import register_handlers

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher(bot)

    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER,
            rbc_notify INTEGER,
            kremlin_notify INTEGER
            )""")
        await db.commit()

    await parse_rbc()
    await parse_kremlin()

    register_handlers(dp)
    asyncio.create_task(background_parsing(bot))
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())