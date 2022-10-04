from genre.models import Genre
from genre.serializer import GenreSerializer
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    premiere = serializers.DateField()
    duration = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:
        genre_movie = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for genre in genre_movie:
            genre_save, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre_save)

        return movie

    def update(self, instance, validated_data):
        if "genres" in validated_data.keys():
            instance.genres.clear()
            genres = validated_data.pop("genres")

            for genre in genres:

                new_genres, _ = Genre.objects.get_or_create(**genre)

                instance.genres.add(new_genres)

            for key, value in validated_data.items():
                setattr(instance, key, value)

            instance.save()

            return instance
