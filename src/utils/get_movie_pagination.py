from aiogram.filters.callback_data import CallbackData

from src.domain.entities.movie import Movie
from src.presentation.keyboards.pagination import PaginationItems, Pagination


class MovieCallbackData(CallbackData, prefix="movie"):
    id: int


def get_movie_pagination(
    movies: list[Movie],
    callback_data_navigation_ending: str,
    max_items_per_page: int = 5,
) -> Pagination:
    items: list[PaginationItems] = []
    for m in movies:
        items.append(
            PaginationItems(text=m.title, callback_data=MovieCallbackData(id=m.id))
        )

    pagination = Pagination(
        items=items,
        max_items_per_page=max_items_per_page,
        callback_data_navigation_ending=callback_data_navigation_ending,
    )

    return pagination
