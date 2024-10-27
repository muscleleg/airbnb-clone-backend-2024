from rest_framework.serializers import ModelSerializer
from .models import Wishlists


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlists
        fields = "__all__"
