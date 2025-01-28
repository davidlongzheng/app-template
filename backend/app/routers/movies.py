from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.backend.session import create_session
from app.schemas.auth import UserSchema
from app.schemas.movies import MovieSchema
from app.services.auth import get_current_user
from app.services.movies import MovieService

router = APIRouter(prefix="/movies")


@router.get("/", response_model=MovieSchema)
async def get_movie(
    movie_id: int,
    user: UserSchema = Depends(get_current_user),
    session: Session = Depends(create_session),
) -> MovieSchema:
    return MovieService(session).get_movie(movie_id)


@router.get("/new", response_model=List[MovieSchema])
async def get_new_movies(
    year: int, rating: float, session: Session = Depends(create_session)
) -> List[MovieSchema]:
    return MovieService(session).get_movies(year, rating)
