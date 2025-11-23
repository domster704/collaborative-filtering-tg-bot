from dataclasses import dataclass

from src.domain.entities.movie import Movie
from src.domain.entities.user import UserModel


@dataclass(frozen=True, slots=True)
class Rating:
    user: UserModel
    movie: Movie
    rating: int
    timestamp: int | None
