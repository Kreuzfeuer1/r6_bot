from aiogram.fsm.state import State, StatesGroup


"""FSM code for adding follow team"""
class AddFollowTeam(StatesGroup):
    name = State()


"""FSM code for delete team from follow teams"""
class DeleteFollowTeam(StatesGroup):
    name = State()