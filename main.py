import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from database.engine import create_db, drop_db
from handlers.user_private import user_private_router
from handlers.group import group_router
from handlers.admin_private import admin_router
from common_const.bot_cmds_list import private


ALLOWED_UPDATES = ['message, edited-message']

bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)


db = Dispatcher(fsm_strategy = FSMStrategy.USER_IN_CHAT)

db.include_router(user_private_router)
db.include_router(group_router)
db.include_router(admin_router)


async def on_start(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Бот лёг')


async def main():
    db.startup.register(on_start)
    db.shutdown.register(on_shutdown)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await db.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
    