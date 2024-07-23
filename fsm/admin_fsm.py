from aiogram.fsm.state import State, StatesGroup



"""FSM for add team"""


class AddTeam(StatesGroup):
    name = State()
    first_player = State()
    second_player = State()
    third_player = State()
    fourth_player = State()
    fifth_player = State()
    coach = State()
    logo = State()
    texts = {
        'AddTeam:name': 'введите название команды заново',
        'AddTeam:first_player': 'введите nickname первого игрока заново',
        'AddTeam:second_player': 'введите nickname второго игрока заново',
        'AddTeam:third_player': 'введите nickname третьего игрока заново',
        'AddTeam:fourth_player': 'введите nickname четвёртого игрока заново',
        'AddTeam:fifth_player': 'введите nickname пятого игрока заново',
        'AddTeam:coach': 'введите nickname тренера заново',
    }