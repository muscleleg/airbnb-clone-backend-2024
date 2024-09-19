from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    # serializer.CharField로 할시에는 문자로 변환되어 나옴
    # pk = serializers.CharField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
