from aiogram import F, Router, types
from aiogram.filters import Command, or_f

from filters.chat_types_filters import ChatTypeFilter, IsAdmin
from keyboards import admin_reply_keyboards



admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


@admin_router.message(or_f(Command('admin'), (F.text == 'В админку')))
async def start_admin_cmd(message: types.Message):
    await message.answer('Что желаете сделать?',
            reply_markup=admin_reply_keyboards.start_admin_keyboard.as_markup(
                resize_keyboard=True,
                input_field_placeholder="Удачи"))


@admin_router.message(F.text == 'Зашёл просто так')
async def starring(message: types.Message):
    await message.answer('Окей',
            reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
                resize_keyboard=True,
                input_field_placeholder="Что вас интересует?"))


"""FSM for add team"""
@admin_router.message(F.text == 'Добавить команду')
async def start_adding_team(message: types.Message):
    await message.answer("Введите название команды",
            reply_markup=admin_reply_keyboards.fsm_keyboard.as_markup(
            resize_keyboard=True))


@admin_router.message(F.text == 'Отмена')
async def cancel_handler(message: types.Message):
    await message.answer("Отмена действия",
            reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
                resize_keyboard=True))


@admin_router.message(F.text == 'Шаг назад')
async def cancel_last_step(message: types.Message):
    await message.answer("Вы вернулись на предыдущий шаг")





@admin_router.message(or_f(Command('add_tournament'), (F.text == 'Добавить турнир')))
async def add_tournament(message: types.Message):
    await message.answer('Начало добавления турнира')