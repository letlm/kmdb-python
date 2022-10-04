from rest_framework import serializers
from rest_framework.exceptions import APIException
from users.serializers import UserCriticSerializer

from .models import Review


class AlreadyExists(APIException):
    status_code = 403


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserCriticSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
            "recomendation",
        ]
        read_only_fields = ["id", "critic", "movie_id"]
        extra_kwargs = {"stars": {"min_value": 1, "max_value": 10}}

    def create(self, validated_data: dict):
        critic = self.context.get("critic")
        movie_id = self.context.get("movie_id")

        validated_data.update({"critic": critic})
        validated_data.update({"movie_id": movie_id})

        confered_keys = {"critic": critic, "movie_id": movie_id}

        if Review.objects.filter(**confered_keys).exists():
            raise AlreadyExists({"detail": "Review already exists."})

        review = Review.objects.create(**validated_data)

        return review
