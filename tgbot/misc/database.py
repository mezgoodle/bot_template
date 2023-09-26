from tgbot.models.models import Event, Team, Tournament


class Database:
    def __init__(self):
        self.tournament = Tournament
        self.event = Event
        self.team = Team

    async def create_tournament(self, name: str) -> Tournament:
        return await self.tournament.create(name=name)

    async def create_team(self, name: str) -> Team:
        return await self.team.create(name=name)

    async def create_event(
        self, name: str, tournament_name: str, participants: list[int]
    ) -> Event:
        if (
            tournament := await self.tournament.get_or_create(
                name=tournament_name
            )
        ) and (teams := await self.team.filter(id__in=participants)):
            return await self.event.create(
                name=name, tournament=tournament, participants=teams
            )

    async def get_teams(self) -> list[Team]:
        return await self.team.all()
