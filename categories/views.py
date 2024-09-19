from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories.models import Category
from .serializer import CategorySerializer


@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(
        all_categories, many=True
    )  # many=True는 카테코리가 배열이라고 알려주는 것임
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        }
    )
