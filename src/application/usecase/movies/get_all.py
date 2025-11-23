from src.infrastructure.repositories.movie_repository import APIMovieRepository


class MoviesGetAllUseCase:
    def __init__(self, repo: APIMovieRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.get_all()
