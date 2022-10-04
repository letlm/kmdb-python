from django.urls import path
from review.views import ReviewDetailsView, ReviewView

from . import views

urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<int:movie_id>/", views.MovieDetaisView.as_view()),
    path("movies/<int:movie_id>/reviews/", ReviewView.as_view()),
    path(
        "movies/<int:movie_id>/reviews/<int:review_id>/",
        ReviewDetailsView.as_view(),
    ),
]
