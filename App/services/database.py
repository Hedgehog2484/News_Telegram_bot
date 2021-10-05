import asyncio
import aiosqlite

from ..load_config import DATABASE_PATH


async def db_add_user(userID: int) -> None:
    async with aiosqlite.connect(DATABASE_PATH) as connect:
        cursor = await connect.execute("SELECT * FROM users WHERE user_id=?", (userID,))
        if await cursor.fetchone() is None:
            await connect.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (userID, 0, 0, 0))
            await connect.commit()
        await cursor.close()


async def db_update_user(userID: int, what_update: str) -> bool:
    """What update must be 'rbc' or 'kremlin'."""
    async with aiosqlite.connect(DATABASE_PATH) as connect:
        cursor = await connect.cursor()

        await cursor.execute("SELECT * FROM users WHERE user_id=?", (userID,))
        value = await cursor.fetchone()

        if what_update == "rbc":
            if value[1] == 0:
                await cursor.execute("UPDATE users SET rbc_notify=1 WHERE user_id=?", (userID,))
                await connect.commit()
                await cursor.close()
                return True
            else:
                await cursor.execute("UPDATE users SET rbc_notify=0 WHERE user_id=?", (userID,))
                await connect.commit()
                await cursor.close()
                return False

        elif what_update == "kremlin":
            if value[2] == 0:
                await cursor.execute("UPDATE users SET kremlin_notify=1 WHERE user_id=?", (userID,))
                await connect.commit()
                await cursor.close()
                return True
            else:
                await cursor.execute("UPDATE users SET kremlin_notify=0 WHERE user_id=?", (userID,))
                await connect.commit()
                await cursor.close()
                return False

        elif what_update == "lenta":
            if value[3] == 0:
                await cursor.execute("UPDATE users SET lenta_notify=1 WHERE user_id=?", (userID,))
                await connect.commit()
                await cursor.close()
                return True
            else:
                await cursor.execute("UPDATE users SET lenta_notify=0 WHERE user_id=?", (userID,))
                await connect.commit()
                await cursor.close()
                return False


async def db_get_user(what_get: str) -> tuple:
    """What_get must be 'rbc' or 'kremlin'."""
    async with aiosqlite.connect(DATABASE_PATH) as connect:
        cursor = await connect.cursor()
        if what_get == "rbc":
            await cursor.execute("SELECT user_id FROM users WHERE rbc_notify=1")
            return await cursor.fetchall()

        elif what_get == "kremlin":
            await cursor.execute("SELECT user_id FROM users WHERE kremlin_notify=1")
            return await cursor.fetchall()

        elif what_get == "lenta":
            await cursor.execute("SELECT user_id FROM users WHERE lenta_notify=1")
            return await cursor.fetchall()
