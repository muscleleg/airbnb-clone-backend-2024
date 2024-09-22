from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    # serializer.CharField로 할시에는 문자로 변환되어 나옴
    # pk = serializers.CharField()
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        # print(validated_data)
        return Category.objects.create(
            **validated_data,
        )
        ## **연산자는 딕셔너리에있는 데이터를 자동으로 파싱해줌 {"name":"test", "kind": "experiences"} -> name = "test" kind = "experineces"
