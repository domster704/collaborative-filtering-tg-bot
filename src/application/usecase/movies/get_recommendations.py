from src.domain.entities.movie import Movie
from src.infrastructure.exceptions import InfrastructureError
from src.infrastructure.repositories.movie_repository import APIMovieRepository


class MoviesGetRecommendationsUseCase:
    def __init__(self, repo: APIMovieRepository):
        self.repo = repo

    async def execute(self, tg_user_id: int, top_n: int = 10) -> list[Movie]:
        try:
            return await self.repo.get_recommendations(tg_user_id, top_n)
        except InfrastructureError as e:
            return []
