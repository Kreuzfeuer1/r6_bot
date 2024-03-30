import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.group import group_router
from handlers.admin_private import admin_router
from common_const.bot_cmds_list import private


ALLOWED_UPDATES = ['message, edited-message']

bot = Bot(token=os.getenv('TOKEN'))


db = Dispatcher()

db.include_router(user_private_router)
db.include_router(group_router)
db.include_router(admin_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await db.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
    