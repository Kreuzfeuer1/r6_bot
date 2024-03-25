from aiogram import  F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from keyboards import  reply_keyboards

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('команда старт', reply_markup=reply_keyboards.start_keyboard)

@user_private_router.message(or_f(Command('tournaments'), (F.text == 'Ближайшие турниры')))
async def tournaments_cmd(message: types.Message):
    await message.answer('Список ближайших турниров')

@user_private_router.message(or_f(Command('matches'), (F.text == 'Ближайшие матчи')))
async def matches_cmd(message: types.Message):
    await message.answer('Ближайшие матчи')

@user_private_router.message(or_f(Command('follow_teams'), (F.text == 'Отслеживаемые команды')))
async def follow_teams_cmd(message: types.Message):
    await message.answer('Ваши отслеживаемы команды')

@user_private_router.message(or_f(Command('results'), (F.text == 'Результаты последних матчей')))
async def result_cmd(message: types.Message):
    await message.answer('Вот результаты последних матчей')