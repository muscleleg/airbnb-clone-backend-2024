from rest_framework.serializers import ModelSerializer
from .models import Amenity


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
        # read_only_fields = ("created_at",)  # 읽기 전용으로 설정할 필드


# ModelSerializer를 상속받았기 때문에 id, created_at,updated_at이 readonly로 자동 지임정된거임


# readOnly를 수동으로 지정해주는 예예
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)  # 읽기 전용
#     name = serializers.CharField()  # 쓰기 가능
#     kind = serializers.CharField()  # 쓰기 가능
#     created_at = serializers.DateTimeField(read_only=True)  # 읽기 전용
