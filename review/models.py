from django.db import models


class Recomendation(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    NO_OPINION = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(null=True, blank=True, default=False)
    recomendation = models.CharField(
        max_length=50, choices=Recomendation.choices, default=Recomendation.NO_OPINION
    )

    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )

    movie_id = models.ForeignKey(
        "movie.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
