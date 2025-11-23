from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.domain.entities.movie import Movie
from src.presentation.dependencies.movies import get_recommendations_use_case
from src.presentation.keyboards.pagination import Pagination
from src.utils.get_movie_pagination import get_movie_pagination

recommend_router = Router()


@recommend_router.message(F.text == "Получить рекомендации")
async def get_recommendations(message: Message, state: FSMContext):
    use_case = get_recommendations_use_case()
    recommended_movies: list[Movie] = await use_case.execute(message.from_user.id)

    pagination: Pagination = get_movie_pagination(
        recommended_movies, callback_data_navigation_ending="recommendations"
    )
    await state.update_data(pagination=pagination)

    await message.answer(
        text="Фильмы, которые подходят тебе:", reply_markup=pagination.get_markup()
    )
