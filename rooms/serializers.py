from django.template.context_processors import request
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializer import CategorySerializer
from reviews.serializers import ReviewsSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )
        # read_only_fields = ("created_at",)  # 읽기 전용으로 설정할 필드


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(
        read_only=True,
    )

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        print(self.context)
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    def get_is_liked(self, room):
        request = self.context["request"]
        return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()

    # def create(self, validated_data):
    #     return Room.objects.create(**validated_data)


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


# ModelSerializer를 상속받았기 때문에 id, created_at,updated_at이 readonly로 자동 지임정된거임


# readOnly를 수동으로 지정해주는 예예
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)  # 읽기 전용
#     name = serializers.CharField()  # 쓰기 가능
#     kind = serializers.CharField()  # 쓰기 가능
#     created_at = serializers.DateTimeField(read_only=True)  # 읽기 전용
