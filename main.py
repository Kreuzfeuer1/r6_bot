import asyncio
import os
from aiogram import Bot, Dispatcher, types

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('TOKEN'))

db = Dispatcher()


async def main():
    await db.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
    