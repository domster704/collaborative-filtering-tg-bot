from src.application.usecase.rating.create import RatingCreateUseCase
from src.config.config import API_URL
from src.infrastructure.repositories.rating_repository import APIRatingRepository


def get_rating_create_use_case():
    repo = APIRatingRepository(API_URL)
    return RatingCreateUseCase(repo)
