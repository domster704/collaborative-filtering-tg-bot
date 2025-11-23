from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.domain.entities.movie import Movie
from src.presentation.dependencies.movies import get_movies_use_case
from src.presentation.keyboards.pagination import Pagination
from src.utils.get_movie_pagination import get_movie_pagination

movies_router = Router()


@movies_router.message(F.text == "Список фильмов")
async def movies_start(message: Message, state: FSMContext):
    movies_uc = get_movies_use_case()
    movies: list[Movie] = await movies_uc.execute()

    pagination: Pagination = get_movie_pagination(
        movies, callback_data_navigation_ending="movies"
    )
    await state.update_data(pagination=pagination)

    await message.answer(text="Список фильмов:", reply_markup=pagination.get_markup())
