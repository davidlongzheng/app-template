from typing import List

from sqlalchemy import select

from app.models.movies import MovieModel
from app.schemas.movies import MovieSchema
from app.services.base import BaseDataManager, BaseService


class MovieService(BaseService):
    async def get_movie(self, movie_id: int) -> MovieSchema:
        return await MovieDataManager(self.session).get_movie(movie_id)

    async def get_movies(self, year: int, rating: float) -> List[MovieSchema]:
        return await MovieDataManager(self.session).get_movies(year, rating)


class MovieDataManager(BaseDataManager):
    async def get_movie(self, movie_id: int) -> MovieSchema:
        stmt = select(MovieModel).where(MovieModel.movie_id == movie_id)
        model = await self.get_one(stmt)

        return MovieSchema(**model.to_dict())

    async def get_movies(self, year: int, rating: float) -> List[MovieSchema]:
        schemas: List[MovieSchema] = list()

        stmt = select(MovieModel).where(
            MovieModel.released >= year,
            MovieModel.rating >= rating,
        )

        models = await self.get_all(stmt)
        for model in models:
            schemas.append(MovieSchema(**model.to_dict()))

        return schemas
