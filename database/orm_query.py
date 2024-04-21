from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Team


async def orm_add_team(session: AsyncSession, data: dict):
    object_team = Team(
        name = data["name"],
        first_player = data["first_player"],
        second_player = data["second_player"],
        third_player = data["third_player"],
        fourth_player = data["fourth_player"],
        fifth_player = data["fifth_player"],
        coach = data["coach"],
        logo = data["logo"],
    )
    session.add(object_team)
    await session.commit()


async def orm_get_all_teams(session: AsyncSession):
    query = select(Team)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_team(session: AsyncSession, team_id: int):
    query = select(Team).where(Team.id == team_id)
    result = await session.execute(query)
    await result.commit()


async def orm_delete_team(session: AsyncSession, team_id: int):
    query = delete(Team).where(Team.id == team_id)
    await session.execute(query)
    await session.commit()