from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories.models import Category
from .serializer import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories, many=True
        )  # many=True는 카테코리가 배열이라고 알려주는 것임
        return Response(serializer.data)
    elif request.method == "POST":
        # {
        #     "name": "jaejun",
        #     "kind": "test"
        # }
        # json형태로 안보내면 실패함
        # print(request.data)

        # 아래와 같이 생성을 할 수는 있으나 Valdiation이 안되었기 때문에 오류가 발생할 수 있어 좋지 않음
        Category.objects.create(
            name=request.data["name"],
            kind=request.data["kind"],
        )
        return Response({"created": True})


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
