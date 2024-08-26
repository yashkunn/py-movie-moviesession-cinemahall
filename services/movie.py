from django.db.models import QuerySet, Q

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet | Movie:
    queryset = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return queryset
    if genres_ids and actors_ids:
        return queryset.filter(
            Q(genres__id__in=genres_ids) & Q(actors__id__in=actors_ids)
        ).distinct()
    if genres_ids:
        return queryset.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        return queryset.filter(actors__id__in=actors_ids).distinct()
    return queryset


def get_movie_by_id(id_: int) -> Movie:
    return Movie.objects.get(id=id_)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
    return movie
