from rest_framework import serializers
from .models import *


class RatingSerializer(serializers.ModelSerializer):
        model = Rating
        fields = ("Source", "Value")


class MovieSerializer(serializers.ModelSerializer):
    Ratings = RatingSerializer(many=True)
    model = Movie
    fields = '__all__'