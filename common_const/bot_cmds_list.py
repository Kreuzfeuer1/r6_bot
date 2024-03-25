from aiogram.types import BotCommand

private = [
    BotCommand(command='tournaments', description='ближайшие турниры'),
    BotCommand(command='matches', description='ближайшие матчи'),
    BotCommand(command='follow_teams', description='отслеживаемые команды'),
    BotCommand(command='results', description='результаты последних матчей')
]