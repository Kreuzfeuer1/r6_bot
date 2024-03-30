from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_keyboard = ReplyKeyboardBuilder()
start_keyboard.add(
    KeyboardButton(text="Турниры"),
    KeyboardButton(text="Ближайшие матчи"),
    KeyboardButton(text="Отслеживаемые команды"),
    KeyboardButton(text="Результаты последних матчей")
)
start_keyboard.adjust(2, 2)


follow_teams_keyboard = ReplyKeyboardBuilder()
follow_teams_keyboard.add(
    KeyboardButton(text='Добавить команду'),
    KeyboardButton(text='Удалить команду'),
    KeyboardButton(text='Назад')
)
follow_teams_keyboard.adjust(2, 1)


tournaments_keyboard = ReplyKeyboardBuilder()
tournaments_keyboard.add(
    KeyboardButton(text='Прошедшие'),
    KeyboardButton(text='Предстоящие'),
    KeyboardButton(text='Назад')
)
tournaments_keyboard.adjust(2,)