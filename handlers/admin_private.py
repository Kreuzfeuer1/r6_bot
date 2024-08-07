from aiogram import F, Router, types
from aiogram.filters import Command, or_f, StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import orm_add_team, orm_get_all_teams, orm_delete_team

from fsm.admin_fsm import AddTeam

from filters.chat_types_filters import ChatTypeFilter, IsAdmin

from keyboards import admin_reply_keyboards, inline_keyboards


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


@admin_router.message(or_f(Command('admin'), (F.text == 'В админку')))
async def start_admin_cmd(message: types.Message):
    await message.answer(
        'Что желаете сделать?',
        reply_markup=admin_reply_keyboards.start_admin_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Удачи"))


@admin_router.message(F.text == 'Список команд')
async def get_team_list(message: types.Message, session: AsyncSession):
    for team in await orm_get_all_teams(session=session):
        await message.answer(
            team.name,
            reply_markup=inline_keyboards.get_callback_buttons(buttons={
                'Удалить': f'delete_{team.id}',
                'Изменить': f'change_{team.id}',
            }))
    await message.answer('Вот список команд')


@admin_router.callback_query(F.data.startswith('delete_'))
async def delete_team(callback: types.CallbackQuery, session: AsyncSession):
    team_id = callback.data.split("_")[-1]
    await orm_delete_team(session, int(team_id))
    await callback.answer("Команда удалена")
    await callback.message.answer("Команда удалёна")


@admin_router.message(F.text == 'Зашёл просто так')
async def starring(message: types.Message):
    await message.answer(
        'Окей',
        reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Что вас интересует?"))


"""FSM code for cancel all actions"""


@admin_router.message(StateFilter('*'), F.text.casefold() == 'отмена действия')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        "Отмена действия",
        reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
            resize_keyboard=True))


@admin_router.message(StateFilter('*'), F.text == 'Шаг назад')
async def cancel_previous_step(message: types.Message, state: FSMContext):
    current_step = await state.get_state()
    if current_step == AddTeam.name:
        await message.answer(
            "Вы были на первом шаге, добавление команды отменено",
            reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
                resize_keyboard=True))
        await state.clear()
    else:
        previous = None
        for step in AddTeam.__all_states__:
            if step.state == current_step:
                await state.set_state(previous)
                await message.answer(
                    f"Вы вернулись к предыдущему шагу,\n {AddTeam.texts[previous.state]}")
                return
            previous = step


@admin_router.message(StateFilter(None), F.text == 'Добавить команду')
async def start_adding_team(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите название команды",
        reply_markup=admin_reply_keyboards.fsm_keyboard.as_markup(
            resize_keyboard=True))
    await state.set_state(AddTeam.name)


@admin_router.message(StateFilter(AddTeam.name), F.text)
async def add_first_palyer(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите nickname первого игрока")
    await state.set_state(AddTeam.first_player)


@admin_router.message(StateFilter(AddTeam.name))
async def err_add_first_palyer(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, введите название команды текстом")


@admin_router.message(StateFilter(AddTeam.first_player), F.text)
async def add_second_player(message: types.Message, state: FSMContext):
    await state.update_data(first_player=message.text)
    await message.answer("Введите nickname второго игрока")
    await state.set_state(AddTeam.second_player)


@admin_router.message(StateFilter(AddTeam.first_player))
async def err_add_second_player(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, введите nickname игрока текстом")


@admin_router.message(StateFilter(AddTeam.second_player), F.text)
async def add_third_player(message: types.Message, state: FSMContext):
    await state.update_data(second_player=message.text)
    await message.answer("Введите nickname третьего игрока")
    await state.set_state(AddTeam.third_player)


@admin_router.message(StateFilter(AddTeam.second_player))
async def err_add_third_player(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, введите nickname игрока текстом")


@admin_router.message(StateFilter(AddTeam.third_player), F.text)
async def add_fourth_player(message: types.Message, state: FSMContext):
    await state.update_data(third_player=message.text)
    await message.answer("Введите nickname четвёртого игрока")
    await state.set_state(AddTeam.fourth_player)


@admin_router.message(StateFilter(AddTeam.third_player))
async def err_add_fourth_player(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, введите nickname игрока текстом")


@admin_router.message(StateFilter(AddTeam.fourth_player), F.text)
async def add_fifth_player(message: types.Message, state: FSMContext):
    await state.update_data(fourth_player=message.text)
    await message.answer("Введите nickname пятого игрока")
    await state.set_state(AddTeam.fifth_player)


@admin_router.message(StateFilter(AddTeam.fourth_player))
async def err_add_fifth_player(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, введите nickname игрока текстом")


@admin_router.message(StateFilter(AddTeam.fifth_player), F.text)
async def add_coach(message: types.Message, state: FSMContext):
    await state.update_data(fifth_player=message.text)
    await message.answer("Введите nickname тренера")
    await state.set_state(AddTeam.coach)


@admin_router.message(StateFilter(AddTeam.fifth_player))
async def err_add_coach(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, введите nickname игрока текстом")


@admin_router.message(StateFilter(AddTeam.coach), F.text)
async def add_logo(message: types.Message, state: FSMContext):
    await state.update_data(coach=message.text)
    await message.answer("Отправте логотип команды")
    await state.set_state(AddTeam.logo)


@admin_router.message(StateFilter(AddTeam.logo), F.photo)
async def end_adding_team(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(logo=message.photo[-1].file_id)
    data = await state.get_data()
    try:
        await orm_add_team(session=session, data=data)
        await message.answer(
            "Команда добавлена",
            reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
                resize_keyboard=True))
        await state.clear()
    except Exception as err:
        await message.answer(
            f"Ошибка: \n{str(err)}\nнадо что-то с этим делать",
            reply_markup=admin_reply_keyboards.default_admin_keyboard.as_markup(
                resize_keyboard=True))
        await state.clear()


@admin_router.message(StateFilter(AddTeam.logo))
async def err_end_adding_team(message: types.Message, state: FSMContext):
    await message.answer("Вы введи не допустимые данные, отправте логотип команды файлом")


@admin_router.message(or_f(Command('add_tournament'), (F.text == 'Добавить турнир')))
async def add_tournament(message: types.Message):
    await message.answer('Начало добавления турнира')