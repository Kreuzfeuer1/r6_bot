from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.reply_keyboards import start_keyboard


start_admin_keyboard = ReplyKeyboardBuilder()
start_admin_keyboard.add(
    KeyboardButton(text="Список команд"),
    KeyboardButton(text="Добавить команду"),
    KeyboardButton(text="Добавить турнир"),
    KeyboardButton(text="Зашёл просто так"),
)
start_admin_keyboard.adjust(2, 1, 1)


default_admin_keyboard = ReplyKeyboardBuilder()
default_admin_keyboard.attach(start_keyboard)
default_admin_keyboard.row(
    KeyboardButton(text="В админку"),
)


fsm_keyboard = ReplyKeyboardBuilder()
fsm_keyboard.add(
    KeyboardButton(text='Шаг назад'),
    KeyboardButton(text='Отмена действия'),
)
fsm_keyboard.adjust(2, )