from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    # serializer.CharField로 할시에는 문자로 변환되어 나옴
    # pk = serializers.CharField()
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        max_length=15,
    )
    created_at = serializers.DateTimeField(read_only=True)
