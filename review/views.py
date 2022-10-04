from django.shortcuts import get_object_or_404
from movie.models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.permissions import IsCritic

from review.permissions import IsCriticOrAdmin

from .models import Review
from .serializer import ReviewSerializer


class NotFound(APIException):
    status_code = 400


class ReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCritic]

    def get(self, request: Request, movie_id: int) -> Response:
        reviews = Review.objects.filter(movie_id=movie_id)
        if not reviews:
            raise NotFound({"detail": "Not found."})

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        user = get_object_or_404(User, id=request.user.id)

        self.check_object_permissions(request, user)

        serializer = ReviewSerializer(
            data=request.data, context={"movie_id": movie, "critic": request.user}
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewDetailsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCriticOrAdmin]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        reviews = Review.objects.filter(id=review_id)
        movie_review = get_object_or_404(reviews, movie_id=movie_id)

        serializer = ReviewSerializer(movie_review)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int, review_id: int) -> Response:

        validated = {"id": review_id, "movie_id": movie_id}
        reviews = get_object_or_404(Review, **validated)

        self.check_object_permissions(request, reviews.critic)

        reviews.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
