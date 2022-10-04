from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status

from .models import Movie
from .permissions import IsAdminOrReadOnly
from .serializer import MovieSerializer


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetaisView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
