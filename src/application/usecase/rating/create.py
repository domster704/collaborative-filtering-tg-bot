from src.domain.entities.raiting import Rating


class RatingCreateUseCase:
    def __init__(self, rating_repository):
        self.rating_repository = rating_repository

    async def execute(self, rating: Rating):
        return await self.rating_repository.add(rating)
