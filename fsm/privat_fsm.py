from aiogram.fsm.state import State, StatesGroup


"""FSM code for adding follow team"""


class AddFollowTeam(StatesGroup):
    name = State()