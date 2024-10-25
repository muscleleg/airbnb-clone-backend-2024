from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Review


class ReviewsSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ("user", "payload", "rating",)
