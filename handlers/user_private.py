from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards import reply_keyboards

from database.orm_query import orm_get_all_teams

user_private_router = Router()


@user_private_router.message(or_f(CommandStart(), (F.text == 'Назад')))
async def start_cmd(message: types.Message):
    await message.answer(
        'Что вас интересует?',
        reply_markup=reply_keyboards.start_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что вас интересует?'))


@user_private_router.message(or_f(Command('tournaments'), (F.text == 'Турниры')))
async def tournaments_cmd(message: types.Message):
    await message.answer(
        'Какие туниры вас интересуют?',
        reply_markup=reply_keyboards.tournaments_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что вас интересует?'))


@user_private_router.message(or_f(Command('matches'), (F.text == 'Ближайшие матчи')))
async def matches_cmd(message: types.Message):
    await message.answer('Ближайшие матчи')


@user_private_router.message(or_f(Command('follow_teams'), (F.text == 'Отслеживаемые команды')))
async def follow_teams_cmd(message: types.Message):
    await message.answer(
        'Ваши отслеживаемы команды',
        reply_markup=reply_keyboards.follow_teams_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что вас интересует?'))


"""FSM code for cancel all actions"""


@user_private_router.message(StateFilter('*'), Command('отмена'))
@user_private_router.message(StateFilter('*'), F.text.casefold() == 'отмена')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        'Действия отменены',
        reply_markup=reply_keyboards.start_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что вас интересует?'))


"""FSM code for adding follow team"""


class AddFollowTeam(StatesGroup):
    name = State()


@user_private_router.message(StateFilter(None), F.text == 'Добавить отслеживаемую команду')
async def add_follow_team_name(message: types.Message, state: FSMContext, session: AsyncSession):
    for team in await orm_get_all_teams(session=session):
        await message.answer(team.name)
    await message.answer(
        'Введите название команды из приведённого выше списка',
        reply_markup=reply_keyboards.fsm_keyboard.as_markup(
            resize_keyboard=True,
        ))
    await state.set_state(AddFollowTeam.name)


@user_private_router.message(StateFilter(AddFollowTeam.name), F.text)
async def end_adding_follow_team(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        'Добавление завершено',
        reply_markup=reply_keyboards.start_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что вас интересует?'))
    await state.clear()


@user_private_router.message(StateFilter(AddFollowTeam.name))
async def err_end_adding_follow_team(message: types.Message, state: FSMContext):
    await message.answer('Вы введи не допустимые данные, введите название команды текстом')


"""FSM code for delete team from follow teams"""


class DeleteFollowTeam(StatesGroup):
    name = State()


@user_private_router.message(StateFilter(None), F.text == 'Удалить команду из отслеживаемых')
async def start_deletion_follow_team(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите название команды, которой хотите удалить',
        reply_markup=reply_keyboards.fsm_keyboard.as_markup(
            resize_keyboard=True))
    await state.set_state(DeleteFollowTeam.name)


@user_private_router.message(StateFilter(DeleteFollowTeam.name), F.text)
async def ending_delete_follow_team(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        'Удаление завершено',
        reply_markup=reply_keyboards.start_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что вас интересует?'))
    await state.clear()


@user_private_router.message(StateFilter(DeleteFollowTeam.name))
async def err_ending_delete_follow_team(message: types.Message, state: FSMContext):
    await message.answer('Вы введи не допустимые данные, введите название команды текстом')


@user_private_router.message(or_f(Command('results'), (F.text == 'Результаты последних матчей')))
async def result_cmd(message: types.Message):
    await message.answer('Вот результаты последних матчей')