from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    if session_date:
        date_object = datetime.strptime(session_date, "%Y-%m-%d").date()

        return MovieSession.objects.filter(show_time__date=date_object)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:
    try:
        movie_session = MovieSession.objects.get(id=session_id)

        if show_time:
            movie_session.show_time = show_time
        if movie_id:
            movie_session.movie_id = movie_id
        if cinema_hall_id:
            movie_session.cinema_hall_id = cinema_hall_id

        movie_session.save()

        return movie_session
    except MovieSession.DoesNotExist:
        raise ValueError(f"MovieSession with id {session_id} does not exist.")


def delete_movie_session_by_id(movie_session_id: int) -> None:
    movie_session = MovieSession.objects.filter(id=movie_session_id)
    if movie_session.exists():
        movie_session.delete()
    else:
        raise ValueError(
            f"MovieSession with id {movie_session_id} does not exist."
        )
