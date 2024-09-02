from django.http import JsonResponse
from django.core import serializers

# Django serializers로 json을 나타낼 수 있으나 reponse를 커스터마이징 할 수 없어서 별로임
# 예를들어 pk를 제외한다거나 이런게 불가능함, Django RestFramework 사용하는게 나ㅡㅇㅁ
from .models import Category


def categories(request):
    all_categories = Category.objects.all()  # Create your views here.
    return JsonResponse(
        {
            "ok": True,
            "categories": serializers.serialize("json", all_categories),
        }
    )
