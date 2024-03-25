from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ближайшие турниры"),
            KeyboardButton(text="Ближайшие матчи"),
        ],
        [
            KeyboardButton(text="Отслеживаемые команды"),
            KeyboardButton(text="Результаты последних матчей")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)