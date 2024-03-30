from aiogram import  F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from keyboards import  reply_keyboards

user_private_router = Router()

@user_private_router.message(or_f(CommandStart(), (F.text == 'Назад')))
async def start_cmd(message: types.Message):
    await message.answer('Что вас интересует?',
            reply_markup=reply_keyboards.start_keyboard.as_markup(
                resize_keyboard=True,
                input_field_placeholder='Что вас интересует?'))


@user_private_router.message(or_f(Command('tournaments'), (F.text == 'Турниры')))
async def tournaments_cmd(message: types.Message):
    await message.answer('Какие туниры вас интересуют?',
            reply_markup=reply_keyboards.tournaments_keyboard.as_markup(
                resize_keyboard=True,
                input_field_placeholder='Что вас интересует?'))


@user_private_router.message(or_f(Command('matches'), (F.text == 'Ближайшие матчи')))
async def matches_cmd(message: types.Message):
    await message.answer('Ближайшие матчи')


@user_private_router.message(or_f(Command('follow_teams'), (F.text == 'Отслеживаемые команды')))
async def follow_teams_cmd(message: types.Message):
    await message.answer('Ваши отслеживаемы команды',
            reply_markup=reply_keyboards.follow_teams_keyboard.as_markup(
                resize_keyboard=True,
                input_field_placeholder='Что вас интересует?'))


@user_private_router.message(or_f(Command('results'), (F.text == 'Результаты последних матчей')))
async def result_cmd(message: types.Message):
    await message.answer('Вот результаты последних матчей')